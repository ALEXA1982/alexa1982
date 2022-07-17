from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect


from .models import Question,Chochice
from django.http import Http404
from django.urls import reverse
from django.views import generic

#def index(request):
    #latest_question_list= Question.objects.order_by('-pub_date')[:5]
   #context = {'latest_question_list': latest_question_list}

   # return render(request, "polls/index.html",context)
class IndexView(generic.ListView):
   template_name = 'polls/index.html'
   context_object_name = 'latest_question_list'
   def get_queryset(self):
       return Question.objects.order_by('-pub_date')[:5]

#def detail(request, question_id):
   # question = get_object_or_404(Question,pk=question_id)

    #try:
      # question=Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
       # raise Http404(" Question doesn t exist")


   # return render(request, "polls/detail.html",{"question":question})
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"



#def results(request, question_id):
 #   question = get_object_or_404(Question,pk=question_id)
  #  return render(request, "polls/results.html",{"question":question})

class ResultsView(generic.DetailView):
     model = Question
     template_name ="polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_chochice = question.chochice_set.get(pk=request.POST["chochice"])
    except (KeyError, Chochice.DoesNotExist):
        return render(request, "polls/detail.html",
                      {"question": question,
                       "error_message": "U didn't select a chochice",})
    else:
        selected_chochice.votes += 1
        selected_chochice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))









