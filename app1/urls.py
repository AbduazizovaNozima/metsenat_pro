from project.urls import path
from . import views


urlpatterns = [
    path('student/', views.StudentListAPIView.as_view()),
    path('student-create/', views.StudentCreateAPIView.as_view()),
    path('student-update/<int:pk>', views.StudentUpdateAPIView.as_view()),
    path('student-retrieve/<int:pk>', views.StudentRetrieveAPIView.as_view()),
    path('sponsor/', views.SponsorListAPIView.as_view()),
    path('sponsor-update/<int:pk>', views.SponsorUpdateAPIView.as_view()),
    path('sponsor-retrieve/<int:pk>', views.SponsorRetrieveAPIView.as_view()),
    path('sponsor-create/', views.SponsorCreateListAPIView.as_view()),
    path('sponsor-delete/<int:pk>', views.SponsorDeleteAPIView.as_view()),
]