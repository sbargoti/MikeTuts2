from django.shortcuts import render_to_response
from article.models import Article
from article.forms import ArticleForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.
def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'
    
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
        
    if 'lang' in request.session:
        session_language = request.session['lang']
        
    args = {}
    args.update(csrf(request))
    
    args['articles'] = Article.objects.all()
    args['language'] = language   
    args['session_language'] = session_language 
    
    return render_to_response('articles.html', args)

def article(request,article_id=1):
    return render_to_response('article.html',
                              {'article': Article.objects.get(id=article_id) })
                              
def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)
    
    response.set_cookie('lang', language) 
    
    request.session['lang'] = language
    return response

def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('create_article.html',args)
    
def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
        
    return HttpResponseRedirect('/articles/get/%s' % article_id)

def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
        
    articles = Article.objects.filter(title__contains=search_text)
    return render_to_response('ajax_search.html', {'articles' : articles})
    
#    articles = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))            
#    
#    return render_to_response('ajax_search.html', {'articles' : articles})
    
########### FROM TUTORIAL 3 ###########
#def hello(request):
#    name = "Annie"
#    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
#    return HttpResponse(html)
#    
#def hello_template(request):
#    name = "Annie"
#    t = get_template('hello.html')
#    html = t.render(Context({'name': name}))
#    return HttpResponse(html)
#
#def hello_template_simple(request):
#    name = "Suchet"
#    return render_to_response('hello.html', {'name': name})
#    
#class HelloTemplate(TemplateView):
#    template_name = 'hello_class.html'
#    
#    def get_context_data(self, **kwargs):
#        context = super(HelloTemplate,self).get_context_data(**kwargs)
#        context['name'] = 'Suchet'
#        return context
#        
########### END TUTORIAL 3 ###########
