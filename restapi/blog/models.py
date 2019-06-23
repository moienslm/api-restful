from django.db import models
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='./images')
    def __str__(self):
        return str(self.name)

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return  str(self.title)

