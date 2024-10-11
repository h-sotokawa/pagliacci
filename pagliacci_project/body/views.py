from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BodyComposition
from .forms import BodyCompositionForm

@login_required
def body_list(request):
    body_compositions = BodyComposition.objects.filter(user=request.user)
    return render(request, 'body/body_list.html', {'body_compositions': body_compositions})

@login_required
def body_add(request):
    if request.method == 'POST':
        form = BodyCompositionForm(request.POST)
        if form.is_valid():
            body_composition = form.save(commit=False)
            body_composition.user = request.user
            body_composition.save()
            return redirect('body_list')
    else:
        form = BodyCompositionForm()
    return render(request, 'body/body_form.html', {'form': form})

@login_required
def body_edit(request, pk):
    body_composition = get_object_or_404(BodyComposition, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BodyCompositionForm(request.POST, instance=body_composition)
        if form.is_valid():
            form.save()
            return redirect('body_list')
    else:
        form = BodyCompositionForm(instance=body_composition)
    return render(request, 'body/body_form.html', {'form': form})

@login_required
def body_delete(request, pk):
    body_composition = get_object_or_404(BodyComposition, pk=pk, user=request.user)
    if request.method == 'POST':
        body_composition.delete()
        return redirect('body_list')
    return render(request, 'body/body_confirm_delete.html', {'body_composition': body_composition})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('body_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
