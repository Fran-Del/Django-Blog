from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail

from .forms import ContactForm, CommentForm
from .models import BlogPost


def index(request):
    """ The home page for the blog. """
    return render(request, 'blogs/index.html')


def post_list(request):
    """ Displays all  blog posts """
    post_list = BlogPost.objects.all()
    # Show 1 post per Page
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}
    return render(request, 'blogs/post_list.html', context)


def post(request, post_id):
    """ Show a single blog post and all it's comments """
    post = BlogPost.objects.get(id=post_id)
    comments = post.comment_set.order_by('-date_added')

    new_comment = None
    if request.method != 'POST':
        comment_form = CommentForm()

    else:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # create a comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # assigning the current post to the comment
            new_comment.post = post
            # saving comment to database
            new_comment.save()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }



    #context = {'post': post, 'comments': comments}
    return render(request, 'blogs/post.html', context)


def about(request):
    """ shows the about page """
    return render(request, 'blogs/about.html')


def contact(request):
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = ContactForm()
    else:
        # POST data submitted; process data.
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            send_mail(
                form.cleaned_data['name'],
                form.cleaned_data['message'],
                form.cleaned_data['senders_email'],
                ["tchoffofrandel@gmail.com"],
                fail_silently=False,
            )
            return render(request, 'blogs/contact_success.html')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/contact.html', context)


def add_comment_to_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method != 'POST':
        comment_form = CommentForm()

    else:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # create a comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # assigning the current post to the comment
            new_comment.post = post
            # saving comment to database
            new_comment.save()
    context = {'new_comment':new_comment, 'comment_form':comment_form}

    return render(request, 'blogs/post.html', context)


