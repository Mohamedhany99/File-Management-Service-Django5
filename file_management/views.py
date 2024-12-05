# file_management/views.py
from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_xml.renderers import XMLRenderer
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from collections import Counter
import random


# Task 1 Upload and store files
class FileUploadView(generics.CreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    parser_classes = (
        MultiPartParser,
        FormParser,
    )


# Task 2 get random line from the uploaded file and if header application/*
class RandomLineView(APIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer, XMLRenderer]

    def get(self, request):
        accept_header = request.META.get("HTTP_ACCEPT", "text/plain")
        files = UploadedFile.objects.all()
        if not files:
            return HttpResponse(status=404)

        file = random.choice(files)
        with open(file.file.path) as f:
            lines = f.readlines()
        # Get the random line and its index in a single step
        line_index = random.randrange(len(lines))
        line = lines[line_index].strip()
        line_number = line_index + 1
        most_common_letter = Counter(line.replace(" ", "")).most_common(1)[0][0]

        if accept_header == "application/json":
            return JsonResponse(
                {
                    "line": line,
                    "line_number": line_number,
                    "file_name": file.filename,
                    "most_common_letter": most_common_letter,
                }
            )
        elif accept_header == "application/xml":
            response = f"""
            <response>
                <line>{line}</line>
                <line_number>{line_number}</line_number>
                <file_name>{file.filename}</file_name>
                <most_common_letter>{most_common_letter}</most_common_letter>
            </response>
            """
            return HttpResponse(response, content_type="application/xml")
        else:
            return HttpResponse(line, content_type="text/plain")


# Task 3 Random Line Backwards
class RandomLineBackwardsView(APIView):
    def get(self, request):
        files = UploadedFile.objects.all()
        if not files:
            return HttpResponse(status=404)

        file = random.choice(files)
        with open(file.file.path) as f:
            lines = f.readlines()

        line = random.choice(lines).strip()
        reversed_line = line[::-1]

        return HttpResponse(reversed_line, content_type="text/plain")


class Longest100LinesView(APIView):
    def get(self, request):
        all_lines = []
        files = UploadedFile.objects.all()
        for file in files:
            with open(file.file.path) as f:
                lines = f.readlines()
                all_lines.extend([line.strip() for line in lines])

        longest_lines = sorted(all_lines, key=len, reverse=True)[:100]
        return JsonResponse({"longest_100_lines": longest_lines})


class Longest20LinesOfFileView(APIView):
    def get(self, request, filename):
        try:
            file = UploadedFile.objects.get(filename=filename)
        except UploadedFile.DoesNotExist:
            return HttpResponse(status=404)

        with open(file.file.path) as f:
            lines = f.readlines()

        longest_lines = sorted([line.strip() for line in lines], key=len, reverse=True)[
            :20
        ]
        return JsonResponse({"longest_20_lines": longest_lines})
