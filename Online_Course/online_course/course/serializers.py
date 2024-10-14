from rest_framework import serializers

from .models import *


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'
        depth = 1


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        depth = 1


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        depth = 1


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        depth = 1


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        depth = 1


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1


class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = '__all__'
        depth = 1


class AverageRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AverageRating
        fields = '__all__'
        depth = 1


class TeacherRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherRating
        fields = '__all__'
        depth = 1


class CourseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseComment
        fields = '__all__'
        depth = 1


class LessonCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonComment
        fields = '__all__'
        depth = 1


class LikeOrDislikeLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeOrDislikeLesson
        fields = '__all__'
        depth = 1


class MailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    text = serializers.CharField()
