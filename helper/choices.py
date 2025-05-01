from django.db.models import TextChoices

class StatusChoices(TextChoices):
    BACHELOR = 'bachelor', 'Bachelor'
    MASTER = 'master', 'Master'

class PaymentChoices(TextChoices):
    CASH = 'cash', 'Cash'
    BANK = 'bank', 'Bank'
    ONLINE = 'online', 'Online'

class UserTypeChoices(TextChoices):
    INDIVIDUAL = 'individual', 'Individual'
    LEGAL = 'legal', 'Legal'


