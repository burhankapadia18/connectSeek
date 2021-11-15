from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register((Teacher_table,Student_table,Subject_table,Semester_table,Attendance_table,Tbl_attendance,Notice,Resources))
