from django.shortcuts import redirect, render
from blog.forms import BlogPostForm, CategoryForm
from blog.models import BlogPost, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# Create your views here.

# View all the blogs
def view_allBlogs(request):
    blogs=BlogPost.objects.all().order_by('-date_posted')
    categoryList=Category.objects.all()
    paginator=Paginator(blogs,5)
    page=request.GET.get('page')
    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    except EmptyPage:
        blogs=paginator.page(paginator.num_pages)
    context={'page_title':'All Blogs','blogs':blogs,'categoryList':categoryList,'page':page}
    return render(request,'blogs.html',context)

# View a single blog by id
def view_aBlog(request,blog_id):
    blog=BlogPost.objects.get(id=blog_id)
    categoryList=Category.objects.all()
    context={'page_title':blog.title,'blog':blog,'categoryList':categoryList}
    return render(request,'blog.html',context)

# Create a new blog
def view_add_aBlog(request):
    form=BlogPostForm()
    if request.method=='POST':
        form=BlogPostForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('view_allBlogs')
    return render(request,'add_blog.html',{'form':form})


# update a new blog
def view_update_blog(request,blog_id):
    blog=BlogPost.objects.get(id=blog_id)
    form=BlogPostForm(instance=blog)
    if request.method=='POST':
        form=BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
        return redirect('view_allBlogs')
    return render(request,'update_blog.html',{'form':form}) 







# View all the categories
def view_allCategory(request):
    categories=Category.objects.all()
    context={'page_title':'All Category','category':categories}
    return render(request,'categorys.html',context)

# View a category blog by id
def view_aCategory(request,cId):
    ctg=Category.objects.get(id=cId)
    blogs=BlogPost.objects.filter(category=ctg)
    categoryList=Category.objects.all()
    context={'page_title':ctg.name,'blogs':blogs,'categoryList':categoryList}
    return render(request,'blogs.html',context)

# view a single category by category name
def view_aCategory_byName(request,categoryName):
    cId=Category.objects.get(name=categoryName).id
    return redirect('view_aCategory',cId)

# Create a new blog
def view_add_aCategory(request):
    form=CategoryForm()
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_allCategory')
    return render(request,'add_category.html',{'form':form})
