from django.db import models

class User(models.Model):
    username = models.CharField("Username", max_length=20)
    name = models.CharField("Ім'я",max_length=20)
    surname = models.CharField("Прізвище",max_length=20)
    phone_number = models.CharField("Номер телефону", max_length=17)
    email = models.CharField("Електронна пошта", max_length=50)

    def __str__(self):
        return self.username

class Word(models.Model):
    Slovo = models.CharField("Слово", max_length=20)
    Perevod = models.CharField("Переклад", max_length=15)
    languages = models.TextField("На яку мову перекладено", max_length=100)

    class Meta:
        db_table = 'user_word'
    def __str__(self):
        return self.Slovo



