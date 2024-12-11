# Student Vote Portal

This is a simple Flask-based Student Voting Portal for the University of Nairobi (UoN). The portal allows users to log in with a username and password, and login attempts are sent via email to the administrator. The project includes authentication, sending email notifications, and more.

## Features
- Login functionality with hardcoded credentials.
- Email notification on login attempts.
- User-friendly UI with responsive design.

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python 3 or later
- A Gmail account for sending emails via Flask-Mail
- Virtual environment (optional but recommended)

### Step 1: Clone the Repository and Set Up Virtual Environment

Clone the repository to your local machine:

```bash
git clone https://github.com/KenyanAudo03/StudentVotePortal.git
cd StudentVotePortal

# On Window
python -m venv venv
.\venv\Scripts\activate

# On Linux/Mac Os
python3 -m venv venv
source venv/bin/activate
```
### Step 3: Install Dependencies
```bash 
pip install -r requirements.txt
```

### Step 4: Set Up Gmail for Sending Emails

To send login attempt emails, you'll need a Gmail account and enable **Less Secure App Access**. Follow these steps:

1. **Create a Gmail account** (if you don't have one already).

2. **Enable Less Secure Apps**:
   - Visit [Google Account Settings](https://myaccount.google.com/security).
   - Turn on **"Less secure app access"** (You might need to enable two-factor authentication to do this).

   **Note**: Google recommends using OAuth 2.0 for production applications. However, for simplicity, this example uses less secure apps for development purposes.

3. **Create a `.env` File**:  
   Create a `.env` file in the root of the project with your Gmail credentials:

   ```plaintext
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-email-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   ```


### Step 5: Run the Application

Once you have set up the environment and installed the dependencies, you can run the Flask application:

```bash
python app.py
```

This will start the Flask development server. By default, the app will be available at http://localhost:5000.


### Step 6: Test the Application

Visit [http://localhost:5000](http://localhost:5000) in your browser and try logging in with any credentials of your choice:

- **Username**: (Your choice)
- **Password**: (Your choice)

### Troubleshooting

#### If you encounter issues with Gmail email sending, ensure you have enabled Less Secure App Access.

#### If you get errors with dependencies or Flask-Mail, ensure that the virtual environment is activated and all dependencies are correctly installed.
