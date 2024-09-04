from django.db import models

# Create your models here.
from django.db import models

class AudioFile(models.Model): 
    file = models.FileField(upload_to='audio/')
    uploaded = models.DateTimeField(auto_now_add=True)
    

# The AudioFile model represents an audio file that can be uploaded by the user.
# It has a single field, file, which is a FileField that stores the uploaded audio file.
    