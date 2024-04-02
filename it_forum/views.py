from django.shortcuts import render, get_object_or_404
from it_forum.forms import ItForumForm, ReviewForm
from django.http import HttpResponse
from it_forum.models import ItForum
from django.views import generic
from django.urls import reverse


class AnsewersListView(generic.ListView):
    template_name = "crud/answers_list.html"
    context_object_name = "answer"
    model = ItForum

    def get_queryset(self):
        return self.model.objects.all()


# def answers_list_view(request):
#     if request.method == "GET":
#         answer = ItForum.objects.all()
#         return render(request, template_name='crud/answers_list.html',
#                       context={'answer': answer})


class AnswersDetailView(generic.DetailView):
    template_name = 'crud/answers_detail.html'
    context_object_name = 'answer_id'
    model = ItForum

    def get_object(self, **kwargs):
        answer_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=answer_id)


# def answers_detail_view(request, id):
#     if request.method == "GET":
#         answer_id = get_object_or_404(ItForum, id=id)
#         return render(request, template_name='crud/answers_detail.html', context={
#             'answer_id': answer_id
#         })

class CreateAnswerView(generic.CreateView):
    template_name = 'crud/create_answer.html'
    form_class = ItForumForm
    success_url = '/answer_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateAnswerView, self).form_valid(form=form)


class CreateReviewView(generic.CreateView):
    template_name = 'crud/create_review.html'
    form_class = ReviewForm
    success_url = '/answer_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)



# def create_answer_it_forum_view(request):
#     if request.method == 'POST':
#         form = ItForumForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Answer create successfully</h1>')
#     else:
#         form = ItForumForm()
#     return render(request, template_name='crud/create_answer.html',
#                   context={'form': form})


# Удаление

class DeleteAnswerView(generic.DeleteView):
    template_name = "crud/confirm_delete.html"
    success_url = '/answer_list/'
    model = ItForum

    def get_object(self, **kwargs):
        answer_id = self.kwargs.get("id")
        return get_object_or_404(self.model, id=answer_id)


# def delete_answer_it_forum_view(request, id):
#     answer_id = get_object_or_404(ItForum, id=id)
#     answer_id.delete()
#     return HttpResponse('<h1>Answer Deleted Successfully</h1>')


# Изменение данных
class UpdateAnswerView(generic.UpdateView):
    template_name = "crud/edit_answer.html"
    form_class = ItForumForm
    model = ItForum

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateAnswerView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        answer_id = self.kwargs.get("id")
        return get_object_or_404(self.model, id=answer_id)

    def get_success_url(self, **kwargs):
        answer_id = self.kwargs.get("id")
        return reverse("it_forum:detail", kwargs={"id": answer_id})


# def edit_answer_it_forum_view(request, id):
#     answer_id = get_object_or_404(ItForum, id=id)
#     if request.method == 'POST':
#         form = ItForumForm(request.POST, instance=answer_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Answer is updated successfully</h1>')
#     else:
#         form = ItForumForm(instance=answer_id)
#     return render(request, template_name='crud/edit_answer.html',
#                   context={'form': form})


class SearchAnswerView(generic.ListView):
    template_name = "crud/answers_list.html"
    context_object_name = "answer"
    paginate_by = '5'

    def get_queryset(self):
        return ItForum.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get("q")
        return context
