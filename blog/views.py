from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

class BlogList(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'object_list'
    paginate_by = 5
    paginate_orphans = 3
    ordering = ['-id']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutPageView(TemplateView):
    template_name = 'post_detail.html'

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'О нас'})