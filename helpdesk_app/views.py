from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Problem
from .forms import ProblemSubmissionForm


def unauthorized_user_form(request):
    if request.method == 'POST':
        form = ProblemSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ProblemSubmissionForm()

    return render(request, 'main_page.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_ticket_list')
        else:
            error_message = "Incorrect login/password"
            return render(request, 'employee_login.html', {'error_message': error_message})
    return render(request, 'employee_login.html')


def user_logout(request):
    logout(request)
    return redirect('employee_login')


@login_required
def problem_list(request):
    problems = Problem.objects.exclude(status="resolved")
    return render(request, 'employee_ticket_list.html', {'problems': problems})


@login_required
def specific(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)

    if request.method == 'POST':
        actions = request.POST.get('actions', '')
        new_status = request.POST.get('status', '')

        problem.actions = actions
        problem.status = new_status

        if new_status == "resolved":
            problem.delete()
            return redirect('employee_ticket_list')
        elif new_status != "in_progress":
            problem.status = new_status

        problem.save()
        return redirect('employee_ticket_list')

    return render(request, 'specific_info.html', {'problem': problem})




















