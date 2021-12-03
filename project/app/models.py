from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save, pre_save


# Create your models here.

# class User(AbstractUser):
#     pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    def __str__(self):
        return str(self.user)



class Committee(models.Model):
    committee_creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    committee_name = models.CharField(max_length=100)
    committee_members_limit = models.IntegerField()
    committee_amount_per_month = models.IntegerField(default=0)
    committee_month_period = models.IntegerField(default=0)
    committee_amount_limit = models.IntegerField(null=True)
    committee_starting_date = models.DateTimeField(auto_now_add=False)



    committee_ending_date = models.DateTimeField(auto_now_add=False)
    class Meta:
        verbose_name = 'Committee'
        verbose_name_plural = 'Committees'

    def __str__(self):
        return str(self.committee_name) 

class Participants(models.Model):
    participants_name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    participants_committee_name = models.ForeignKey(Committee, on_delete=models.CASCADE)
    participants_paid_status = models.BooleanField(default=False)
    participants_amount_paid = models.IntegerField()
    participants_payment_slip = models.ImageField(upload_to='images/', null=True, blank=True)
    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'

    def __str__(self):
        return str(self.participants_name) 

    

def post_user_created_signal(sender, instance,created, **kwargs ):
    print(instance,created)
    if created:
        Profile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender= User)