
from django.db.models.functions import Greatest
from django.contrib.postgres.search import TrigramSimilarity
import re
from unittest import result
from django.db.models.manager import EmptyManager
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import PostShare, CommentForm, SearchForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
# Create your views here.
def post_search(request):
    form = SearchForm()
    query = None
    results=[]
    if 'query' in request.GET:
        form=SearchForm(request.GET)
        if form.is_valid():
            query=form.cleaned_data['query']
            results = Post.published.annotate(similarity=Greatest(TrigramSimilarity('title', query),TrigramSimilarity('content', query))).filter(similarity__gt=0.1).order_by('-similarity')
    return render(request, 'search.html',{'form':form,'query':query,'results':results})

def post_detail(request, post,year,month,day):
    post = get_object_or_404(Post, slug=post,publish__year=year,
                                   publish__month=month,
                                   publish__day=day, status='published')
    new_comment = None
    comments=post.comments.filter(active=True)
    if request.method=="POST":
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
            comment_form=CommentForm()
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]
    return render(request, 'post_detail.html', {'post': post,'comments':comments,"comment_form":comment_form,'new_comment': new_comment,'similar_posts':similar_posts})

def post_share(request, post_id):
    post=get_object_or_404(Post,id=post_id,status='published')
    sent=False
    post_url = request.build_absolute_uri(post.get_absolute_url())
    if request.method=="POST":
        form=PostShare(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            subj=f'{cd["name"]} ({cd["email"]}) chce, żebyś przeczytał post: {post.title}'
            content=f'Przeczytaj post "{post.title}", na stronie {post_url}\n\n Komentarz dodany przez {cd["name"]}: "{cd["comment"]}"'
            print(subj,content)
            send_mail(subj,content,'news.harc@gmail.com',[cd['to']],fail_silently=False)
            sent=True
    else:
        form=PostShare()
    return render(request,'share.html', {'post':post,'form':form,'sent':sent,'url':post_url})

def lista_postow(request, tag_slug=None):
    posts = Post.published.all()
    tag = None
    if tag_slug:
        tag=get_object_or_404(Tag, slug=tag_slug)
        posts=posts.filter(tags__in=[tag])
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'lista_postow.html', {'posts': posts, 'page':page,'tag':tag})
