from django.db import models


class Category(models.Model):
   name=models.CharField(max_length=100, null=False, blank=False)
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
    due_date = (
        ('R', 'Regular'),
        ('O', 'Overdue'),
        ('N', 'NearOverdue'),

    )
    title=models.CharField(max_length=50, null=False, blank=False)
    description=models.CharField(max_length=200, null=True, blank=True)
    avatar=models.ImageField(upload_to='./images', null=True, blank=True)
    priority = models.CharField(max_length=1, choices=priority,default="M")
    status = models.CharField(max_length=1, choices=status, default="A")
    date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(null=True, blank=True)
    finish_time = models.TimeField(null=True, blank=True)
    due_date = models.CharField(max_length=1, choices=due_date, default="R")
    progress = models.IntegerField(null=True, blank=True, default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)+" "+str(self.description)

class Subset(models.Model):
    status = (
        ('A', 'Active'),
        ('P', 'Pendig'),
        ('D', 'Done'),
    )
    priority = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )
    title = models.CharField(max_length=50, null=False)
    status = models.CharField(max_length=1, choices=status, default="A")
    priority = models.CharField(max_length=1, choices=priority, default='M')
    progress = models.IntegerField(null=True, blank=True, default=0)
    todo= models.ForeignKey('Todo', related_name='+', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.title)


