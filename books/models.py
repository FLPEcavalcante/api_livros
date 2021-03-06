from distutils.command.upload import upload
from mailbox import Maildir
from platform import release
from venv import create
from django.db import models
from uuid import uuid4

from django.forms import UUIDField

# Create your models here.

def upload_iamge_book(instance, filename):
    return f"{instance.id_book}-{filename}"

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.DateTimeField(auto_now_add=True)
    create_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to = upload_iamge_book, blank=True, null=True)