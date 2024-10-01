# PYMAIL - A Python GUI Application for Sending Emails

PYMAIL is a Python-based graphical user interface (GUI) application that allows users to send emails using their Gmail accounts. The application is built using the Tkinter library for the GUI, with Python's `smtplib` module handling the email-sending process. This simple yet functional app is ideal for users looking to send quick emails from a custom interface without opening a browser or email client.

## Features
- **GUI Interface**: A sleek, user-friendly interface for inputting sender credentials, receiver email, and the email message.
- **Email Sending Functionality**: The app uses Gmail’s SMTP server to send emails securely.
- **Real-Time Feedback**: After successfully sending an email, the console prints a confirmation message ("Mail Sent").
- **Password Security**: Input field for the password is hidden using an asterisk (`*`) to provide privacy during entry.
- **Custom Graphics**: Includes an embedded image in the GUI for branding and design aesthetics.

## How It Works
1. Users input their Gmail credentials (email and password) in the designated fields.
2. Users provide the recipient’s email address and the message they wish to send.
3. Upon clicking "SUBMIT," the application uses Gmail's SMTP server to send the email.

## Prerequisites
- Python 3.x
- Tkinter library (comes with most Python installations)
- A valid Gmail account
- Less secure apps enabled in Gmail (since this project uses basic SMTP authentication)
  - [Enable Less Secure Apps in Gmail](https://myaccount.google.com/lesssecureapps)

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/pymail.git
    ```
2. Install the required dependencies:
    - For `Tkinter`, it comes pre-installed with Python, but if you're using Linux, you might need to install it:
    ```bash
    sudo apt-get install python3-tk
    ```

## Usage
1. Run the Python script:
    ```bash
    python pymail.py
    ```
2. Enter the following details:
   - Your Gmail ID and password.
   - The recipient’s email address.
   - The message you want to send.
3. Click on the "SUBMIT" button to send the email.

## Project Structure
pymail/
│
├── pymail.py          # Main Python file that contains the GUI and email-sending logic
├── by _ KRRITHEN.gif  # Image used in the GUI (optional, replace with your own)


## Security Warning
This project uses basic SMTP authentication with your Gmail credentials, which requires enabling less secure apps in your Google account. Be cautious while sharing your credentials or running the app in environments where security is a concern. It is recommended to use app-specific passwords or OAuth2 authentication for real-world applications.

## Future Improvements
- Implement OAuth2 for more secure email authentication.
- Add the ability to attach files to the email.
- Provide a better error-handling mechanism for failed login attempts or message delivery issues.
