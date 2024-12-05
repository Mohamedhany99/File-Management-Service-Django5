# file_management/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from .models import UploadedFile
import os


class FileManagementTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.file_path = "test_file.txt"
        with open(self.file_path, "w") as f:
            f.write("\n".join([f"Line {i}" for i in range(1, 101)]))

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_upload_file(self):
        with open(self.file_path, "rb") as f:
            response = self.client.post("/file-management/upload/", {"file": f})
        self.assertEqual(response.status_code, 200)
        self.assertIn("filename", response.json())

    def test_random_line(self):
        with open(self.file_path, "rb") as f:
            self.client.post("/file-management/upload/", {"file": f})
        response = self.client.get(
            "/file-management/random-line/", HTTP_ACCEPT="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("line", response.json())

    def test_longest_100_lines(self):
        with open(self.file_path, "rb") as f:
            self.client.post("/file-management/upload/", {"file": f})
        response = self.client.get("/file-management/longest-100-lines/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("longest_100_lines", response.json())

    def test_longest_20_lines_of_file(self):
        with open(self.file_path, "rb") as f:
            self.client.post("/file-management/upload/", {"file": f})
        response = self.client.get(
            f"/file-management/longest-20-lines/{self.file_path}/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("longest_20_lines", response.json())
