from django.shortcuts import render
from .decorators import admin_only
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User


@admin_only
def banusers(request):
    users = User.objects.all()
    return render(request, 'banusers.html', context={'users': users})


@admin_only
def ban_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.banstatus.is_banned = True
    user.banstatus.save()
    return redirect("administrator:banusers")  # Replace "user_list" with the URL name of the user list page


@admin_only
def unban_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.banstatus.is_banned = False
    user.banstatus.save()
    return redirect("administrator:banusers")  # Replace "user_list" with the URL name of the user list page


def notallowed(request):
    return render(request, 'notallowed.html')
