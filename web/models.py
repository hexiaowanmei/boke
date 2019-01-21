from django.db import models

# Create your models here.


class BokeUser(models.Model):
    username = models.CharField(max_length=20, unique=True, null=True)
    password = models.CharField(max_length=200, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bokeuser'


class BokeToken(models.Model):
    token = models.CharField(max_length=20)
    user = models.OneToOneField(BokeUser, on_delete=models.CASCADE)


    class Meta:
        db_table = 'boketoken'