from django.db import models

class President(models.Model):
    pres_name = models.CharField(max_length=80)
    presimg = models.CharField(max_length=80)
    realfirstlady = models.CharField(max_length=80)

    def __str__(self):
        return str(self.pres_name)


class FirstLady(models.Model):
    president = models.ForeignKey(President)
    lady_name = models.CharField(max_length=80)
    image = models.CharField(max_length=80)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.lady_name)
