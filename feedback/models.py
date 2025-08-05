# class Feedback:

from django.db import models


class Users(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    msg_type = models.CharField(max_length=10, default="md")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(Users, on_delete=models.CASCADE)
