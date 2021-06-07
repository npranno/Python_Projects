from django.db import models
#import all models to database

#create class called djangoClasses, with following attributes

class djangoClasses(models.Model):
    course_title = models.CharField(max_length=60)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=60)
    course_duration = models.DecimalField(max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.course_title