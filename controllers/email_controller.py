# controllers/email_controller.py
from services.email_service import send_email as send_email_service

def send_email(to, subject, body):
    return send_email_service(to, subject, body)
