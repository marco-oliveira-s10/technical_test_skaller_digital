import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client

def test_send_email(client):
    response = client.post('/email/send-email', headers={"Content-Type": "application/json"}, json={
        "to": "marco.oliveira.s10@gmail.com",
        "subject": "Service in Python",
        "body": "Hello, this is an email triggered by a service in Python, thanks!"
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['message'] == 'Email sent successfully'

def test_send_email_with_invalid_email(client):
    response = client.post('/email/send-email', headers={"Content-Type": "application/json"}, json={
        "to": "invalid-email",
        "subject": "Service in Python",
        "body": "Hello, this is an email triggered by a service in Python, thanks!"
    })
    json_data = response.get_json()
    assert response.status_code == 400
    assert json_data['error'] == 'Invalid email address'

def test_send_email_without_required_fields(client):
    response = client.post('/email/send-email', headers={"Content-Type": "application/json"}, json={
        "to": "marco.oliveira.s10@gmail.com",
        # Missing 'subject' and 'body'
    })
    json_data = response.get_json()
    assert response.status_code == 400
    assert json_data['error'] == 'Missing required fields'

def test_send_email_with_empty_subject(client):
    response = client.post('/email/send-email', headers={"Content-Type": "application/json"}, json={
        "to": "marco.oliveira.s10@gmail.com",
        "subject": "",
        "body": "Hello, this is an email triggered by a service in Python, thanks!"
    })
    json_data = response.get_json()
    assert response.status_code == 400
    assert json_data['error'] == 'Missing required fields'

def test_send_email_with_empty_body(client):
    response = client.post('/email/send-email', headers={"Content-Type": "application/json"}, json={
        "to": "marco.oliveira.s10@gmail.com",
        "subject": "Service in Python",
        "body": ""
    })
    json_data = response.get_json()
    assert response.status_code == 400
    assert json_data['error'] == 'Missing required fields'
