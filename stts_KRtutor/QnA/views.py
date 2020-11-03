from django.shortcuts import render, redirect
from .models import QuestionAndAnswer
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.


def QnA_list(request):
    QnAs = QuestionAndAnswer.objects.all().order_by("hit")

    return render(request, "QnA/list.html", context={"QnAs": QnAs})


def MyQnA(request):
    userid = request.user
    
    MyQnAs = QuestionAndAnswer.objects.filter(author=userid.id).order_by("hit")
        
    return render(request, "QnA/myqna.html", context={"MyQnAs": MyQnAs})


class QnAUploadView(CreateView):
    model = QuestionAndAnswer
    fields = ["title", "text"]
    template_name = "QnA/upload.html"

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')

        else:
            return self.render_to_response({"form" : form})


class QnADeleteView(DeleteView):
    model = QuestionAndAnswer
    success_url = '/'
    template_name = 'QnA/delete.html'

class QnAUpdateView(UpdateView):
    model = QuestionAndAnswer
    fields = ["title", "text"]
    template_name = "QnA/update.html" 

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')

        else:
            return self.render_to_response({"form" : form})



