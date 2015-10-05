from django.db import models

class President(models.Model):
    pres_name = models.CharField(max_length=80)
    presimg = models.CharField(max_length=80)
    realfirstlady = models.CharField(max_length=80)

    def __str__(self):
        return str(self.pres_name)
1

class FirstLady(models.Model):
    president = models.ForeignKey(President)
    lady_name = models.CharField(max_length=80)
    image = models.CharField(max_length=80)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.lady_name)

class RecipePost(models.Model):
    title = models.CharField(max_length=40)
    urltitle = models.CharField(max_length=40)
    upvotes = models.IntegerField(default=1)
    downvotes = models.IntegerField(default=0)
    ingredients = models.CharField(max_length=200)
    instructions = models.CharField(max_length=300)

    def __str__(self):
        return str("Recipe Title: " + str(self.title))


class RecipeComment(models.Model):
    recipe = models.ForeignKey(RecipePost)
    text = models.CharField(max_length=200)

    def __str__(self):
        return "comment on " + str(self.recipe)
