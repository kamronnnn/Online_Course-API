from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.


class Direction(models.Model):
    """Bu model Yo'nalish yozilgan (masalan: Backend, Frontend, QA)"""

    name = models.CharField(max_length=50, verbose_name="Yo'nalishlar",
                            help_text="Yo'nalish ni kiriting")

    created = models.DateTimeField(verbose_name="Yo'nalish ochilgan vaxt",
                                   help_text="Yo'nalish ochilgan vaxt ni kiriting")

    updated = models.DateTimeField(auto_now_add=True, verbose_name="Yo'nalish yangilngan vaxt")

    description = models.TextField(verbose_name="Yo'nalish bo'yicha qisqacha ma'lumot",
                                   help_text="Yo'nalish bo'yicha qisqacha ma'lumot kiriitng")

    status = models.BooleanField(default=True, verbose_name="Status",
                                 help_text="Yo'nalish faol yoki faol emas")

    image = models.ImageField(upload_to='directions/',
                              null=True, blank=True, verbose_name="Yo'nalish Rasmi",
                              help_text="Yo'nalish Rasmini kiriting")

    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"
        ordering = ['-created']

    def __str__(self):
        return self.name


# ----------------------------------------------------------------------------------------------------------------------

class Teacher(models.Model):
    """Teacher(Ustozlar) uchun model"""

    name = models.OneToOneField(User, on_delete=models.CASCADE)
    about_teacher = models.TextField(null=True, blank=True)
    experience = models.CharField(max_length=10, verbose_name="Ustozni Tajribasi",
                                  help_text="Ustozni Tajribasini kiriting")

    phone_number = models.CharField(max_length=13, verbose_name="Ustozni tel raqami",
                                    help_text="Ustozni Tel raqamini kiriting")

    is_active = models.BooleanField(default=True, help_text="Ustoz Ishlayabtimi ?")

    class Meta:
        verbose_name = "Ustoz"
        verbose_name_plural = "Ustozlar"

    def __str__(self):
        return self.name.username


# ----------------------------------------------------------------------------------------------------------------------


class Course(models.Model):
    """Kurs uchun model"""

    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, verbose_name="Kurs Nomi",
                            help_text="Kurs nomini kiriting")

    duration = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True,
                                   help_text="Kurs Haqida qisqacha ma'lumot")

    start_date = models.DateTimeField(help_text="Kurs boshlanish vaxti")
    end_date = models.DateTimeField(help_text="Kurs tugash vaxti")
    created = models.DateTimeField(help_text="Kurs ochilgan vaxt")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Kurs Narxi",
                                help_text="Kurs narxini kiriting")

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.name


# ----------------------------------------------------------------------------------------------------------------------


class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=5, verbose_name="Guruh nomi",
                            help_text="Guruh nomi")

    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True,
                                help_text="Ustozni Tanlang")

    created = models.DateTimeField(verbose_name="Guruh ochilgan sanasi",
                                   help_text="Guruh ochilgan sanasi")

    max_student = models.CharField(max_length=13, verbose_name="O'quvchilar soni",
                                   help_text="O'quvchilar soni")

    def __str__(self):
        return self.name


# ----------------------------------------------------------------------------------------------------------------------


class Lesson(models.Model):
    """Bu model darslar uchun"""

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    theme = models.CharField(max_length=100, verbose_name="Mavzu nomi",
                             help_text="Mavzu nomi")

    description = models.TextField(null=True, blank=True, verbose_name="Izoh",
                                   help_text="Mavzu haqida batafsil ma'lumot")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Mavzu sanasi",
                                   help_text="Mavzu sanasi")

    updated = models.DateTimeField(auto_now=True, verbose_name="Mazvu yangilangan sana",
                                   help_text="Mazvu yangilangan sana")

    video = models.FileField(upload_to='theme/videos', validators=[
        FileExtensionValidator(allowed_extensions=['MP4', 'ASF', 'FLV', 'MKV', 'MOV'])
    ])

    homework = models.CharField(max_length=100, verbose_name="Uyga vazifa",
                                help_text="Uyga vazifa")

    def __str__(self):
        return self.theme


# ----------------------------------------------------------------------------------------------------------------------


