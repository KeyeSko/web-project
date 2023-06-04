from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.

AnecCategory = (
    ("Family", "FAMILY"),
    ("Army", "ARMY"),
    ("Other", "OTHER")
)


class Anecdot(models.Model):
    text = models.TextField()
    # like_count = models.IntegerField(default='0')
    liked = models.ManyToManyField(User, blank=True, related_name='likes')
    category = models.CharField(max_length=10, choices=AnecCategory, default='Other')

    def num_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anecdot = models.ForeignKey(Anecdot, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)

    def __str__(self):
        return f"{self.user}-{self.anecdot}-{self.value}"
