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
```
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
```

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
4. Configured Ngrok for Public Access:
   Downloaded and placed Ngrok in the project directory to create a secure tunnel, allowing the local Flask server to be accessed from external devices over the internet.
5. Generated a Public URL:
   Opened the command prompt within the project folder and executed Ngrok to forward the local server port (5000), resulting in a unique, publicly accessible URL.
   ```bash
   ngrok http 5000
   ```
6. Linked the Public URL in the Email Script:
   Copied the Ngrok-generated link and updated it within send_email.py so that the phishing simulation email directs recipients to the hosted fake login page.
7. Dispatched the Simulation Email:
   Executed send_email.py to send an awareness demonstration email to a specified recipient, containing the Ngrok link to the simulated phishing page.
   ```bash
   python send_email.py
   ```
8. Ran the Flask Application:
   Started the Flask server by running app.py, ensuring that the fake login page is live and ready to receive submissions from users who access the link.
   ```bash
   python app.py
   ```
9. Captured User Input:
    When a recipient visits the page and enters credentials, the data is securely logged in a file named logs.txt for later review and analysis.
10. Reviewed Collected Data:
    Examined logs.txt to analyze the submitted dummy credentials, demonstrating how phishing attacks can collect sensitive information and highlighting the importance of user awareness.

## Disclaimer
This project is strictly for educational and awareness purposes. Do not use it to collect real user credentials. Use responsibly and ethically.

## Enclosures
- **_app.py:_** Flask application that serves the fake login page and captures submitted credentials for demonstration purposes.
- **_send_email.py:_** Python script to send a phishing simulation email containing the Ngrok public link to the fake login page.
- **_outlook_modern.html:_** HTML template that mimics a realistic Microsoft Outlook login page used in the simulation.
- **_modern.css:_** CSS file that styles the fake login page to closely resemble the authentic Outlook interface.
- **_report_proj.pdf:_** The final project report outlining objectives, tools used, workflow steps, and conclusions drawn from the simulation.

## Conclusion
This project illustrates how phishing tactics can be ethically replicated within a controlled environment to enhance user awareness and resilience against online deception. By integrating a realistic login interface, a robust Flask backend, secure Ngrok tunneling, and an automated email dispatch system, the simulation effectively demonstrates how unsuspecting users can be manipulated into revealing sensitive credentials. This exercise underscores the critical role of continuous cybersecurity education and proactive vigilance in safeguarding personal and organizational data against social engineering threats.

## Author
  Name: Satvik Bhagat
  Contact: satvikbhagat2705@gmail.com
