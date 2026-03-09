from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3

from database import init_db
from chatbot import chatbot_response

import smtplib
from email.mime.text import MIMEText


app = Flask(__name__)
app.secret_key = "secret123"

init_db()


def connect():
    return sqlite3.connect("complaints.db")


# ---------------- EMAIL FUNCTION ---------------- #

def send_email(user_email, complaint, category, priority):

    subject = "Complaint Ticket Created"

    body = f"""
Hello,

Your complaint has been successfully registered.

Complaint: {complaint}

Category: {category}
Priority: {priority}

Our support team will review your issue shortly.

Thank you,
Complaint Management System
"""

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = "your_email@gmail.com"
    msg["To"] = user_email

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login("your_email@gmail.com", "your_app_password")

        server.send_message(msg)

        server.quit()

        print("Email sent successfully")

    except Exception as e:

        print("Email sending failed:", e)



# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = connect()
        cursor = conn.cursor()

        user = cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email,password)
        ).fetchone()

        conn.close()

        if user:
            session["user_id"] = user[0]
            session["email"] = user[2]

            return redirect("/")

    return render_template("login.html")



# ---------------- REGISTER ---------------- #

@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
        "INSERT INTO users(name,email,password) VALUES(?,?,?)",
        (name,email,password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")



# ---------------- HOME PAGE ---------------- #

@app.route("/")
def home():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("index.html")



# ---------------- CHATBOT ---------------- #

@app.route("/chatbot", methods=["POST"])
def chatbot():

    data = request.get_json()

    message = data["message"]

    category, priority, team, reply = chatbot_response(message)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO complaints(user_id,complaint,category,priority,team,status)
    VALUES(?,?,?,?,?,?)
    """,(session["user_id"], message, category, priority, team, "Open"))

    conn.commit()

    conn.close()


    # SEND EMAIL
    send_email(session["email"], message, category, priority)


    return jsonify({"reply": reply})



# ---------------- DASHBOARD ---------------- #

@app.route("/dashboard")
def dashboard():

    conn = connect()
    cursor = conn.cursor()

    tickets = cursor.execute("SELECT * FROM complaints").fetchall()

    total = cursor.execute(
    "SELECT COUNT(*) FROM complaints"
    ).fetchone()[0]

    technical = cursor.execute(
    "SELECT COUNT(*) FROM complaints WHERE category='technical'"
    ).fetchone()[0]

    billing = cursor.execute(
    "SELECT COUNT(*) FROM complaints WHERE category='billing'"
    ).fetchone()[0]

    service = cursor.execute(
    "SELECT COUNT(*) FROM complaints WHERE category='service'"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        tickets=tickets,
        total=total,
        technical=technical,
        billing=billing,
        service=service
    )



# ---------------- UPDATE STATUS ---------------- #

@app.route("/update_status/<int:id>/<status>")
def update_status(id,status):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
    "UPDATE complaints SET status=? WHERE id=?",
    (status,id)
    )

    conn.commit()
    conn.close()

    return redirect("/dashboard")



# ---------------- TRACK COMPLAINT ---------------- #

@app.route("/track", methods=["GET","POST"])
def track():

    ticket=None

    if request.method=="POST":

        ticket_id=request.form["ticket_id"]

        conn=connect()
        cursor=conn.cursor()

        ticket=cursor.execute(
        "SELECT * FROM complaints WHERE id=?",
        (ticket_id,)
        ).fetchone()

        conn.close()

    return render_template("track.html",ticket=ticket)



# ---------------- MY TICKETS ---------------- #

@app.route("/my_tickets")
def my_tickets():

    conn=connect()
    cursor=conn.cursor()

    tickets=cursor.execute(
    "SELECT * FROM complaints WHERE user_id=?",
    (session["user_id"],)
    ).fetchall()

    conn.close()

    return render_template("my_tickets.html",tickets=tickets)



# ---------------- RUN SERVER ---------------- #

if __name__ == "__main__":
    app.run(debug=True)