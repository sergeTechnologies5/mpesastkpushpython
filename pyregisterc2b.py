
import requests
from requests.auth import HTTPBasicAuth
import json

consumer_key = "jJMVK098pTNas1GdmiEUGwVARaI5zOs3"
consumer_secret = "LMmzbd6qzELQfR5f"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
print("token request")
print (r.text)
access_token = json.loads(r.text)["access_token"]
print("url registration")
# url registration
api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
headers = {"Authorization": "Bearer %s" % access_token}
request = { "ShortCode": "601426",
    "ResponseType": "Completed",
    "ConfirmationURL": "https://e07f93d4.ngrok.io/pesa/b2c/v1",
    "ValidationURL": "https://e07f93d4.ngrok.io/pesa/b2c/v1"}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)

# c2b
print("c2b")
api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
headers = {"Authorization": "Bearer %s" % access_token
,"Content-Type":"application/json"}
request = {
    "ShortCode": "601426",
    "CommandID": "CustomerPayBillOnline",
    "Amount": "100",
    "Msisdn": "254708374149",
    "BillRefNumber": "account"
}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)

print("b2c")
# b2c
api_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
headers = { "Authorization": "Bearer %s" % access_token }
request = {
    "InitiatorName": "apiop33",
    "SecurityCredential": "lqymkVEGSbqTIFT40E8aN46Rtm+0vtW0VDLIgIKiYd/xwaQz5PE1EEnmg6UgL5KNb+yc2uSLULvWczdzpCIL5LNVMCiRimxn3l5O/W6jLx/+Lp5caM+9+D0NDiVAEcc/2gZXSsVaAUq8y89xNh7gmxTkVMxEIJcP8oSpzRb6ja3oESBtKIOzS0uT2BruoEl6SwXRiBdu5IBfxDCMsy1wLcPEg3u2RqZ9orw26LmjDsx6FZVrBSYq3+9QUjdL/GMnrl+GDEM2cJwTB89eLj1MclcRYhxwnov+Yz9XXDCnNIOQJBKaL6woA/+lwqEaqkFSBhfk46j2yuO9DBEHPM8u/A==",
    "CommandID": "BusinessPayment",
    "Amount": "1000",
    "PartyA": "601426",
    "PartyB": "254702261679",
    "Remarks": "please",
    "QueueTimeOutURL": "https://e07f93d4.ngrok.io/pesa/b2c/v1" ,
    "ResultURL": "https://e07f93d4.ngrok.io/pesa/b2c/v1",
    "Occassion":  "work"
}
response = requests.post(api_url, json = request, headers=headers)

print (response.text)


print("b2b")
# b2b
api_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
headers = { "Authorization": "Bearer %s" % access_token }
request = {
	"InitiatorName": "apitest361",
	"SecurityCredential": "TEMBbsVFFP/cyXCnM6UiGZKCHeK6p8PSLv6BUVjObJfIpOZPKQm5/WWICTwASZW3o0vrHfSwPblTGAtZ6NynmKbSC7ZPHDbLFy62i7QrFDvhsR9ZfNXAHS/zODNxvuxKIA0MybYmF6MdtcIzsvRzvAEAD/bxdezPy+anYQVZF7RAzGOFp2FpFh9EpAzbEWFFWuLS4BwiF00VP4KkbeEj7tYoqQVRtyF4yFhDknX9LW3UyskblgXZd3k0ALRuEmTTxEgZhaQOFeSURlTU2uIqADuGH4ixNskhINEon3fMOos0X9uxyWitfwhqpnrM9Rosj9j/4FR4XOz/oN6PsKrlCw==",
	"CommandID": "BusinessPayment",
	"SenderIdentifierType": "4",
	"RecieverIdentifierType": "4",
	"Amount": "1000",
	"PartyA": "601426",
	"PartyB": "254708374149",
	"AccountReference": "ref",
	"Remarks": "please",
	"QueueTimeOutURL": "https://e07f93d4.ngrok.io/pesa/b2b/v1" ,
	"ResultURL": "https://e07f93d4.ngrok.io/pesa/b2b/v1"
}
response = requests.post(api_url, json = request, headers=headers)

print (response.text)

print("Lipa na mpesa stkpush")

api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token }

import datetime
from base64 import b64encode
timestamp = str(datetime.datetime.now()).split(".")[0].replace("-", "").replace(" ", "").replace(":", "")
business_short_code = "174379"
pass_key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
password = "{}{}{}".format(business_short_code,pass_key,str(timestamp))
data_bytes = password.encode("utf-8")
#password encoding base64 
password = b64encode(data_bytes)
# hustle to change password and timestamp
password = password.decode("utf-8")

