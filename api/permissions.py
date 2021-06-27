from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and (obj.user == request.user or request.user.is_staff)
        )


#class IsOwnerOrReadOnly(BasePermission):
#    def has_permission(self, request, view):
#        if request.method in SAFE_METHODS:
#            return True
#        user = request.user
#        if view.action == "create":
#            return True
#        article = view.get_object()
#        return article.author_id == user.id#


#class IsUserOrReadOnly(BasePermission):
#    def has_permission(self, request, view):
#        if request.method in SAFE_METHODS:
#            return True
##        if view.action == "create":
 #           return True
 #       user = view.get_object()
 #       return request.user.id == user.id