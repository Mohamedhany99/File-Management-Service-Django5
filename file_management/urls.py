# file_management/urls.py
from django.urls import path
from .views import (
    FileUploadView,
    RandomLineView,
    RandomLineBackwardsView,
    Longest100LinesView,
    Longest20LinesOfFileView,
)

urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="upload_file"),
    path("random-line/", RandomLineView.as_view(), name="random_line"),
    path(
        "random-line-backwards/",
        RandomLineBackwardsView.as_view(),
        name="random_line_backwards",
    ),
    path("longest-100-lines/", Longest100LinesView.as_view(), name="longest_100_lines"),
    path(
        "longest-20-lines/<str:filename>/",
        Longest20LinesOfFileView.as_view(),
        name="longest_20_lines_of_file",
    ),
]