request = {
	"BusinessShortCode": business_short_code,
	"Password": password,
	"Timestamp": timestamp,
	"TransactionType": "CustomerPayBillOnline",
	"Amount": "1000",
	"PartyA": "254708374149",
	"PartyB": "174379",
	"PhoneNumber": "254702261679",
	"CallBackURL": "https://e07f93d4.ngrok.io/pesa/b2c/v1",
	"AccountReference": "account",
	"TransactionDesc": "test" ,
}
response = requests.post(api_url, json = request, headers=headers)

print (response.text)

# account balance
print("Balance ")
api_url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
headers = {"Authorization": "Bearer %s" % access_token}
request = { 
    "Initiator":"apitest361",
    "SecurityCredential":"TEMBbsVFFP/cyXCnM6UiGZKCHeK6p8PSLv6BUVjObJfIpOZPKQm5/WWICTwASZW3o0vrHfSwPblTGAtZ6NynmKbSC7ZPHDbLFy62i7QrFDvhsR9ZfNXAHS/zODNxvuxKIA0MybYmF6MdtcIzsvRzvAEAD/bxdezPy+anYQVZF7RAzGOFp2FpFh9EpAzbEWFFWuLS4BwiF00VP4KkbeEj7tYoqQVRtyF4yFhDknX9LW3UyskblgXZd3k0ALRuEmTTxEgZhaQOFeSURlTU2uIqADuGH4ixNskhINEon3fMOos0X9uxyWitfwhqpnrM9Rosj9j/4FR4XOz/oN6PsKrlCw==",
    "CommandID":"AccountBalance",
    "PartyA":"174379",
    "IdentifierType":"4",
    "Remarks":"Remarks",
    "QueueTimeOutURL":"https://e07f93d4.ngrok.io/pesa/b2c/v1",
    "ResultURL":"https://e07f93d4.ngrok.io/pesa/b2c/v1"
    }

response = requests.post(api_url, json = request, headers=headers)

print (response.text)

# transaction status
print("transaction status")
api_url = "https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query"
headers = { "Authorization": "Bearer %s" % access_token }
request = {
  "Initiator":"apitest361",
  "SecurityCredential":"TEMBbsVFFP/cyXCnM6UiGZKCHeK6p8PSLv6BUVjObJfIpOZPKQm5/WWICTwASZW3o0vrHfSwPblTGAtZ6NynmKbSC7ZPHDbLFy62i7QrFDvhsR9ZfNXAHS/zODNxvuxKIA0MybYmF6MdtcIzsvRzvAEAD/bxdezPy+anYQVZF7RAzGOFp2FpFh9EpAzbEWFFWuLS4BwiF00VP4KkbeEj7tYoqQVRtyF4yFhDknX9LW3UyskblgXZd3k0ALRuEmTTxEgZhaQOFeSURlTU2uIqADuGH4ixNskhINEon3fMOos0X9uxyWitfwhqpnrM9Rosj9j/4FR4XOz/oN6PsKrlCw==",
  "CommandID":"TransactionStatusQuery",
  "TransactionID":"dadfsasf",
  "PartyA":"174379",
  "IdentifierType":"1",
  "ResultURL":"https://e07f93d4.ngrok.io/pesa/b2c/v1",
  "QueueTimeOutURL":"https://e07f93d4.ngrok.io/pesa/b2c/v1",
  "Remarks":"please",
  "Occasion":"work"
}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)
# reversal transation
print("transaction reversal")
api_url = "https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request"
headers = {"Authorization": "Bearer %s" % access_token}
request ={
	"Initiator":"apitest361",
	"SecurityCredential":"TEMBbsVFFP/cyXCnM6UiGZKCHeK6p8PSLv6BUVjObJfIpOZPKQm5/WWICTwASZW3o0vrHfSwPblTGAtZ6NynmKbSC7ZPHDbLFy62i7QrFDvhsR9ZfNXAHS/zODNxvuxKIA0MybYmF6MdtcIzsvRzvAEAD/bxdezPy+anYQVZF7RAzGOFp2FpFh9EpAzbEWFFWuLS4BwiF00VP4KkbeEj7tYoqQVRtyF4yFhDknX9LW3UyskblgXZd3k0ALRuEmTTxEgZhaQOFeSURlTU2uIqADuGH4ixNskhINEon3fMOos0X9uxyWitfwhqpnrM9Rosj9j/4FR4XOz/oN6PsKrlCw==",
	"CommandID":"TransactionReversal",
	"TransactionID":"dadfsasf",
	"Amount":"10",
	"ReceiverParty":"601426",
	"RecieverIdentifierType":"4",
	"ResultURL":"https://e07f93d4.ngrok.io/pesa/b2c/v1",
	"QueueTimeOutURL":"https://e07f93d4.ngrok.io/pesa/b2c/v1",
	"Remarks":"please",
	"Occasion":"work"
}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)