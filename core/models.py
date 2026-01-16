from django.db import models


class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url_path = models.CharField(max_length=100, default="/")
    is_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
