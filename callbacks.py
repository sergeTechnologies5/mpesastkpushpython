
'''[POST] https://yourdomain.co.ke/your/validation/url

// HEADERS
Content-Type: application/json

// BODY
{
    "TransactionType": "",
    "TransID": "LHG31AA5TX",
    "TransTime": "20170816190243",
    "TransAmount": "200.00",
    "BusinessShortCode": "601426",
    "BillRefNumber": "account",
    "InvoiceNumber": "",
    "OrgAccountBalance": "",
    "ThirdPartyTransID": "",
    "MSISDN": "254708374149",
    "FirstName": "John",
    "MiddleName": "",
    "LastName": "Doe"
}'''



# this is the call back response data from mpesa after a stk push initialization

'''{
	"Body": 
	{
		"stkCallback": 
		{
			"MerchantRequestID": "21605-295434-4",
			"CheckoutRequestID": "ws_CO_04112017184930742",
			"ResultCode": 0,
			"ResultDesc": "The service request is processed successfully.",
			"CallbackMetadata": 
			{
				"Item": 
				[
					{
						"Name": "Amount",
						"Value": 1
					},
					{
						"Name": "MpesaReceiptNumber",
						"Value": "LK451H35OP"
					},
					{
						"Name": "Balance"
					},
					{
						"Name": "TransactionDate",
						"Value": 20171104184944
					},
					{
						"Name": "PhoneNumber",
						"Value": 254727894083
					}
				]
			}
		}
	}
}'''

# b2c result response ftom callback
'''{
	"Result":
	{
		"ResultType":0,
		"ResultCode":0,
		"ResultDesc":"The service request has been accepted successfully.",
		"OriginatorConversationID":"14593-80515-2",
		"ConversationID":"AG_20170821_000049448b24712383de",
		"TransactionID":"LHL41AHJ6G",
		"ResultParameters":
		{
			"ResultParameter":
			[
				{
					"Key":"TransactionAmount",
					"Value":100
				},
				{
					"Key":"TransactionReceipt",
					"Value":"LHL41AHJ6G"
				},
				{
					"Key":"B2CRecipientIsRegisteredCustomer",
					"Value":"Y"
				},
				{
					"Key":"B2CChargesPaidAccountAvailableFunds",
					"Value":0.00
				},
				{
					"Key":"ReceiverPartyPublicName",
					"Value":"254708374149 - John Doe"
				},
				{
					"Key":"TransactionCompletedDateTime",
					"Value":"21.08.2017 12:01:59"
				},
				{
					"Key":"B2CUtilityAccountAvailableFunds",
					"Value":98834.00
				},
				{
					"Key":"B2CWorkingAccountAvailableFunds",
					"Value":100000.00
				}
			]
		},
		"ReferenceData":
		{
			"ReferenceItem":
			{
				"Key":"QueueTimeoutURL",
				"Value":"https:\/\/internalsandbox.safaricom.co.ke\/mpesa\/b2cresults\/v1\/submit"
			}
		}
	}
}'''

# b2b

'''{
    "Result":
    {
        "ResultType":0,
        "ResultCode":0,
        "ResultDesc":"The service request has been accepted successfully.",
        "OriginatorConversationID":"8551-61996-3",
        "ConversationID":"AG_20170727_00006baee344f4ce0796",
        "TransactionID":"LGR519G2QV",
        "ResultParameters":
        {
            "ResultParameter":
            [
                {
                    "Key":"InitiatorAccountCurrentBalance",
                    "Value":"{ Amount={BasicAmount=46713.00, MinimumAmount=4671300, CurrencyCode=KES
                    }}"
                },
                {
                    "Key":"DebitAccountCurrentBalance",
                    "Value":"{Amount={BasicAmount=46713.00, MinimumAmount=4671300, CurrencyCode=KES}}"
                },
                {
                    "Key":"Amount",
                    "Value":10
                },
                {
                    "Key":"DebitPartyAffectedAccountBalance",
                    "Value":"Working Account|KES|46713.00|46713.00|0.00|0.00"
                },
                {
                    "Key":"TransCompletedTime",
                    "Value":20170727102524
                },
                {
                    "Key":"DebitPartyCharges",
                    "Value":"Business Pay Bill Charge|KES|77.00"
                },
                {
                    "Key":"ReceiverPartyPublicName",
                    "Value":"603094 - Safaricom3117"
                },
                {
                    "Key":"Currency",
                    "Value":"KES"
                }
            ]
        },
        "ReferenceData":
        {
            "ReferenceItem":
            [
                {
                    "Key":"BillReferenceNumber",
                    "Value":"aaa"
                },
                {
                    "Key":"QueueTimeoutURL",
                    "Value":"https://internalsandbox.safaricom.co.ke/mpesa/b2bresults/v1/submit"
                }
            ]
        }
    }
}'''

# reversal callback data
'''{
	"Result":
	{
		"ResultType":0,
		"ResultCode":0,
		"ResultDesc":"The service request has been accepted successfully.",
		"OriginatorConversationID":"10819-695089-1",
		"ConversationID":"AG_20170727_00004efadacd98a01d15",
		"TransactionID":"LGR019G3J2",
		"ReferenceData":
		{
			"ReferenceItem":
			{
				"Key":"QueueTimeoutURL",
				"Value":"https://internalsandbox.safaricom.co.ke/mpesa/reversalresults/v1/submit"
			}
		}
	}
}'''

# import the Flask Framework
from flask import Flask,jsonify, make_response, request

app = Flask(__name__)

# Create the context (endpoint/URL) which will be triggered when the request
# hits the above specified port. This will resolve to a URL like
# 'http://address:port/context'. E.g. the context below would
# resolve to 'http://127.0.0.1:80/mpesa/b2c/v1' on the local computer. Then
# the Handler will handle the request received via the given URL.

# You may create a separate URL for every endpoint you need

@app.route('/pesa/b2c/v1', methods = ["POST"])
def listenB2c():
    #save the data
    request_data = request.data

    #Perform your processing here e.g. print it out...
    print(request_data)

    # Prepare the response, assuming no errors have occurred. Any response
    # other than a 0 (zero) for the 'ResultCode' during Validation only means
    # an error occurred and the transaction is cancelled
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
    };

    # Send the response back to the server
    return jsonify({'message': message}), 200

# Change this part to reflect the API you are testing
@app.route('/pesa/b2b/v1', methods = ["POST"])
def listenB2b():
    request_data = request.data
    print(request_data)
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
    };

    return jsonify({'message': message}), 200

if __name__ == '__main__':
    app.run(debug=True)
