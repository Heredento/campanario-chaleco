import os
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# today = datetime.datetime.today(pytz.timezone('Etc/GMT+6'))
### https://docs.djangoproject.com/en/4.1/topics/files/
backup_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, '/backups/'))
song_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, '/songs/'))

class auth_code(models.Model):
    username = models.CharField (max_length=150)
    email = models.CharField (max_length=254)
    code = models.CharField (max_length=6)
    toverify = models.BooleanField(default=True)
    
class AuthCodeVerification(models.Model):
    username = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        related_name='validation_username', 
        on_delete=models.CASCADE)
    email = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        related_name='validation_email', 
        on_delete=models.CASCADE)
    code = models.CharField (max_length=6)
    toverify = models.BooleanField(default=True)
    
    
class events_list(models.Model):
    name = models.CharField (max_length=50)
    selection = models.IntegerField()
    time = models.CharField (max_length=20)
    week = models.CharField (max_length=20, blank=True)
    song = models.IntegerField()
    currentyear = models.BooleanField(default=False)
    date = models.CharField(blank=True, max_length=20)

class events_files(models.Model):
    filename = models.CharField (max_length=11)
    title = models.CharField (max_length=255)
    

class events_backups(models.Model):
    filename = models.CharField (max_length=11)
    title = models.CharField (max_length=255)
    creationdate=models.CharField (max_length=20, blank=True)


class EventSongsBackups(models.Model):
    title=models.CharField (max_length=255)
    file_name=models.CharField (max_length=11)
    song_file = models.FileField(upload_to=backup_storage)
    creation_date=models.DateTimeField()


class EventSongsFiles(models.Model):
    title=models.OneToOneField(
        EventSongsBackups, 
        related_name='title_create_retrieve', 
        on_delete=models.RESTRICT)
    file_name=models.OneToOneField(
        EventSongsBackups, 
        related_name='filename_create_retrieve', 
        on_delete=models.RESTRICT)
    song_file=models.FileField(upload_to=backup_storage)


class ClockInformation(models.Model):
    name = models.CharField (max_length=255, blank=True)
    is_active = models.BooleanField(default=False, blank=True)
    
