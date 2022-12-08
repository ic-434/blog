from django.db import models


class Task(models.Model):
    title = models.CharField('название', max_length=100)
    task = models.TextField('описание')


    def __str__(self):
        return self.title
# создали класс Task, далее выполнить команды:...makemigrations, ...migrate

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'тексты'
# переименовали названия класса в админ. панеле
