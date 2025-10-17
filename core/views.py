from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Category, Photo, ContactMessage
from .forms import LoginForm, PhotoForm

def home(request):
    cats = Category.objects.all().prefetch_related('photos')[:5]
    return render(request, "home.html", {"cats": cats})

def services(request):
    cats = Category.objects.all()
    return render(request, "services.html", {"cats": cats})

def category_detail(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    photos = cat.photos.all()
    can_manage = request.user.is_authenticated
    return render(request, "category_detail.html", {"cat": cat, "photos": photos, "can_manage": can_manage})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                return redirect("services")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def manage_gallery(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    if request.method == "POST":
        if "delete" in request.POST:
            Photo.objects.filter(id=request.POST.get("delete")).delete()
        else:
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                p = form.save(commit=False)
                p.category = cat
                p.save()
        return redirect("manage_gallery", slug=slug)
    return render(request, "manage_gallery.html", {"cat": cat, "photos": cat.photos.all(), "form": PhotoForm()})

def contact_view(request):
    sent = False
    if request.method == "POST":
        full_name = request.POST.get("full_name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        message = request.POST.get("message", "")
        ContactMessage.objects.create(full_name=full_name, email=email, phone=phone, message=message)

        body = f"שם: {full_name}\nטלפון: {phone}\nאימייל: {email}\n\nהודעה:\n{message}"
        send_mail("פנייה מהאתר – צור קשר", body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_RECIPIENT])
        sent = True
    return render(request, "contact.html", {"sent": sent})
