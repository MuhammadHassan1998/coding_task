from rest_framework import permissions


class IsAuthorOrCollaborator(permissions.BasePermission):
    """
    Custom permission to allow authors and collaborators to edit sections/subsections.
    Only authors can create new sections/subsections.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        user_profile = request.user.userprofile
        if view.action == "create":
            return user_profile.role == "Author"
        elif view.action in ["update", "partial_update", "destroy"]:
            return user_profile.role in ["Author", "Collaborator"]
        return True
