from model import predict_category, predict_priority, assign_team


def chatbot_response(message):

    # Predict complaint details using ML model
    category = predict_category(message)
    priority = predict_priority(message)
    team = assign_team(category)


    # Base response
    reply = f"""
This appears to be a {category} related issue.

✅ Ticket created successfully!

📂 Category: {category}
⚡ Priority: {priority}
👨‍💻 Assigned Team: {team}

"""


    # Escalation logic for high priority complaints
    if priority == "High":

        reply += """
⚠ This complaint has been marked as HIGH priority.

Your issue has been automatically escalated to the senior support team for faster resolution.
"""


    # Final response message
    reply += """

Our support team will review your complaint shortly.

You can track the status using the ticket ID in the dashboard.
"""


    return category, priority, team, reply