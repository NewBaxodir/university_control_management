from django.db import models



from moderator.models import MainUser



class EducationalDepartmentManager(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    
    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        verbose_name = 'O\'quv bo\'limi manageri'
        verbose_name_plural = '1. O\'quv bo\'limi managerlari'


