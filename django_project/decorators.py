from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def only_instructor(view_func):
    def wrapper(request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if not user.is_instructor:
            messages.warning(request, 'Permission Denied. You do not have access to this resource')
            return redirect('dashboard')
        response = view_func(request, *args, **kwargs) 
        return response
    return wrapper

def only_learner(view_func):
    def wrapper(request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if not user.is_learner:
            messages.warning(request, 'Permission Denied. You do not have access to this resource')
            return redirect('dashboard')
        response = view_func(request, *args, **kwargs) 
        return response
    return wrapper