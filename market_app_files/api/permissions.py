from rest_framework.permissions import BasePermission, SAFE_METHODS

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

class IsStafforReadOnly(BasePermission):
    def has_permission(self, request, view):
        is_staff = bool(request.user and request.user.is_staff)
        return is_staff or request.method in SAFE_METHODS

class IsAdminForDeleteOrPatchReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        elif request.method == "DELETE":
            return bool(request.user and request.user.is_superuser)
        else: 
            bool(request.user and request.user.is_staff)


class IsOwnerorAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        elif request.method == "DELETE":
            return bool(request.user and request.user.is_superuser)
        else:
         return bool(request.user and request.user == obj.user)  
            