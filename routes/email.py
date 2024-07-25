from flask_restx import Namespace, Resource, fields
from flask import request
from email_validator import validate_email, EmailNotValidError
from controllers.email_controller import send_email

email_ns = Namespace('Email operations', description='Operations related to email sending')

email_model = email_ns.model('Email', {
    'to': fields.String(required=True, description='Email address of the recipient'),
    'subject': fields.String(required=True, description='Subject of the email'),
    'body': fields.String(required=True, description='Body of the email')
})

@email_ns.route('/send-email')
class SendEmail(Resource):
    @email_ns.doc('send_email')
    @email_ns.expect(email_model)
    def post(self):
        data = request.get_json()
        to = data.get('to')
        subject = data.get('subject')
        body = data.get('body')
        
        if not to or not subject or not body:
            return {'error': 'Missing required fields'}, 400

        # Validação do e-mail
        try:
            validate_email(to)
        except EmailNotValidError as e:
            return {'error': 'Invalid email address'}, 400
        
        success, message = send_email(to, subject, body)
        
        if success:
            return {'message': 'Email sent successfully'}, 200
        else:
            return {'error': message}, 500
