from django.db import models


# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class Meta:
    db_table='users'

def __str__(self):
    return self.name


class Todo(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
class Meta:
    db_table='Todo'

def __str__(self):
    return self.title

