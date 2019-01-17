from django.conf import settings
from django.contrib.auth import get_user_model

class EmailBackend(object):
     def authenticate(self, username=None, password=None, **kwargs):
        user = get_user_model()

        try:
            user = user.objects.get(email=username)
        except user.DoesNotExist:
            return None
        if user.check_password(password) and getattr(user,'is_active'):
                return user
        return None
     def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
