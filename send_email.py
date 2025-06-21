import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 🔹 Ask user for recipient email
recipient_email = input("Enter recipient Gmail address: ")

# 🔹 Ask user for project link
project_link = input("Enter your connection (URL): ")

# --- Create the awareness demonstration email ---
msg = MIMEMultipart("alternative")

msg['Subject'] = "Security Awareness Project - Safe Login Demonstration"
msg['From'] = "bhagatjisatvik@gmail.com"
msg['To'] = recipient_email  # dynamically set recipient

# Plain text version
text = f"""\
Hello,

This email is part of an academic project on secure login awareness.

Please help by visiting the link below and entering sample (fake) credentials — this will only be used to demonstrate how phishing can work and how to protect against it.

Project Link: {project_link}

Your participation is greatly appreciated for educational purposes only.

Thank you!
"""

# HTML version
html = f"""\
<html>
  <body>
    <p>Hello,<br><br>
       This email is part of an academic project demonstrating secure login awareness.<br>
       Please <a href="{project_link}">click here</a> and enter sample (fake) credentials.<br>
       This is strictly for study purposes to show how phishing attempts can be made and detected.<br><br>
       Your participation helps this educational project.<br><br>
       Thank you!
    </p>
  </body>
</html>
"""

# Attach both plain and HTML parts
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
msg.attach(part1)
msg.attach(part2)

# --- Connect to Gmail SMTP securely ---
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# ✅ Use your real Gmail and App Password
server.login("bhagatjisatvik@gmail.com", "bztbqpzvrpdecndw")

# --- Send the email ---
server.send_message(msg)
print(f"Awareness project email sent successfully to {recipient_email}!")

server.quit()
