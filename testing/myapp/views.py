from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from myapp.models import Question, Choice
from django.template import loader
from django.urls import reverse

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5:-1]
    output = ', '.join([q.question_text for q in latest_question_list])

    context = {
                'latest_question_list': latest_question_list,
            }
    return render(request, 'myapp/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'myapp/detail.html', {'question' : question})

def parens(request, firarg):
    str = "this is the first argument " + firarg
    return (HttpResponse(str))

def vote(request, question_id):
    approQuestion = get_object_or_404(Question, pk=question_id)
    try:
        approChoice = approQuestion.choice_set.get(pk=request.POST['choice'])
    except ( KeyError, Choice.DoesNotExist):
        return render(request, 'myapp/detail.html', {
            'question' : approQuestion,
            'error_message': "You didn't select a choice.",
        })
    else:
        approChoice.votes += 1
        approChoice.save()
        return HttpResponseRedirect(reverse('result', args=(approQuestion.id,)))
def result(request, question_id):
    approQuestion = get_object_or_404(Question, pk=question_id)
    choices = list(approQuestion.choice_set.all())
    return render(request, 'myapp/result.html', {
            'question' : approQuestion,
            'choices' : choices,
        })
