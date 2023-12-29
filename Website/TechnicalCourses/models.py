from django.db import models
import datetime
from django.utils import timezone

class AllCourses(models.Model):
    course_name = models.CharField(max_length=200)
    ins_name = models.CharField(max_length=100)
    started_from = models.DateTimeField('Started from')
    def __str__(self):
        return self.course_name
    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.started_from <= now

class details(models.Model):
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    ct = models.CharField(max_length=500)
    your_choice = models.BooleanField(default=False)
    def __str__(self):
        return str(self.ct)