from django.shortcuts import render, redirect
from .models import Question, Option, UserAnswer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegisterForm
from datetime import datetime


# Registration view

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login view using Django's AuthenticationForm
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quiz')  # Redirect to the home page or quiz
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('about')



@login_required(login_url='login')
def quiz_view(request):
    questions = Question.objects.all()  # Get all questions
    
    if request.method == 'POST':
        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            if selected_option_id:
                selected_option = Option.objects.get(id=selected_option_id)
                # Store the user's answer
                UserAnswer.objects.create(
                    user=request.user,
                    question=question,
                    selected_option=selected_option
                )
        return redirect('quiz_result')  # Redirect to result page or elsewhere

    return render(request, 'quiz.html', {'questions': questions})

@login_required(login_url='login')
def quiz_result_view(request):
    user_answers = UserAnswer.objects.filter(user=request.user)
    score = sum([1 for answer in user_answers if answer.selected_option.is_correct])
    total_questions = user_answers.count()
    
    return render(request, 'quiz_result.html', {
        'user_answers': user_answers,
        'score': score,
        'total_questions': total_questions,
    })
date=datetime.now().year
def base(request):
    print(date)
    return render(request,'base.html',{'date':date})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about_us.html')