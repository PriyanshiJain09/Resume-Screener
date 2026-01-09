from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import tempfile

from matcher.nlp.pipeline import run_resume_matching



class ResumeMatchAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        resume_file = request.FILES.get("resume")
        jd_text = request.data.get("job_description")

        if not resume_file or not jd_text:
            return Response(
                {"error": "Resume file and job description are required"},
                status=400
            )

        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            for chunk in resume_file.chunks():
                tmp.write(chunk)
            resume_path = tmp.name

        result = run_resume_matching(resume_path, jd_text)

        return Response(result)

