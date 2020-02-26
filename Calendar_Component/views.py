from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.template import loader
from .models import Choice, Question

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'Calendar_Component/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions(not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'Calendar_Component/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'Calendar_Component/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'Calendar_Component/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Calendar_Component:results', args=(question.id,)))

    # def index(request)
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('Calendar_Component/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))


# def detail(request, question_id):

    # error handling
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')

    # you can also write like below
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'Calendar_Component/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'Calendar_Component/results.html', {'question': question})
