# Job Application Automation

An automated email system for sending job applications to recruiters with personalized messages and resume attachments.

## 📋 Overview

This Python application automates the process of sending job application emails to multiple recruiters. It reads recruiter information from a CSV file and sends personalized emails with your resume attached to each recruiter based on specified conditions.

## ✨ Features

- **Bulk Email Sending**: Send personalized emails to multiple recruiters at once
- **CSV-Based Management**: Manage recruiter contacts through a simple CSV file
- **Conditional Sending**: Control which recruiters receive emails using a condition flag
- **Resume Attachment**: Automatically attach your resume to each email
- **HTML Email Support**: Send formatted HTML emails with personalized content
- **Gmail Integration**: Uses Gmail SMTP for reliable email delivery
- **Progress Tracking**: Console output shows successful email deliveries

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Gmail account with App Password enabled
- Resume file in PDF format

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Job--application-automation-main
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Gmail App Password**
   - Enable 2-factor authentication on your Gmail account
   - Generate an App Password for this application
   - Replace the `app_pass` variable in `main.py` with your App Password

### Configuration

1. **Update Email Credentials**
   ```python
   sender_email = "your-email@gmail.com"  # Replace with your Gmail
   app_pass = "your-app-password"         # Replace with your App Password
   ```

2. **Add Your Resume**
   - Place your resume PDF in the `Attachments/` folder
   - Update the filename in `main.py` if different from "resume (2).pdf"

3. **Customize Email Content**
   - Modify the `subject` and `body` variables in `main.py`
   - Update contact information and personal details

## 📊 CSV File Format

The `Recruter_email.csv` file should contain the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| Name | Recruiter's name | John Smith |
| Gmail | Recruiter's email address | john.smith@company.com |
| ContactNumber | Phone number (optional) | +1234567890 |
| Linkedin | LinkedIn profile (optional) | linkedin.com/in/johnsmith |
| condition | Send email flag (TRUE/FALSE) | TRUE |

### Example CSV Content:
```csv
Name,Gmail,ContactNumber,Linkedin,condition
John Smith,john.smith@company.com,+1234567890,linkedin.com/in/johnsmith,TRUE
Jane Doe,jane.doe@techcorp.com,+0987654321,linkedin.com/in/janedoe,FALSE
```

## 🔧 Usage

1. **Prepare your data**
   - Update `Recruter_email.csv` with recruiter information
   - Set `condition` to `TRUE` for recruiters you want to email

2. **Run the application**
   ```bash
   python main.py
   ```

3. **Monitor progress**
   - The application will display the CSV data
   - Success messages will show for each email sent
   - Only recruiters with `condition=TRUE` will receive emails

## 📁 Project Structure

```
Job--application-automation-main/
├── main.py                 # Main application script
├── requirements.txt        # Python dependencies
├── Recruter_email.csv     # Recruiter contact database
├── .gitignore             # Git ignore rules
├── Attachments/           # Resume and attachment folder
│   └── resume (2).pdf     # Your resume file
└── README.md              # This file
```

## ⚙️ Dependencies

- **pandas (2.3.3)**: For CSV file handling and data manipulation
- **smtplib**: Built-in Python library for SMTP email sending
- **email**: Built-in Python library for email composition

## 🔒 Security Notes

- **Never commit your App Password**: Keep your Gmail App Password secure
- **Use App Passwords**: Don't use your regular Gmail password
- **Review Recipients**: Always verify the CSV file before running
- **Test First**: Send test emails to yourself before bulk sending

## 🛠️ Customization

### Email Template
Modify the email content in `main.py`:
```python
subject = "Your Custom Subject"
body = f"""
Your custom HTML email template here.
Use {row['Name']} for personalization.
"""
```

### Attachment Management
To change the resume file:
```python
filename = "Attachments/your-resume.pdf"
```

### Conditional Logic
Modify the condition check:
```python
if row["condition"] == True and row["ContactNumber"] != "":
    # Your custom conditions
```

## 🚨 Important Warnings

- **Gmail Limits**: Gmail has daily sending limits (500 emails/day for regular accounts)
- **Spam Prevention**: Don't send too many emails rapidly to avoid being flagged
- **Legal Compliance**: Ensure compliance with anti-spam laws in your jurisdiction
- **Professional Content**: Always maintain professional email content

## 🐛 Troubleshooting

### Common Issues

1. **Authentication Error**
   - Verify App Password is correct
   - Ensure 2FA is enabled on Gmail

2. **File Not Found Error**
   - Check resume file path and name
   - Ensure file exists in Attachments folder

3. **CSV Reading Error**
   - Verify CSV format and column names
   - Check for special characters in data

4. **SMTP Connection Error**
   - Check internet connection
   - Verify Gmail SMTP settings

## 📝 License

This project is for educational and personal use. Please ensure compliance with applicable laws and email service terms of use.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues or questions:
- Check the troubleshooting section
- Review Gmail App Password setup
- Verify CSV file format
- Test with a single recipient first

---

**Disclaimer**: This tool is for legitimate job application purposes only. Users are responsible for compliance with anti-spam laws and email service terms of use.
# LoanVsSIP
