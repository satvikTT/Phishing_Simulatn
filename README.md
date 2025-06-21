# Ethical Phishing Simulation Platform

## Overview
This Ethical Phishing Simulation Platform has been developed as an educational initiative to demonstrate the tactics commonly employed in phishing attacks and to cultivate user awareness on how to recognize and effectively avoid such threats. By simulating realistic phishing scenarios in a controlled and safe environment, this project aims to equip individuals with practical knowledge and best practices to safeguard their personal information and enhance overall cybersecurity hygiene.

## Features
- Realistic fake login page styled like Microsoft Outlook
- Flask server that captures submitted credentials (for demonstration only)
- Python script to send phishing-like emails with a link to the fake login
- Ngrok tunnel for testing on external devices
- Secure logging to `logs.txt` for analysis
- For educational demonstration / purposes only

## Tech Stack
- **Programming Language:** Python
- **Backend:** Flask
- **Frontend:** HTML/CSS
- **Email Sending:** Python `smtplib` with Gmail SMTP server
- **Exposure:** Ngrok for tunneling
- **Logging:** Plain text file

## Project Structure
phishing_simulatn/
|---app.py
|---send_email.py
|---templates/
|-|---outlook_modern.html
|---static/
|-|---css/
|-|-|---modern.css
|---logs.txt
|---report_proj.pdf
|---ngrok.exe

## Pre-Requisite
- Python (above 3.0 version)
- PIP (python package manager)
- Ngrok
- Code Editor (VS Code)
  
## How to use:
### Clone the repository
```bash
git clone https://github.com/satvikTT/Phishing_Simulatn.git
cd Phishing_Simulatn
```
### Install Dependencies
- Flask
```bash
pip install Flask
```
- Ngrok
```bash
https://ngrok.com/downloads/windows?tab=download
```

## Working
1. Designed the Login Interface:
   Created a realistic login page using custom HTML and CSS to mimic a genuine sign-in form, enhancing the authenticity of the simulation.
2. Developed the Backend Application:
   Implemented `app.py` using the Flask framework to serve the login page and handle form submissions securely.
3. Integrated Frontend with Backend:
   Configured Flask to render the HTML template and capture user input data when credentials are submitted through the form.
4. 
