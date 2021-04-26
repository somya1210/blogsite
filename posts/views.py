from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.forms import PostForm,CommentForm
# Create your views here.
class CommentViews(generic.CreateView):
    model=Comment
    form_class = CommentForm
    template_name='Blog/add_comment.html'
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    reverse_lazy('post_detail')

def LikeViews(request,pk):
  post=get_object_or_404(Post,id=request.POST.get('post_id'))
  liked=False
  if post.likes.filter(id=request.user.id).exists():
      post.likes.remove(request.user)
      liked=False
  else:
      post.likes.add(request.user)
      liked=True
  return HttpResponseRedirect(reverse('post_detail',args=[str(post.slug)]))

class HomePage(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'Blog/homepage.html'

class DetailView(generic.DetailView):
 model = Post
 template_name = 'Blog/post_detail.html'
 def get_context_data(self,*args,**kwargs):
     context=super(DetailView,self).get_context_data(*args,**kwargs)
     forlike=get_object_or_404(Post,slug=self.kwargs['slug'])
     total_like=forlike.total_likes()
     context["total_like"]=total_like
     liked=False
     if forlike.likes.filter(id=self.request.user.id).exists():
         liked=True
     context["liked"]=liked
     return context


class AddPostview(generic.CreateView):
    model=Post
    form_class = PostForm
    template_name = 'Blog/post_form.html'

class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'Blog/post_update.html'

class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'Blog/post_delete.html'
    success_url = reverse_lazy('home')

