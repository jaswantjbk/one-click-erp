from django.db import models

class Attendance(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent'),
        ]
    )

    def __str__(self):
        return f"{self.name} - {self.date}"
