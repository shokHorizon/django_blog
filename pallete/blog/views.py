from datetime import date, timedelta
from unicodedata import category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import PostForm, CommentForm
from .models import Post



def index(request):
    delta_week = date.today()-timedelta(days=7)
    context = {
        'recent_posts': Post.objects.order_by('-pub_date')[:3],
        'popular_posts': Post.objects.filter(pub_date__gte=delta_week).order_by('-likes')[:3],
        }
    return render(request, 'index.html', context=context)
    
    
def post_view(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
            
    context = {
        'form': CommentForm(),
        'post': post
    }
            
    return render(request, 'post.html', context)

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html' 
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
    
def likePostView(request, post_id):
    if request.method == 'GET':
        user = get_user(request)
        post = Post.objects.get(id=post_id)
        if user not in post.likes.all():
            post.likes.add(user)
        else:
            post.likes.remove(user)
        post.save()
            
    
    return redirect('index')

def create_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        form = CommentForm(request.POST)
        form.instance.author = request.user
        form.instance.post = post
        if form.is_valid():
            form.save()
    
    return redirect('post', post_id)

def search_post(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        category = request.GET.get('category', '')
        posts = Post.objects

        if category:
            posts = posts.filter(category__name=category)
        if q:
            posts = posts.filter(Q(title__icontains=q)|Q(text__icontains=q))

        context = {
            'posts': posts,
            'category': category,
            }
    
    return render(request, 'search.html', context)

