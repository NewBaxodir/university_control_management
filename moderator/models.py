from django.db import models
from django.contrib.auth.models import AbstractUser


class MainUser(AbstractUser):

    def __str__(self) -> str:
        return '%s (%s %s)'%(self.username, self.last_name, self.first_name)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = '1. Userlar'

