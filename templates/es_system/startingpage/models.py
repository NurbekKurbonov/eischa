from django.db import models

class Page(models.Model):
    title = models.CharField('Sarlavha', max_length=60)
    permalink = models.CharField('Link', max_length=12, unique=True)
    update_date = models.DateTimeField('Oxirgi yangilanish')
    bodytext = models.TextField('Yozuv')
    def __str__(self):
        return self.title
