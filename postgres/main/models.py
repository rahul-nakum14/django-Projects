from django.db import models
    
class course (models.Model):
    course_name = models.CharField(max_length=100)
    course_id = models.CharField(primary_key='True',max_length=100)

    def __str__(self):
        return self.course_name
    
class student(models.Model):
    name = models.CharField(max_length=10)
    Er_no = models.IntegerField()
    Address = models.TextField()
    image = models.ImageField(upload_to='pics')
    CHOICES = [
            ('Subject 1', 'Data Science'),
            ('Subject 2', 'AI/ML'),
            ('Subject 3', 'Python'),
        ]
    choice = models.CharField(
        max_length=100,
        choices=CHOICES,
        default='Subject 2'
    )
   
    def __str__(self):
        return self.name
    
class register(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)