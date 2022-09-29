# works with both python 2 and 3
from __future__ import print_function

import africastalking

class SMS:
    def __init__(self):
        self.username = "kariukiHarry"
        self.api_key = "8f571fbd15404f8ce19bae31b2f530c0c5a730b7abe002ef980353d0580c2ac2"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self,phoneNumber):
            # Set the numbers you want to send to in international format
            recipients = [phoneNumber]

            # Set your message
            message = "Thank you for your feedback. WasaFi appreciates your input";

            # Set your shortCode or senderId
            try:
				# Thats it, hit send and we'll take care of the rest.
                response = self.sms.send(message, recipients)
                print (response)
            except Exception as e:
                print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send("+254700725236")