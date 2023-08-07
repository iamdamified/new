from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.views.generic import DetailView

# Create your views here.

class ShowProfilePage(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def update(self, *args, **kwargs):
        users = Profile.objects.all()
        contect = super(ShowProfilePage, self).get_context_data(*args, **kwargs)

        current_user = get_object_or_404(Profile, )