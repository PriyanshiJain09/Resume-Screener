from django.urls import path
from .views import ResumeMatchAPIView

urlpatterns = [
    path("match/", ResumeMatchAPIView.as_view(), name="resume-match"),
]
