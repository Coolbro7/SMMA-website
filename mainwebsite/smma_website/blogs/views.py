from django.shortcuts import render, HttpResponse
from blogs.models import Post,comment,category
from .form import *



# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts":posts,
    }
    return render(request,"blog/blog_index.html",context)

def blog_category(request,category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by("-created_on")
    context = {
        "category":category,
        "posts":posts,
    }
    return render(request,"blog/category.html",context)

def detail(request,pk,slug):
    def create_related_post_query():
        '''
        this function creates a queryset of similar posts to the current post.it creates 2 empty queryset and
        then fills one with the related posts on the basis of categories and since the categories bring the same 
        posts multiple time so the next empty querset filters only the unique onces and discards the repeated ones
        '''
        related_post = Post.objects.none()
        final_related_post = Post.objects.none() 
        for category in post.categories.all():
            related_post = related_post | Post.objects.filter(
            categories__name__contains = category
        ).order_by("-created_on")
        for rpost in related_post:
            if Post.objects.filter(title = rpost) not in final_related_post:
                final_related_post = final_related_post | Post.objects.filter(title= rpost).order_by("-created_on")
        final = final_related_post[:6]
        return final
    

    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        posted_comment = request.POST.get("comment")
        if len(posted_comment) > 0:
            new_comment = comment(author = "Annonomous User",body=posted_comment,post=post)
            new_comment.save()
    comments = comment.objects.filter(post=post)
    title = post.title
    similar_post = create_related_post_query()


    context = {
        "post": post,
        "comments":comments,
        "related_posts":similar_post,
        "current_title":title,
    }
    return render(request,"blog/details.html",context)

def post_blog(request):
    
    def make_list(categories):
        '''this function make a list from the input it gets from the categories field'''
        final = categories.split(",")
        return final

    def add_categories(post,list_of_categories):
        '''
    this function add categories to the new articles. loops through all the categories in the list and tries to add the categories 
    from the existing database by comparing the value from input to that of database and if it exists it adds the same or else it creates a new
    one and adds it
        '''
        for cat in list_of_categories:
            
            try:
                p1 = category.objects.filter(name=cat).values()
                post.categories.add(p1[0]["id"])
            except Exception as e:
                post.categories.create(name=cat)

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.POST.get("author")
        list_of_categories = make_list(request.POST.get("category"))
        new_post = Post(title=title,author=author,body=content)
        new_post.save()
        add_categories(new_post,list_of_categories)
    return render(request,"blog/create.html")

