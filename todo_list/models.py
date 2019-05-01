from django.db import models
from django import forms


class TodoList(models.Model):
    task = models.CharField(max_length=100)

    Doing = 'необходимо выполнить'
    Done = 'сделано'
    Canceled = 'отменено'

    Status = (
    	(Doing, 'необходимо выполнить'),
    	(Done, 'сделано'),
    	(Canceled, 'отменено'),
    	)

    Status = models.CharField(max_length=20, choices=Status, default=Doing)

    def __str__(self):
    	return self.task