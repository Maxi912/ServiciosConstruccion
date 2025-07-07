from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def about_view(request):
    return render(request, 'pages/about.html')


from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all().order_by('-fecha')
    return render(request, 'pages/blog_list.html', {'blogs': blogs})


from django.shortcuts import get_object_or_404

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'pages/blog_detail.html', {'blog': blog})

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from .forms import BlogForm

def es_admin(user):
    return user.is_staff

@login_required
@user_passes_test(es_admin)
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.autor = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'pages/blog_form.html', {'form': form})


@login_required
@user_passes_test(es_admin)
def blog_update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'pages/blog_form.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'pages/blog_confirm_delete.html', {'blog': blog})