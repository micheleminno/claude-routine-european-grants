"""
send_email.py
-------------
Sends the daily EU grants summary email via the Mailgun HTTP API.
Called by the Claude Code cloud routine at the end of each execution.

Uses Mailgun's HTTPS API (not SMTP) because the routine's execution
environment only permits outbound HTTPS traffic.

Required environment secrets:
    MAILGUN_API_KEY      — Mailgun private API key
    MAILGUN_DOMAIN        — Mailgun sending domain (e.g. mg.sara-system.com,
                             or the sandboxXXXX.mailgun.org domain on the free plan)

Optional environment secrets:
    MAILGUN_API_BASE_URL — defaults to https://api.mailgun.net/v3
                             (use https://api.eu.mailgun.net/v3 for EU-region domains)
    MAILGUN_FROM          — defaults to "European Grants Monitor <mailgun@MAILGUN_DOMAIN>"

Note: on Mailgun's free sandbox domain, only "Authorized Recipients" added in
the Mailgun dashboard can receive mail. Verify a custom domain to lift that
restriction.
"""

import base64
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import date


RECIPIENTS = [
    "michele.minno@sara-system.com",
    "luca.sbano@sara-systems.eu",
    "markus.kirkilionis@sara-systems.eu",
]


def send_email(subject: str, body_html: str, body_text: str = "") -> None:
    """
    Send an email via the Mailgun HTTP API using environment secrets.

    Args:
        subject:    Email subject line
        body_html:  HTML version of the email body
        body_text:  Plain text fallback (optional)
    """
    api_key = os.environ["MAILGUN_API_KEY"]
    domain = os.environ["MAILGUN_DOMAIN"]
    base_url = os.environ.get("MAILGUN_API_BASE_URL", "https://api.mailgun.net/v3")
    sender = os.environ.get("MAILGUN_FROM", f"European Grants Monitor <mailgun@{domain}>")

    data = {
        "from": sender,
        "to": RECIPIENTS,
        "subject": subject,
        "html": body_html,
    }
    if body_text:
        data["text"] = body_text

    encoded_body = urllib.parse.urlencode(data, doseq=True).encode("utf-8")
    request = urllib.request.Request(f"{base_url}/{domain}/messages", data=encoded_body)
    credentials = base64.b64encode(f"api:{api_key}".encode()).decode()
    request.add_header("Authorization", f"Basic {credentials}")

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Mailgun API error {e.code}: {e.read().decode()}") from e

    print(f"Email sent successfully to: {', '.join(RECIPIENTS)} (Mailgun id: {result.get('id')})")


def build_subject() -> str:
    today = date.today().strftime("%d %B %Y")
    return f"European AI/coding grants — update {today}"


if __name__ == "__main__":
    # Quick smoke test — sends a test email when run directly
    test_html = """
    <h2>Test email</h2>
    <p>This is a test message from the <strong>european-grants-monitor</strong> routine.</p>
    <p>If you received this, Mailgun is configured correctly.</p>
    """
    send_email(
        subject="[TEST] European grants monitor — Mailgun check",
        body_html=test_html,
        body_text="Test email from european-grants-monitor. Mailgun is configured correctly.",
    )
