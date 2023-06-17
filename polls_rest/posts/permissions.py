from rest_framework import permissions

class isManager(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.username == 'juju':
            return False
        else: return True

class isStudent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.title.lower() == 'test post 3' and request.user.username == 'student':
            return False
        else: return True