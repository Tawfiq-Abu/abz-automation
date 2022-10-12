from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.core.exceptions import PermissionDenied
# Create your views here.

# @method_decorator([login_required()], name="dispatch")
class BlogView(ListView):
    template_name = "back/author/blog/index.html"
    model = Blog
    form_class = BlogForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {
            "url4": "active",
            "blogs": Blog.objects.all(),
            "form": form
        }
        return render(request, self.template_name, context=context)
    
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST, request.FILES)
    #     if form.is_valid():
    #         object = form.save(commit=False)
    #         object.author = self.request.user
    #         object.save()
    #     else:
    #         print(form.errors)
    #     return redirect('author:blogs')


# @method_decorator([login_required()], name="dispatch")
class BlogDetailView(DetailView):
    template_name = "back/author/blog/show.html"
    model = Blog
    form_class = BlogForm

    def get(self, request, *args, **kwargs):
        # the detail view has access to the current instance so we just call the increase_views func
        object = self.get_object()
        
        # if not (object.author == request.user or request.user.is_admin):
        #     raise PermissionDenied()
        
        object.increase_views()
        
        form = self.form_class(instance=object)
        context = {
            "url4": "active",
            'form': form,
            "tutorial": object
        }
        return render(request, self.template_name, context=context)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST, instance=self.get_object())
    #     if form.is_valid():
    #         form.save()

    #     #   to be changed after writing urls
    #     return redirect("author:blog", kwargs={'slug': self.get_object().slug})
    
