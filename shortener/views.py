from django.shortcuts import render
from django.http import  Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.db.models import F
from shortener.forms import AddSite
from shortener.models import ShortURL, LongURL
import random, string
import datetime


def add_site(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = AddSite(request.POST)
        if form.is_valid():

            flag = True
            while flag:
                key = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
                if not ShortURL.objects.filter(name = key).exists():
                    flag = False


            long_u = LongURL(name = request.POST['link'],ads = form.cleaned_data["advertiment"])
            long_u.save()
            if auth.get_user(request).id is not None:
                user = auth.get_user(request)
            else:
                user = None
            now = datetime.datetime.now()
            short_u = ShortURL(name = key, long_link = long_u , user =user, created_date=now)
            short_u.save()
            whole_short_u = request.META['HTTP_HOST'] +'/' + '%s' %(short_u)

            
            args['short_url'] = short_u
            args['whole_short_u'] = whole_short_u
            args['username'] = auth.get_user(request).username
            

            return render_to_response('show_short.html', args)

        if 'delete' in request.POST:
            for item in request.POST.getlist('choices'):
                short = ShortURL.objects.get(id=item)
                short.long_link.delete()
                short.delete()
            return HttpResponseRedirect('/')

    else:
        args['form'] = AddSite()
        args['username'] = auth.get_user(request).username
        args['short_urls_list'] = ShortURL.objects.filter(user=auth.get_user(request).id)
        args['host'] = request.META['HTTP_HOST']
        return render_to_response('add_site.html', args)

def open_short_url(request, key):
    
    if ShortURL.objects.filter(name = key).exists():

        long_url = ShortURL.objects.get(name = key).long_link
        number = ShortURL.objects.get(name = key)
        number.clicks = F('clicks') + 1
        number.save()

        if ShortURL.objects.get(name = key).long_link.ads == "Yes_Ads":
        	return render(request,'ads.html',{'url':long_url})
       	else:
			return HttpResponseRedirect(long_url)
    else:
        return render_to_response('wrong.html')