class Student(models.Model):
    """Bu model o'quvchilarga uchun"""

    full_name = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True, verbose_name="Tug'ilgan sana",
                                  help_text="Tug'ilgan sana")

    register_date = models.DateTimeField(verbose_name="Ro'yxatdan o'tgan sana",
                                         help_text="Ro'yxatdan o'tgan sana")

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True,
                              help_text="Qaysi guruhda o'qiydi")

    phone_number = models.CharField(max_length=13, verbose_name="Tel raqam",
                                    help_text="Tel raqam")

    address = models.CharField(max_length=100, verbose_name="Yashash joyi",
                               help_text="Yashash joyi")

    def __str__(self):
        return self.full_name.username


# ----------------------------------------------------------------------------------------------------------------------


class Parents(models.Model):
    """Bu model o'quvchilarni ota-onalari uchun
    Kirib nazorat qilib turishlari uchun"""

    full_name = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=13, verbose_name="Tel raqam",
                                    help_text="Tel raqam")

    address = models.CharField(max_length=100, verbose_name="Yashash joyi",
                               help_text="Yashash joyi")

    last_login = models.DateTimeField(auto_now_add=True, verbose_name="Saytga kirgan vaxti",
                                      help_text="Saytga kirgan vaxti")

    register_date = models.DateTimeField(verbose_name="Ro'yxatdan o'tgan sana",
                                         help_text="Ro'yxatdan o'tgan sana")

    def __str__(self):
        return self.full_name.username


# ----------------------------------------------------------------------------------------------------------------------


class AverageRating(models.Model):
    """Bu model o'quvchini o'rtacha baxosi uchun
    1 dan 5 gacha"""

    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    rating = models.CharField(max_length=3, verbose_name="Baxosi",
                              help_text="Baxosi")

    added = models.DateTimeField(auto_now_add=True, verbose_name="Baxo berilgan vaxt",
                                 help_text="Baxo berilgan vaxt")

    updated = models.DateTimeField(auto_now_add=True, verbose_name="Baxo yangilangan vaxt",
                                   help_text="Baxo yangilangan vaxt")

    def __str__(self):
        return self.student.full_name.username


# ----------------------------------------------------------------------------------------------------------------------


class TeacherRating(models.Model):
    """Bu model o'qituvchini reyting uchun"""

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    rating = models.CharField(max_length=3, verbose_name="Baxosi",
                              help_text="Baxosi")

    added = models.DateTimeField(auto_now_add=True, verbose_name="Baxo berilgan vaxt",
                                 help_text="Baxo berilgan vaxt")

    updated = models.DateTimeField(auto_now_add=True, verbose_name="Baxo yangilangan vaxt",
                                   help_text="Baxo yangilangan vaxt")

    def __str__(self):
        return self.teacher.name.username


# ----------------------------------------------------------------------------------------------------------------------


class CourseComment(models.Model):
    """Bu model kurs ga izoh qoldirish uchun"""

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    parent = models.OneToOneField(Parents, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(verbose_name="izoh", help_text="Izoh")
    added = models.DateTimeField(auto_now_add=True, verbose_name="Izoh qo'shilgan vaxt")
    update = models.DateTimeField(auto_now_add=True, verbose_name="izoh yangilangan vaxt")

    def __str__(self):
        return self.course.name


# ----------------------------------------------------------------------------------------------------------------------


class LessonComment(models.Model):
    """Bu model dars ga izoh qoldirish uchun"""

    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(verbose_name="izoh", help_text="Izoh")
    added = models.DateTimeField(auto_now_add=True, verbose_name="Izoh qo'shilgan vaxt")
    update = models.DateTimeField(auto_now_add=True, verbose_name="izoh yangilangan vaxt")

    def __str__(self):
        return self.lesson.theme


# ----------------------------------------------------------------------------------------------------------------------


class LikeOrDislikeLesson(models.Model):
    """Bu model Darsga like(yoqdi) yoki dislike(yoqmadi)"""

    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    like_or_dislike = models.BooleanField(default=False, verbose_name="Like or Dislike",
                                          help_text="True()yoqdi, False(yoqmadi)")

    added = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Yangilangan sana")

    def __str__(self):
        return self.lesson.theme
