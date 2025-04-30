from rest_framework import generics
from . import models, serializers
from rest_framework.response import Response


class StudentListAPIView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentListSerializer


class StudentCreateAPIView(generics.CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentDetailSerializer


class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentDetailSerializer


class StudentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentDetailSerializer


class SponsorListAPIView(generics.ListAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorListSerializer


class SponsorUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorUpdateSerializer


class SponsorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorRetrieveSerializer


class SponsorCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorCreateSerializer

    def get_queryset(self):
        student_id = self.request.query_params.get('student_id')
        if student_id:
            return self.queryset.filter(student_id=student_id)
        return self.queryset


class SponsorDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorCreateSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response({"message": "success"})