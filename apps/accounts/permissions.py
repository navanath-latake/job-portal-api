from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsRecruiter(BasePermission):
    """Allow access only to users with role 'recruiter'."""
    Message = 'Only recruiters can perform this action.'
    
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.role == 'recruiter'
        )

class IsApplicant(BasePermission):
    """Allow Access only to users with role 'applicant'."""
    message = 'Only applicants can perform this action.'
    
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.role == 'applicant'
        )
        
class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission.
    Read: anyone authenticated.
    Write: only the owner of the object.
    """
    message = 'You can only edit your own content.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.recruiter == request.user


class IsRecruiterOrReadOnly(BasePermission):
    """
    Read: anyone authenticated.
    Write: only recruiters.
    """
    message = 'Only recruiters can modify job listings.'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return (
            request.user and
            request.user.is_authenticated and
            request.user.role == 'recruiter'
        )