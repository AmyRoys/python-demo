# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC47f03b5c651d278dc845884293d82699'
auth_token = 'a0517bdeed37aae059bd16ec9114c8d6'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='https://www.youtube.com/watch?v=ECuum1kb8Q4',
    from_='whatsapp:+14155238886',
    to='whatsapp:+353874036213'
)

print(message.sid)
