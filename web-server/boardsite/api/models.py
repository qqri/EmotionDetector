# api/models.py
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    subtitle = models.CharField(max_length=144, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #body = RichTextUploadingField()
    def __str__(self):
        return '[{}] {}'.format(self.user , self.title)

    def post_save(self):
        self.save()

    #이유는 모르겠는데 이거하면 안됨
    # class Meta:
    #     managed = False
    #     db_table = 'Post'