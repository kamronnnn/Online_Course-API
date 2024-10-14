from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()

router.register('directions', DirectionViewSet)
router.register('teachers', TeacherViewSet)
router.register('courses', CourseViewSet)
router.register('groups', GroupViewSet)
router.register('lessons', LessonViewSet)
router.register('students', StudentViewSet)
router.register('parents', ParentsViewSet)
router.register('students-rating', AverageRatingViewSet)
router.register('teachers-rating', TeacherRatingViewSet)
router.register('course-comments', CourseCommentViewSet)
router.register('lesson-comments', LessonCommentViewSet)
router.register('like-dislike', LikeOrDislikeLessonViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('filter-theme/', FilterTheme.as_view()),
    path('send-mail/', SendMail.as_view()),
]
