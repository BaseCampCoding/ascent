from django.shortcuts import render, redirect
from django.views.generic import View
from shoutouts.forms import ShoutoutForm
from shoutouts.models import Shoutout
from django.utils import timezone

# Create your views here.


class Shoutouts(View):
    def get(self, request):
        form = ShoutoutForm(request.POST)
        shoutouts = Shoutout.objects.all()
        return render(request, "shoutouts.html", {"form": form, "shoutouts": shoutouts})

    def post(self, request):
        form = ShoutoutForm(request.POST)
        shoutouts = Shoutout.objects.all()
        if form.is_valid():
            recipient = form.cleaned_data["recipient"]
            content = form.cleaned_data["content"]
            create_new_shoutout = Shoutout.objects.create(
                recipient=recipient,
                content=content,
                datetime=timezone.now(),
                user=request.user,
            )
            return redirect("home")
        elif not form.is_valid():
            return render(
                request, "shoutouts.html", {"form": form, "shoutouts": shoutouts}
            )