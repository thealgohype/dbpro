from django.db import models

# Create your models here.

class mytest(models.Model):
    val1 = models.CharField(max_length=100)
    val2 = models.CharField(max_length=100)
    val3 = models.CharField(max_length=100)
    class Meta:
        db_table = 'chatprocollection'