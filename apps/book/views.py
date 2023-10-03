from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Book, Section, UserProfile
from .permissions import IsAuthorOrCollaborator
from .serializers import BookSerializer, SectionSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrCollaborator]


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthorOrCollaborator]

    def perform_create(self, serializer):
        # Pass the user object to the serializer
        serializer.save(user_role=self.request.user.userprofile.role)

    @action(detail=True, methods=["POST"])
    def add_collaborator(self, request, pk=None):
        section = self.get_object()
        collaborator_id = request.data.get("collaborator_id")

        try:
            collaborator = UserProfile.objects.get(id=collaborator_id)
        except UserProfile.DoesNotExist:
            return Response(
                {"detail": "Collaborator not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if collaborator in section.collaborators.all():
            return Response(
                {"detail": "Collaborator already added."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        section.collaborators.add(collaborator)
        return Response(
            {"detail": "Collaborator added successfully."}, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["POST"])
    def remove_collaborator(self, request, pk=None):
        section = self.get_object()
        collaborator_id = request.data.get("collaborator_id")

        try:
            collaborator = UserProfile.objects.get(id=collaborator_id)
        except UserProfile.DoesNotExist:
            return Response(
                {"detail": "Collaborator not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if collaborator not in section.collaborators.all():
            return Response(
                {"detail": "Collaborator not found in section."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        section.collaborators.remove(collaborator)
        return Response(
            {"detail": "Collaborator removed successfully."}, status=status.HTTP_200_OK
        )
