from django.db import models


class Category(models.Model):
   name=models.CharField(max_length=100)
   def __str__(self):
       return str(self.name)

class Todo(models.Model):
    priority = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )
    status = (
        ('A', 'Active'),
        ('P', 'Pendig'),
        ('D', 'Done'),
    )
    title=models.CharField(max_length=50, null=False)
    description=models.CharField(max_length=200, null=True, blank=True)
    avatar=models.ImageField(upload_to='./images', null=True, blank=True)
    priority = models.CharField(max_length=1, choices=priority)
    status = models.CharField(max_length=1, choices=status, default="A")
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    finish_time = models.TimeField(null=True, blank=True)
    progress = models.IntegerField(null=True, blank=True, default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)+" "+str(self.description)


