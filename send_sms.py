import africastalking

# TODO: Initialize Africa's Talking

africastalking.initialize(
    username='kariukiHarry',
    api_key='8f571fbd15404f8ce19bae31b2f530c0c5a730b7abe002ef980353d0580c2ac2'
)

sms = africastalking.SMS

class send_sms():

    def send(self):
        
        #TODO: Send message
        def sending(self):
            # Set the numbers in international format
            recipients = ["+254700725236"]
            # Set your message
            message = "fgcvhbnm";
            # Set your shortCode or senderId
            sender = "Wasafi"
            try:
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Houston, we have a problem: {e}')
        pass #delete this code
