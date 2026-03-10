from django.db import models
from django.conf import settings
from apps.projects.models import Project


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = 'TODO', 'Нужно сделать'
        IN_PROGRESS = 'IN_PROGRESS', 'В процессе'
        DONE = 'DONE', 'Выполнено'

    class Priority(models.TextChoices):
        LOW = 'LOW', 'Низкий приоритет'
        MID = 'MID', 'Средний приоритет'
        HIGH = 'HIGH', 'Высокий приоритет'
        CRITICAL = 'CRITICAL', 'Критичный приоритет'


    headline = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, 
        choices=Status.choices,
        default=Status.TODO
    )
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MID
    )
    deadline = models.DateField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name='created_tasks'
    )
    executer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks'
    )
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.headline


class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Комментарий от {Comment.author} о {self.task}"