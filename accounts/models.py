from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
	
	def create_user(self, first_name, last_name, username, email, address, password=None):
		if not email:
			raise ValueError("You must provide an email address")
		if not address:
			raise ValueError("You must provide an address to ship to")
		user = self.model(
			email = self.normalize_email(email), 
			username = username,
			address =  address, 
			password = password,
			
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, first_name, last_name, username, email, address, password):
		user = self.create_user(
			first_name = first_name,
			last_name = last_name,
			username = username,
			email = self.normalize_email(email),
			address = address,
			password = password,
		)

		user.is_staff = True
		user.is_admin = True
		user.is_superuser = True
		user.is_active = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):

	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	username = models.CharField(max_length=32, null=True, unique=True, verbose_name="username" )
	email = models.EmailField(max_length=64, null=True, unique=True, verbose_name = "email address")	
	address = models.CharField(max_length=64, null=True, unique=True)
	
	# Required
	date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date joined')
	last_login = models.DateTimeField(auto_now=True, verbose_name='last login')
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'address',]
	objects = AccountManager()

	def __str__(self):
		return self.email + self.username

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True 

