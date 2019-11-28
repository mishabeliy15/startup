from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Category, SubCategory
from django.urls import reverse_lazy


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list_category.html'


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', 'display')
    template_name = 'category/add_category.html'
    success_url = reverse_lazy('category:list-category')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name', 'display')
    template_name = 'category/update_category.html'
    success_url = reverse_lazy('category:list-category')


class CategoryDeleteView(DeleteView):
    model = Category
    fields = ('name', 'display')
    template_name = 'category/update_category.html'
    success_url = reverse_lazy('category:list-category')


class SubCategoryCreateView(CreateView):
    model = SubCategory
    fields = ('category', 'name', 'display')
    template_name = 'category/subcategory/add_subcategory.html'
    success_url = reverse_lazy('category:list-category')


class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    fields = ('category', 'name', 'display')
    template_name = 'category/subcategory/update_subcategory.html'
    success_url = reverse_lazy('category:list-category')


class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    fields = ('category', 'name', 'display')
    template_name = 'category/subcategory/update_subcategory.html'
    success_url = reverse_lazy('category:list-category')
