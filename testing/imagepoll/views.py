from django.shortcuts import render, get_object_or_404
from .models import Question
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

# Create your views here.

def index(request):
    retrqs = Question.objects.all()
    return render(request, 'imagepoll/index.html', {'questions' : retrqs})

def reindex(request):
    return HttpResponseRedirect(reverse('index'))

def questionview(request, question_id):
    approQuestion = get_object_or_404(Question, pk=question_id)
    return render(request, 'imagepoll/questiontemp.html', {
            'question' : approQuestion,
        })
