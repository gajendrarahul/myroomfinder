from django.db import models
from account.models import Account

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50,blank=False, null=True, default=None)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    account = models.OneToOneField(Account, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name

class Room(models.Model):
    number_of_room = models.IntegerField()
    description = models.CharField(max_length=1000)
    image = models.ImageField(null=True,blank=True, upload_to='images/')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.owner.name
