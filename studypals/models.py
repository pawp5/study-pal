<<<<<<< HEAD
from django.db import models


# Create your models here.
class ChatBox(models.Model):
    title = models.CharField(max_length=100)
    # owner = models.ForeignKey(User)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Text(models.Model):
    # chatbox = models.ForeignKey(ChatBox, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=64)
    unit = models.PositiveIntegerField()
    outline = models.TextField()

    def __str__(self):
        return self.code

class TimeTable(models.Model):
    mon = models.TextField()
    tue = models.TextField()
    wed = models.TextField()
    thu = models.TextField()
    fri = models.TextField()
=======
from django.db import models

# Create your models here.
>>>>>>> 8370b914406d0e7e6cc81cdd76708d4004b83da8
