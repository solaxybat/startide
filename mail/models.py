from django.db import models
from evennia.locks.lockhandler import LockHandler
from evennia.utils.utils import lazy_property


# Create your models here.
class Mail(models.Model):
    MAIL_STATUSES = (
        ('U', 'Unread'),
        ('R', 'Read'),
        ('F', 'Forwarded'),
        ('R', 'Replied')
    )
    subject = models.CharField(max_length=50)
    message = models.TextField()
    status = models.CharField(max_length=1, choices=MAIL_STATUSES)
    sent_by = models.ManyToManyField("objects.ObjectDB")
    receivers = models.ManyToManyField("objects.ObjectDB")
    date_sent = models.DateTimeField()
    lock_storage = models.TextField()

    @lazy_property
    def locks(self):
        return LockHandler(self)