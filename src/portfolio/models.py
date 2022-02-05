from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(_("image"), upload_to='images',
                              blank=True, null=True)

    def __str__(self):
        return str(self.title)
