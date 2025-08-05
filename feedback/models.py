from django.db import models

from app.models import User

"""
this is the feedback model, it has a user, title and created_at fields
it is used to store the feedbacks sent by users

"""


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


"""
this is the message model, a feedback can have multiple messages 
messages are sent by users to the feedback system
their current format is markdown
"""


class Message(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    msg_type = models.CharField(max_length=10, default="md")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
