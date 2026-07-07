"""
send_email.py
-------------
Sends the daily EU grants summary email via IONOS SMTP.
Called by the Claude Code cloud routine at the end of each execution.

Required environment secrets:
    SMTP_HOST      — e.g. smtp.ionos.eu
    SMTP_PORT      — e.g. 465
    SMTP_USER      — e.g. michele.minno@sara-systems.com
    SMTP_PASSWORD  — IONOS account password
"""

import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date


RECIPIENTS = [
    "michele.minno@sara-system.com",
    "luca.sbano@sara-systems.eu",
    "markus.kirkilionis@sara-systems.eu",
]


def send_email(subject: str, body_html: str, body_text: str = "") -> None:
    """
    Send an email via IONOS SMTP using environment secrets.

    Args:
        subject:    Email subject line
        body_html:  HTML version of the email body
        body_text:  Plain text fallback (optional)
    """
    smtp_host = os.environ["SMTP_HOST"]
    smtp_port = int(os.environ["SMTP_PORT"])
    smtp_user = os.environ["SMTP_USER"]
    smtp_pass = os.environ["SMTP_PASSWORD"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = ", ".join(RECIPIENTS)

    if body_text:
        msg.attach(MIMEText(body_text, "plain"))
    msg.attach(MIMEText(body_html, "html"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as server:
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, RECIPIENTS, msg.as_string())
        print(f"Email sent successfully to: {', '.join(RECIPIENTS)}")


def build_subject() -> str:
    today = date.today().strftime("%d %B %Y")
    return f"European AI/coding grants — update {today}"


if __name__ == "__main__":
    # Quick smoke test — sends a test email when run directly
    test_html = """
    <h2>Test email</h2>
    <p>This is a test message from the <strong>european-grants-monitor</strong> routine.</p>
    <p>If you received this, SMTP is configured correctly.</p>
    """
    send_email(
        subject="[TEST] European grants monitor — SMTP check",
        body_html=test_html,
        body_text="Test email from european-grants-monitor. SMTP is configured correctly.",
    )
