from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    #return HttpResponse("Hello World, You're at the polls index")
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #output = ', '.join(q.question_text for q in latest_question_list)
    #return HttpResponse(output)

    #template = loader.get_template("polls/index.html") #load templte
    #context = {"latest_question_list": latest_question_list,} #dict, context for template
    #return HttpResponse(template.render(context, request))

    #context = {"latest_question_list": latest_question_list}
    #return render(request, "polls/index.html", context)
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#def detail(request, question_id):
    
    #try:
    #    question = Question.objects.get(pk=question_id)  #primary key

    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/detail.html",{"question":question}) #3rd arg = context
    #return HttpResponse("You're looking at question %s." %question_id)

#def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/results.html", {'question': question})

def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id) #model of thing we are getting, primary key
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {'question': question, 'error_message':"You didn't selecte a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    #return HttpResponse("You're voting on question %s." % question_id)