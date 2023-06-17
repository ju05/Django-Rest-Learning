from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

CATEGORY_CHOICES = (
    ('Dj', 'Django'),
    ('Py', 'Python'),
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices = CATEGORY_CHOICES)
    publish_date = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    

