from django.db import models

class Position(models.Model):
    position1_1 = models.CharField(max_length=20, null=True)
    position1_2 = models.CharField(max_length=20, null=True)
    position2_1 = models.CharField(max_length=20, null=True)
    position2_2 = models.CharField(max_length=20, null=True)
    position3_1 = models.CharField(max_length=20, null=True)
    position3_2 = models.CharField(max_length=20, null=True)
    position4_1 = models.CharField(max_length=20, null=True)
    position4_2 = models.CharField(max_length=20, null=True)
    position5_1 = models.CharField(max_length=20, null=True)
    position5_2 = models.CharField(max_length=20, null=True)
    position6_1 = models.CharField(max_length=20, null=True)
    position6_2 = models.CharField(max_length=20, null=True)
