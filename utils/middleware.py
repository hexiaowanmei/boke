from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

from web.models import BokeUser


class BlokTest(MiddlewareMixin):
    def process_request(self, request):
        path = request.path
        if path in ['/blok/register/', '/blok/login/']:
            return None
        try:
            user_id = request.session['user_id']
            user = BokeUser.objects.get(pk=user_id)
            request.user = user
            return None
        except Exception as e:
            return HttpResponseRedirect(reverse('blok:login'))

