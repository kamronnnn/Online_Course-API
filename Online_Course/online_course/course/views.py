from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import *
from .serializers import *

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


class DirectionViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ParentsViewSet(ModelViewSet):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer


class AverageRatingViewSet(ModelViewSet):
    queryset = AverageRating.objects.all()
    serializer_class = AverageRatingSerializer


class TeacherRatingViewSet(ModelViewSet):
    queryset = TeacherRating.objects.all()
    serializer_class = TeacherRatingSerializer


class CourseCommentViewSet(ModelViewSet):
    queryset = CourseComment.objects.all()
    serializer_class = CourseCommentSerializer


class LessonCommentViewSet(ModelViewSet):
    queryset = LessonComment.objects.all()
    serializer_class = LessonCommentSerializer


class LikeOrDislikeLessonViewSet(ModelViewSet):
    queryset = LikeOrDislikeLesson.objects.all()
    serializer_class = LikeOrDislikeLessonSerializer


class FilterTheme(APIView):
    def get(self, request):
        word = request.query_params.get('word')

        if word:
            theme = Lesson.objects.filter(theme__icontains=word)
            serializer = LessonSerializer(theme, many=True).data
            return Response({'theme': serializer})
        else:
            return Response({'error': 'Keyword NOT FOUND'})


class SendMail(APIView):

    def get(self, request):
        serializer = MailSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = MailSerializer(data=request.data)
        serializer.is_valid()

        users = User.objects.all()
        for user in users:
            subject = serializer.validated_data.get('name')
            message = serializer.validated_data.get('text')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)

        return Response({'success': "Yuborildi"})
