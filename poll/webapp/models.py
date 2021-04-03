from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=400, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Poll'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return f'{self.question} - {self.created_at}'

class Choice(models.Model):
    choice_text = models.CharField(max_length=400, blank=False, null=False)
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='poll', verbose_name='Опрос')

    class Meta:
        db_table = 'Choice'
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return f'{self.choice_text} - {self.poll}'

