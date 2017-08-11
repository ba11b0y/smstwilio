from twilio.rest import TwilioRestClient
accountSid='your account sid here'
authToken='your auth token here'
twilioClient=TwilioRestClient(accountSid,authToken)
sender_twil='number obtained from twilio'
receiver_twil='number to send the message to'
myMessage=twilioClient.messages.create(body="Message Body",from_=sender_twil,to=receiver_twil)
