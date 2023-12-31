from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20, choices=[("Author", "Author"), ("Collaborator", "Collaborator")]
    )


class Section(MPTTModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(
        UserProfile, related_name="collaborators", blank=True
    )

    def __str__(self):
        return self.title


class Collaboration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)
