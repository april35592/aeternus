from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='diary/%Y/%m/%d')
    date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.date

class Reply(models.Model):
    imageid = models.ForeignKey(Image, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.name