from unittest import result
from django.shortcuts import redirect, render
from blog.forms import BlogCommentForm, BlogPostForm, CategoryForm
from blog.models import BlogComment, BlogPost, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


# Create your views here.

# View all the blogs
def view_allBlogs(request):
    blogs = BlogPost.objects.all().order_by('-date_posted')
    categoryList = Category.objects.all()
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {'page_title': 'All Blogs', 'blogs': blogs,
               'categoryList': categoryList, 'page': page}
    return render(request, 'blogs.html', context)

# View a single blog by id

def view_aBlog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    categoryList = Category.objects.all()
    blog_comments = func_get_all_comments(blog_id)
    context = {'page_title': blog.title,
               'blog': blog, 'categoryList': categoryList, 'comments': blog_comments}
    return render(request, 'blog.html', context)


# View a single blog by slug

def view_aBlog_bySlug(request, blog_slug):
    blog = BlogPost.objects.get(slug_title=blog_slug)
    categoryList = Category.objects.all()
    blog_comments = func_get_all_comments(blog.id)
    context = {'page_title': blog.title,
               'blog': blog, 'categoryList': categoryList, 'comments': blog_comments}
    return render(request, 'blog.html', context)

# Create a new blog


@login_required
def view_add_aBlog(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        form.instance.author=request.user
        if(form.is_valid()):
            form.save()
            return redirect('view_allBlogs')
    return render(request, 'add_blog.html', {'form': form})


# update a new blog
@login_required
def view_update_blog(request, blog_id):
    if request.user!=BlogPost.objects.get(id=blog_id).author:
        return redirect('view_allBlogs')
    blog = BlogPost.objects.get(id=blog_id)
    form = BlogPostForm(instance=blog)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
        return redirect('view_allBlogs')
    return render(request, 'update_blog.html', {'form': form})

# View all the categories


def view_allCategory(request):
    categories = Category.objects.all()
    context = {'page_title': 'All Category', 'category': categories}
    return render(request, 'categorys.html', context)

# View a category blog by id


def view_aCategory(request, cId):
    ctg = Category.objects.get(id=cId)
    blogs = BlogPost.objects.filter(category=ctg)
    categoryList = Category.objects.all()
    context = {'page_title': ctg.name,
               'blogs': blogs, 'categoryList': categoryList}
    return render(request, 'blogs.html', context)

# view a single category by category name


def view_aCategory_byName(request, categoryName):
    cId = Category.objects.get(name=categoryName).id
    return redirect('view_aCategory', cId)

# Create a new blog


@login_required
def view_add_aCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_allCategory')
    return render(request, 'add_category.html', {'form': form})


# For search functionality
# Searching by title

def view_search_blog_title(request):
    search_text = request.POST.get('query')
    result = BlogPost.objects.filter(
        title__icontains=search_text)  # i means ignore case
    categoryList = Category.objects.all()
    context = {'page_title': 'Search Result',
               'blogs': result, 'categoryList': categoryList}
    return render(request, 'blogs.html', context)


# For blog comments

# get all the comments for a blog
def func_get_all_comments(blog_id):
    return BlogComment.objects.filter(blog=blog_id)

# count the number of comments


def func_count_comments(blog_id):
    return func_get_all_comments(blog_id).count()


@login_required
def view_add_comment(request,blog_id):
    c_message=request.POST.get('message')
    c_author=request.user
    c_blog=BlogPost.objects.get(id=blog_id)
    commit=BlogComment.objects.create(comment=c_message,author=c_author,blog=c_blog)
    commit.save()
    # add the comment count to the blog
    blog=BlogPost.objects.get(id=blog_id)
    blog.count_comments=func_count_comments(blog_id)+1
    return redirect('view_aBlog',blog_id)

