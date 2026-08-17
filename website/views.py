from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm


def home(request):
    return render(request, "website/home.html")


def about(request):
    return render(request, "website/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

            return redirect("contact")

    else:
        form = ContactForm()

    return render(
        request,
        "website/contact.html",
        {"form": form},
    )