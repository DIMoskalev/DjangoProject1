from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from main.forms import StudentForm
from main.models import Student


class StudentListView(ListView):
    model = Student


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}: {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('main:base')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('main:base')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:base')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:base'))


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
