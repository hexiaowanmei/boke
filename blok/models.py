

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    keyword = models.CharField(max_length=50, null=True)
    describe = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    label = models.CharField(max_length=100, null=True)
    img = models.ImageField(upload_to='upload', null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=0)


    class Meta:
        db_table = 'article'


class Category(models.Model):
    name = models.CharField(max_length=10, null=True)
    art = models.ForeignKey

    class Meta:
        db_table = 'category'