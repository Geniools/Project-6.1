from rest_framework import permissions


class IsTreasurerIsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow users with the treasurer role write privileges in the API.
    """
    
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Delete permissions are only allowed to superusers.
        if request.method == 'DELETE' and not request.user.is_superuser:
            return False
        
        # Write permissions are only allowed to superusers and users with the treasurer role.
        return request.user.is_superuser or request.user.is_treasurer
