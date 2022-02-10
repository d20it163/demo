from models import db


class Student(models.Model):
  student_name = models.CharField(max_length=100)
  student_id = models.CharFeield(max_length=100)
  
  def __str__(self):
    return f"{student_name}"
