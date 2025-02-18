from django.db import models
from django.contrib.auth.models import User

# FAQ Model
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question

# Category Model
class Categories(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Article Model
class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="images/", blank=False)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    categorys = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="articles")
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    likes =  models.ManyToManyField(User, related_name="like_post", blank=True)
    def update_like_count(self):
        self.like_count = self.likes.count()
        self.save()

    def __str__(self):
        return self.title

# Feedback Model
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - commented on {self.article.title}"