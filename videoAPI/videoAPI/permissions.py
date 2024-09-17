from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
    
class IsAuthenticatedNoDelete(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return False
        return bool(request.user and request.user.is_authenticated)
    

class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS