from django.db import models


from moderator.models import MainUser


class FacultyManager(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')

    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        verbose_name = 'Fakultet manageri'
        verbose_name_plural = '1. Fakultet managerlari'




class Faculty(models.Model):
    name = models.CharField(max_length=200, verbose_name='Fakultet nomi')
    manager = models.ForeignKey(FacultyManager, on_delete=models.CASCADE, verbose_name='Fakultet manageri')

    def __str__(self) -> str:
        return '%s (%s)'%(self.name, str(self.manager))
    
    class Meta:
        verbose_name = 'Fakultet'
        verbose_name_plural = '2. Fakultetlar'