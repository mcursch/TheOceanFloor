from django.db import models
from django.conf import settings
from django.utils import timezone
# Django Model Documentation: https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
# to maintain functionality, model should extend Model class
class Post(models.Model):        
    # foreign key acts as a link to another model    
    # on_delete allows us to cascade delete this field when authors is deleted (?)       
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    # when we want to publish this, set its pub date to now and save it
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    # if we want to express this post as a string (i.e. print it, print the title)
    def __str__(self):
        return self.title
        