from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# model class for category instances
class category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
# model class for poem itself


class poetry(models.Model):
    Author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    # this will update every single time
    updated = models.DateField(auto_now=True)
    # this will be taken only ones not more anymore
    created = models.DateTimeField(auto_now_add=True)

    # this helps sort poems in decending order
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        l = self.content.split('\n')
        res = '\n'.join(l[:4])
        return res

# model class for comments instances have attributes like user as foreign keys


class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poetry = models.ForeignKey(poetry, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
