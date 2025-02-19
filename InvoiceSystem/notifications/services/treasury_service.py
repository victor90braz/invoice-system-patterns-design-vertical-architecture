from notifications.strategies.email_notification import EmailNotification
from notifications.strategies.sms_notification import SMSNotification

class TreasuryService:
    def __init__(self, notification_strategy=None):
        self.notification_strategies = {
            'email': EmailNotification(),
            'sms': SMSNotification()
        }
        
       
        self.notification_strategy = self.notification_strategies.get(notification_strategy, EmailNotification())
    
    def notify(self, invoice):
        
        self.notification_strategy.notify(invoice)
