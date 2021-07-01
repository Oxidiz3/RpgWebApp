from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Character(models.Model):
    name = models.CharField(max_length=200)

    # what makes you SPECIAL?
    stamina = models.IntegerField(default=0)
    perception = models.IntegerField(default=0)
    endurance = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    luck = models.IntegerField(default=0)

    def __str__(self):
        return (f"<h2>{self.name}</h2>"
                f"<br/>Stamina: {self.stamina}<br/>"
                f"Perception: {self.perception}<br/>"
                f"Endurance: {self.endurance}<br/>"
                f"Charisma: {self.charisma}<br/>"
                f"Intelligence: {self.intelligence}<br/>"
                f"Agility: {self.agility}<br/>"
                f"Luck: {self.luck}<br/>")
