from django.db import models
from datetime import date
# Create your models here.

class Todo(models.Model):
    title = models.CharField(verbose_name="titulo",max_length=100,null=False,blank=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True,blank=False)
    deadline = models.DateField(verbose_name="data de entrega",null=False,blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ['deadline']
    
    def mark_completed(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()