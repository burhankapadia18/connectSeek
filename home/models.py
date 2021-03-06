from django.db import models
import datetime

# Create your models here.

class Teacher_table(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'male'),('F', 'female'),('T', 'transgender'),))
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    degree = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Student_table(models.Model):
    roll_no = models.CharField(primary_key=True, max_length=12)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'male'),('F', 'female'),('T', 'transgender'),))
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10, null=False, blank=False, unique=True)
    address = models.CharField(max_length=200)
    session = models.CharField(max_length=9)
    program = models.CharField(max_length=10)
    semester = models.CharField(max_length=1)
    profileImage = models.ImageField(upload_to="home/profileImage", default="")

    def __str__(self):
        return str(self.roll_no)+" "+self.first_name

class Subject_table(models.Model):
    id = models.CharField(max_length=9,primary_key=True)
    subject_name = models.CharField(max_length=50)
    teacher_id = models.ForeignKey(Teacher_table, on_delete=models.CASCADE)
    field = models.CharField(max_length=15)
    semester = models.CharField(max_length=1)

    def __str__(self):
        return self.subject_name

class Semester_table(models.Model):
    semester_no = models.CharField(max_length=1)
    field = models.CharField(max_length=15, default="")
    subject = models.ForeignKey(Subject_table, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject.id + " " + self.field

class Attendance_table(models.Model):
    id = models.AutoField(primary_key=True)
    program = models.CharField(max_length=10)
    semester = models.CharField(max_length=1)
    subject = models.ForeignKey(Subject_table, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher_table, on_delete=models.CASCADE)
    stud_roll = models.ForeignKey(Student_table, on_delete=models.CASCADE)
    attendance = models.CharField(max_length=1, choices=(('P','present'),('A','absent'),))
    date = models.DateField()

class Tbl_attendance(models.Model):
    id = models.AutoField(primary_key=True)
    stud_roll_no = models.ForeignKey(Student_table, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject_table, on_delete=models.CASCADE)
    semester = models.CharField(max_length=1)
    attendence = models.CharField(max_length=1,choices=(('P','present'),('A','absent'),))
    date = models.DateField(auto_now_add=True)

class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    details = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="home/notices", default="")

class Resources(models.Model):
    id = models.AutoField(primary_key=True)
    detail = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject_table, on_delete=models.CASCADE, default="")
    file = models.FileField(upload_to="home/files", default="")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

class assignment_details(models.Model):
    id = models.AutoField(primary_key=True)
    given_by = models.ForeignKey(Teacher_table, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject_table, on_delete=models.CASCADE)
    detail = models.CharField(max_length=100, default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=0)

class assigment_data(models.Model):
    student = models.ForeignKey(Student_table, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to="home/assignments")
    assignment = models.ForeignKey(assignment_details, on_delete=models.CASCADE, default="")
    timestamp = models.DateTimeField(auto_now_add=True)

class FeesPayment(models.Model):
    transaction_id = models.CharField(max_length=1000000, primary_key=True)
    student = models.ForeignKey(Student_table, on_delete=models.CASCADE)
    semester = models.CharField(max_length=1)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=1000000)
    payment_mode = models.CharField(max_length=10, choices=(('UPI','UPI'),('DD','Demand Draft'),('Cash','Cash')))