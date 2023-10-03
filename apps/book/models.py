from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    parent_section = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE
    )

    def __repr__(self):
        return self.title


class Subsection(models.Model):
    title = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    parent_subsection = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE
    )

    def __repr__(self):
        return self.title


class Collaboration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)

    def __repr__(self):
        return self.user.name
