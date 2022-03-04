from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import PostForm
from .models import Post



def index(request):
    context = {'posts': Post.objects.order_by('-pub_date')[:10]}
    return render(request, 'index.html', context=context)

class PostView(generic.DetailView):
    model = Post
    template_name = 'post.html'

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'  

class UpdatePostView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'

    success_url = reverse_lazy('index')
