from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'direction_photo')

    def direction_photo(self, direction_photo):
        return mark_safe(f'<img src="{direction_photo.image.url}" width="75px">')

    direction_photo.short_description = 'Rasm'


# ----------------------------------------------------------------------------------------------------------------------


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience')
    list_display_links = ('name',)


# ----------------------------------------------------------------------------------------------------------------------


class CourseAdmin(admin.ModelAdmin):
    list_display = ('direction', 'name', 'start_date', 'price')
    list_display_links = ('name',)


# ----------------------------------------------------------------------------------------------------------------------


class GroupAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'teacher', 'max_student')


# ----------------------------------------------------------------------------------------------------------------------


class LessonAdmin(admin.ModelAdmin):
    list_display = ('group', 'theme', 'homework')


# ----------------------------------------------------------------------------------------------------------------------


class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'register_date', 'birth_date', 'group',
                    'address')


# ----------------------------------------------------------------------------------------------------------------------


class ParentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'address')


# ----------------------------------------------------------------------------------------------------------------------


class AverageRatingAdmin(admin.ModelAdmin):
    list_display = ('student', 'rating', 'added')


class TeacherRatingAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'rating')
    list_display_links = ('teacher', )


# ----------------------------------------------------------------------------------------------------------------------


class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'added')


# ----------------------------------------------------------------------------------------------------------------------


class LessonCommentAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'student', 'added')


# ----------------------------------------------------------------------------------------------------------------------


class LikeOrDislikeAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'student', 'like_or_dislike')


# ----------------------------------------------------------------------------------------------------------------------


admin.site.register(Direction, DirectionAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Parents, ParentAdmin)
admin.site.register(AverageRating, AverageRatingAdmin)
admin.site.register(TeacherRating, TeacherRatingAdmin)
admin.site.register(CourseComment, CourseCommentAdmin)
admin.site.register(LessonComment, LessonCommentAdmin)
admin.site.register(LikeOrDislikeLesson, LikeOrDislikeAdmin)
