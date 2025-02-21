from django.db import models

class ObserverType(models.TextChoices):
    ACCOUNTING = 'AC', 'Accounting'
    TREASURY = 'TR', 'Treasury'
    AUDIT_LOG = 'AL', 'Audit Log'
    EMAIL_NOTIFICATION = 'EN', 'Email Notification'