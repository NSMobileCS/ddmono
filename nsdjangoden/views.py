from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.text import slugify

from .models import FirstLady, President, RecipePost


def home(request):
    return render(request, "nsdjangoden/home.html", {})
# Create your views here.

def about(request):
    return render(request, 'nsdjangoden/about.html', {})

def index(request):
    # president_list = President.objects.all()
    # context = {'president_list':president_list}
    return render(request, 'nsdjangoden/index.html', {})

def voting(request, pres_id):
    pres = get_object_or_404(President, id=pres_id)
    context = {'pres_name':pres.pres_name,
               'presimg':pres.presimg,
               'pres_id':pres_id,
               'first_lady_set':pres.firstlady_set.all(),
               }
    return render(request, 'nsdjangoden/voting.html', context)

def vote(request, pres_id):
    p = get_object_or_404(President, id=pres_id)
    try:
        selected_lady = p.firstlady_set.get(pk=request.POST['choice'])
    except (KeyError, FirstLady.DoesNotExist):
        return HttpResponse("press back button. something's run afoul in the machine")
    else:
        selected_lady.votes += 1
        selected_lady.save()
        try:
            next_id = str(int(pres_id) + 1)
            np = President.objects.get(id=next_id)
            return HttpResponseRedirect('/firstladyswap/%s/voting' % next_id)
        except (KeyError, President.DoesNotExist):
            return HttpResponseRedirect('/firstladyswap/results/')



def detail(request, pres_id):
    pres = get_object_or_404(President, id=pres_id)
    context = {'pres_name':pres.pres_name,
               'presimg':pres.presimg,
               'realfirstlady':pres.realfirstlady,
               }
    return render(request, 'nsdjangoden/detail.html', context)


def all_results(request):
    pres_list = [i for i in President.objects.all()]
    context = {'pres_list':pres_list,
               }
    return render(request, 'nsdjangoden/allresults.html', context)

def results(request, pres_id):
    p = get_object_or_404(President, id=pres_id)
    # p = [i for i in President.objects.all() if int(i.id) == int(pres_id)][0]
    fl = [i for i in p.firstlady_set.all()]

    firstlady = FirstLady.objects.filter(lady_name=p.realfirstlady).first()
    flimg = firstlady.image
    # l = [i for i in FirstLady.objects.filter(lady_name=p.realfirstlady)]
    # flimg = l[0].image
    fl = sorted(fl, reverse=True, key=lambda x: int(x.votes))

    prev_pres, next_pres = None, None
    try:
        prev_pres = [i for i in President.objects.all() if int(i.id) == int(pres_id)-1][0]
    except IndexError:
        pass
    try:
        next_pres = [i for i in President.objects.all() if int(i.id) == int(pres_id)+1][0]
    except IndexError:
        pass

    context = {'pres':p,
               'flimg':flimg,
               'first_lady_list':fl,
               'prev_pres':prev_pres,
               'next_pres':next_pres,
               }
    return render(request, 'nsdjangoden/results.html', context)

def recipeindex(request):
    if request.method == 'POST':
        try:
            title = request.POST['title']
            dup = RecipePost.objects.filter(title=title)
            if dup:
                title += '(2)'

            rp = RecipePost(title=title,
                            urltitle = slugify(title),
                            ingredients=request.POST['ingredients'],
                            instructions=request.POST['instructions'],
                            )
            rp.save()
            return HttpResponseRedirect('/postrecipes/')
        except KeyError:
            context = {'recipes':RecipePost.objects.all(),
                       'warnings':'recipe error. please make sure you filled it in.'}
            return render(request, 'nsdjangoden/recipeindex.html', context)
    elif request.method == 'GET':
        recipes = [i for i in RecipePost.objects.all()]
        recipes = sorted(recipes, key=lambda x: x.title)
        context = {"recipes":recipes,
                   "warnings":None,
                   }
        return render(request, 'nsdjangoden/recipeindex.html', context)

def recipedetail(request, urltitle):
    recipe = get_object_or_404(RecipePost, urltitle=urltitle)
    context = {'recipe':recipe,
               }
    return render(request, 'nsdjangoden/recipedetail.html', context)




#    return render(request, 'templates/index.html')