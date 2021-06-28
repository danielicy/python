from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)
response = client.messages.create(
    to="***",
    from_=config.source_phone,
    body="my test")

print(response)
