from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    by_user = models.CharField(max_length=50)
    def __str__(self):
        return (self.question_text + " by " + self.by_user)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    side = models.CharField(max_length=1)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return (self.side + " -- " + self.question.question_text + " -- " + str(self.votes))
