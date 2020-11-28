from django.core.exceptions import PermissionDenied

class LoginMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(LoginMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied