from rest_framework.permissions import BasePermission, SAFE_METHODS

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

class IsStafforReadOnly(BasePermission):
    def has_permission(self, request):
        is_staff = bool(request.user and request.user.is_staff)
        return is_staff or request.method in SAFE_METHODS