from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_at")
    context = {"posts": posts}
    return render(request, "blog/post_list.html", context)

    html = """
    <html>
        <head>
            <meta charset="utf-8">
            <title>Учебный блог по Django</title>
        </head>
        <body>
            <h1>Блог по Django</h1>
		<ul>
		<li>Пост 1: Знакомство с курсом</li>
		<li>Пост 2: Как устроен наш учебный сайт</li>
		<li>Пост 3: Как сдавать практические работы</li>
		</ul>
	<p>
	<a href="/">На главную</a> | <a href="/about/">О проекте</a>
	</p>
	
	<p>Группа: Д-Э 311<br>Выполнила: Ерошенко Алиса
	</p>
	
        </body>
    </html>        
    """
    #context = {} +
    #return HttpResponse(html)
    #return render(request, "blog/post_list.html", context) +
    
def home(request):
    html = """
    <html>
        <head>
            <meta charset="utf-8">
            <title>Главная страница курса</title>
        </head>
        <body>
            <h1>Главная страница учебного сайта</h1>
            <p>Добро пожаловать на сайт курса. Здесь вы найдете блог и информацию о проекте.
            </p>

	<p>
	<a href="/blog/"> Перейти к блогу</a> | <a href="/about/">О проекте</a>
	</p>
	
	<p>Группа: Д-Э 311<br>Выполнила: Ерошенко Алиса<br>Цели курса:
	</p>
	
	<ul>
	<li>Попробовать себя в моделировании приложений</li>
	<li>Поработать с вебом</li>
	<li>Понять на практике как связана база данных и внутреннаяя часть приложения</li>
	</ul>
	
        </body>
    </html>        
    """
    context = {}
    #return HttpResponse(html)
    return render(request, "blog/home.html", context)
    
    
def about(request):
    html = """
    <html>
    	<head>
    	    <meta charset="utf-8">
    	    <title>О проекте</title>
    	</head>
    	<body>
            <h1>О проекте</h1>
            <p>Этот сайт создан в рамках учебного курса по Django.</p>
            <p>На сайте есть блог и другие разделы, которые мы будем разрабатывать по мере прохождения курса.</p>
            <p>
            	<a href="/">На главную<a> | <a href="/blog/">К блогу<a>
            </p>
            
            <p>Группа: Д-Э 311<br>Выполнила: Ерошенко Алиса<br>Дальнейшее развитие сайта:
	    </p>
	    <p>В рамках данного курса на сайте планируются введение улучшений, таких как добавление системы авторизации, разлиные формы для ввода данных пользователем, а также модели. Безусловно, далее также будут проведены работы по улучению базы данных и внешнего вида сайта. Будет усложена логика веб-приложения.
	    </p>
	
    	</body>
    </html>
    """
    context = {}
    #return HttpResponse(html)
    return render(request, "blog/about.html")
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    similar_posts = Post.objects.filter( created_at__date = post.created_at.date()).exclude(pk=post.pk)[:3]
    context = {"post": post, "similar_posts": similar_posts}
    return render(request, "blog/post_detail.html", context)
    








