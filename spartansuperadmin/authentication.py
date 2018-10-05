from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from spartansuperadmin import settings

class SettingsBackend(object):

    ADMIN_LOGIN = 'superadmin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$36000$JaKRg6BKEHml$KhtzmD8N2N490Gi22Nr9Bv9HT1SH3YBT9wqv6EIp31w='

    def authenticate(self, request, username=None, password=None):
        login_valid = (self.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, self.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.is_superadmin = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def has_perm(self, user_obj, perm, obj=None):
        if user_obj.username == settings.ADMIN_LOGIN:
            return True
        else:
            return False
