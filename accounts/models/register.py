from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

	''' Demonstrate docstring for confirming that this table will store extra informations of user
	'''

	otp_password = models.CharField(max_length = 6, null = True, blank = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
	token_for_user = models.CharField(max_length = 100, null = True, blank = True)
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on = models.DateTimeField(auto_now = True)
	created_by = models.ForeignKey(User, models.CASCADE, null =True, blank =True, related_name = 'profile_create')
	updated_by = models.ForeignKey(User, models.CASCADE, null =True, blank =True, related_name = 'profile_update')
	active = models.BooleanField(default = False)

