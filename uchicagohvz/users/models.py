from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from localflavor.us.models import PhoneNumberField
from uchicagohvz.users.phone import CARRIERS

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	phone_number = PhoneNumberField(blank=True)
	phone_carrier = models.CharField(max_length=32, blank=True, choices=[(k, k) for k in sorted(CARRIERS.keys())])
	subscribe_death_notifications = models.BooleanField(default=False)
	subscribe_chatter_listhost = models.BooleanField(default=True)

	def __unicode__(self):
		return self.user.get_full_name()

	@models.permalink
	def get_absolute_url(self):
		return ("users|profile",)

def get_or_create_profile(sender, **kwargs):
	profile, created = Profile.objects.get_or_create(user=kwargs['instance'])
	if created:
		pass # do email signup here
models.signals.post_save.connect(get_or_create_profile, sender=get_user_model())

def sympa_update(sender, **kwargs):
	from uchicagohvz.users.tasks import do_sympa_update
	old_profile = Profile.objects.get(id=kwargs['instance'].id)
	new_profile = kwargs['instance']
	user = new_profile.user
	if (not old_profile.subscribe_chatter_listhost) and new_profile.subscribe_chatter_listhost:
		do_sympa_update.delay(user, 'hvz-chatter', True)
	elif old_profile.subscribe_chatter_listhost and (not new_profile.subscribe_chatter_listhost):
		do_sympa_update.delay(user, 'hvz-chatter', False)
models.signals.pre_save.connect(sympa_update, sender=Profile)
