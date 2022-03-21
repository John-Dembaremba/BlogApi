from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Checks HTTP verbs from the request are in SAFE_METHOD
        if request.method in permissions.SAFE_METHODS:
            return True

        # If not in SAFE_METHOD, then checks if author is the logged in user
        return obj.author == request.user