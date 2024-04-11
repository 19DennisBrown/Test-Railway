from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    description = models.TextField(blank=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    kra_pin = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    net_income = models.IntegerField( blank=True, null=True)
    age = models.IntegerField( blank=True, null=True)
    loan_amount = models.IntegerField( blank=True, null=True)
    id_no = models.IntegerField( blank=True, null=True)
    def __str__(self):
        return self.user.username


class ProfileStatus(models.Model):
  profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  status = models.BooleanField(null=True, default=None)
  def __str__(self):
        return f" Accept or Reject loan request by {self.profile.user}"