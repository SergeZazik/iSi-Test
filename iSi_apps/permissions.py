from rest_framework.permissions import BasePermission, SAFE_METHODS


class SaveMethodsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 1 or request.method in SAFE_METHODS:
            return True
        return False
