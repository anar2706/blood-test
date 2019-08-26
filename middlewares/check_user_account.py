from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class CheckUserAccount:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        try:
            if request.user.donor.is_closed:
                logout(request)
                messages.add_message(request, messages.ERROR, _("Your account is closed"))
                return redirect('account_login')
        except:
            pass

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
