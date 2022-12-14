from django.db import models
import os
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    head_image = models.ImageField(upload_to='blog/image/%Y/%m/%d/',
                                   blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/',
                                   blank=True)
    hook_text = models.CharField(max_length=100, blank=True)
    # author : 추후 작성예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
