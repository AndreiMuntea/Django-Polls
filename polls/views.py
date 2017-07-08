from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    context = {'choices': choices, 'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'choices': question.choice_set.all()})


def vote(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    choice.votes += 1
    choice.save()
    return redirect(results, question_id=choice.question_id)
