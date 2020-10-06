from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=150)
    total_score = models.PositiveIntegerField()
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Task(models.Model):
    name = models.CharField(max_length=1000)
    task = models.TextField()
    score = models.PositiveIntegerField()
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Solve(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    text = models.TextField()
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return str(self.task_id)

    class Meta:
        verbose_name = "Решение"
        verbose_name_plural = "Решения"
