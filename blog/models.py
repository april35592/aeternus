from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    thumnail = models.ImageField(upload_to='blog')
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'blog:postList', slug


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    thumbnail = models.ImageField(
        upload_to='blog/%Y/%m/%d', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='blog/%Y/%m/%d')
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
