from django.db import models
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class EmailModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(Q(email__iexact=username)|Q(username__iexact=username))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        
        return None