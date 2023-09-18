from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Question, Choice

# Create your views here.
def index(request):
    last_five_questions = Question.objects.order_by("-pub_date")[:5]
    context = { "latest_question_list": last_five_questions }
    # output = ', '.join([q.question_text for q in last_five_questions])
    return render(request=request, context=context, template_name="polls/index.html")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request=request, template_name="polls/detail.html", context=context)

def results(request, question_id):
    return HttpResponse(f'You\'re looking at the results of question {question_id}.')

def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}.')