from django.db import models


class Student(models.Model):
    name = models.TextField(max_length=100)
    roll_no = models.CharField(max_length=40, default="")
    register_no = models.CharField(max_length=40, default="")
    mob_number = models.CharField(max_length=40, default="")

    class Meta:
        app_label = 'student_data'

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    name = models.TextField(max_length=100)
    department = models.CharField(max_length=40, default="")
    mob_number = models.CharField(max_length=40, default="")

    class Meta:
        app_label = 'teacher_data'

    def __unicode__(self):
        return self.name


class DemoRouter:
    """
    A router to control all database operations on models in the
    user application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to studentdb.
        """
        if model._meta.app_label == 'student_data':
            return 'studentdb'
        elif model._meta.app_label == 'teacher_data':
            return 'teacherdb'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to studentdb.
        """
        if model._meta.app_label == 'student_data':
            return 'studentdb'
        elif model._meta.app_label == 'teacher_data':
            return 'teacherdb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'student_data' or \
                obj2._meta.app_label == 'teacher_data':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'student_data':
            return db == 'studentdb'
        if app_label == 'teacher_data':
            return db == 'teacherdb'
        return None
