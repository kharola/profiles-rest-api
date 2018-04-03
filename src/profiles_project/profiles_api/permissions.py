from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to update only their own profile"""

    def has_object_permission(self, request, view, obj):
        """check users is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHOD:
            return True

        return obj.id == request.user.id
