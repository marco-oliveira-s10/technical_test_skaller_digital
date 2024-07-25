# routes/email.py
from flask import Blueprint, request, jsonify
from controllers.email_controller import send_email

email_bp = Blueprint('email', __name__)

@email_bp.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.get_json()
    to = data.get('to')
    subject = data.get('subject')
    body = data.get('body')
    
    if not to or not subject or not body:
        return jsonify({'error': 'Missing required fields'}), 400
    
    success, message = send_email(to, subject, body)
    
    if success:
        return jsonify({'message': 'Email sent successfully'}), 200
    else:
        return jsonify({'error': message}), 500
