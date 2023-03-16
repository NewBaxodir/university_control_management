from django.db import models



from moderator.models import MainUser
from fakultet.models import Faculty

class CafedraManager(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')

    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        verbose_name = 'Kafedra manageri'
        verbose_name_plural = '1. Kafedra managerlari'



class Cafedra(models.Model):
    name = models.CharField(max_length=200, verbose_name='Kafedra nomi')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='Fakulteti')
    manager = models.ForeignKey(CafedraManager, on_delete=models.CASCADE, verbose_name='Kafedra manageri')

    def __str__(self) -> str:
        return '%s (%s)'%(self.name, str(self.manager))
    
    class Meta:
        verbose_name = 'Kafedra'
        verbose_name_plural = '2. Kafedralar'