# Complaint-Management-System-with-Chatbot-Integration-Ticket-Support-Generation
AI-powered complaint management system with chatbot integration that automatically categorizes user complaints, assigns priority, generates support tickets, and enables real-time tracking through an admin dashboard.

## Overview

The **AI-Powered Complaint Management System** is a web-based application that allows users to submit complaints through an intelligent chatbot interface. The system automatically analyzes user complaints using machine learning techniques and generates support tickets with appropriate categories, priority levels, and assigned teams.

This solution helps organizations automate complaint handling, improve response time, and efficiently manage customer issues through an admin dashboard.

---

## Features

### User Features

* User registration and login authentication
* Submit complaints through a chatbot interface
* Automatic ticket generation
* Track complaint status using Ticket ID
* View personal complaint history


### Admin Features

* Dashboard to monitor all complaints
* Complaint statistics and analytics
* Update ticket status (Open → In Progress → Resolved)
* Manage complaint workflow efficiently

---

## Technologies Used

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn
* **NLP Techniques:** TF-IDF Vectorization, Naive Bayes Classifier
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

## Project Structure

```text
Complaint-Management-System
│
├── app.py
├── chatbot.py
├── model.py
├── database.py
├── complaints.db
│
├── templates
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── track.html
│   └── my_tickets.html
│
├── static
│   ├── chatbot.js
│   └── style.css
│
└── README.md
```

---

## System Workflow

1. User logs into the system.
2. User submits a complaint through the chatbot interface.
3. The system analyzes the complaint using a machine learning model.
4. The complaint is categorized and assigned a priority level.
5. A support team is automatically assigned.
6. A support ticket is generated and stored in the database.
7. Admin can manage and update ticket status through the dashboard.
8. Users can track their complaints and monitor resolution progress.

---

## Machine Learning Model

The system uses the following machine learning techniques:

* **TF-IDF Vectorization** to convert complaint text into numerical features.
* **Multinomial Naive Bayes Classifier** to classify complaints into categories.

This allows the chatbot to automatically understand the nature of the complaint and route it to the appropriate support team.

---

## Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/Complaint-Management-System.git
```

### Step 2: Navigate to Project Folder

```bash
cd Complaint-Management-System
```

### Step 3: Install Dependencies

```bash
pip install flask scikit-learn
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

```
http://127.0.0.1:5000
```

---

## Future Improvements

* Sentiment analysis for smarter priority detection
* Automated complaint escalation after time threshold
* Email or SMS notifications for ticket updates
* Graphical analytics dashboard
* Integration with real customer support systems

---

## Author

**Srija Kandimalla**
