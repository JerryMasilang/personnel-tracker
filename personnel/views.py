from django.shortcuts import get_object_or_404, redirect, render
from .forms import PersonnelForm
from .models import Personnel


def personnel_list(request):
    personnel_records = Personnel.objects.all().order_by('full_name')
    return render(request, 'personnel/personnel_list.html', {
        'personnel_records': personnel_records
    })


def personnel_create(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personnel_list')
    else:
        form = PersonnelForm()

    return render(request, 'personnel/personnel_form.html', {
        'form': form,
        'page_title': 'Add Personnel'
    })


def personnel_update(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)

    if request.method == 'POST':
        form = PersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('personnel_list')
    else:
        form = PersonnelForm(instance=personnel)

    return render(request, 'personnel/personnel_form.html', {
        'form': form,
        'page_title': 'Edit Personnel'
    })


def personnel_delete(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)

    if request.method == 'POST':
        personnel.delete()
        return redirect('personnel_list')

    return render(request, 'personnel/personnel_confirm_delete.html', {
        'personnel': personnel
    })