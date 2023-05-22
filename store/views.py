from django.shortcuts import render , redirect
from django.contrib import messages
# from . models import *
from django.http import JsonResponse
from . models import Product , Category , Whatsapp
# Create your views here.
# from . models import Category
# slug, name, descrption, status, trending, meta_tilte, meta_keyword, meta_description, create_at, update_at, category, small_descrption, quantity, original_price, selling_price, tags)

def index(reqeust):
    trending_product = Product.objects.filter(trending=1)
    whatsapp = Whatsapp.objects.all().first()
    
    # url = Produc.objects.get()
    
    # context = {"trending_product": trending_product, "whatsapp": whatsapp,"url":url}
    context = {"trending_product": trending_product, "whatsapp": whatsapp}
    return render(reqeust, 'store/index.html',context)


def collections(reqeust):
    category = Category.objects.filter(status=0)
    context = {'category' : category, }
    return render(reqeust, 'store/collections.html', context)


def collectionsview(reqeust, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products,'category':category,}
        return render(reqeust, 'store/products/index.html', context) 
    else:
        messages.warning(reqeust, 'No Such Category Found')
        return redirct('collections')
def productview(reqeust, cat_slug, prod_slug):
    if (Category.objects.filter(slug=cat_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products':products}
        else:
            messages.error(reqeust, 'No Such Product Found ')
            return redirct('collections')
  
    else:
        messages.error(reqeust, 'No Such Category Found ')
        return redirct('collections')

    return render(reqeust, 'store/products/single.html', context) 


def productlist(reqeust):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productList = list(products)
    return JsonResponse(productList, safe=False)



def searchproduct(reqeust):
    if reqeust.method == 'POST':
        searchitem = reqeust.POST.get('productsearch')
        if searchitem  == "":
            return redirect(reqeust.META.get("HTTP_REFERER"))
        else:
          product = Product.objects.filter(name__contains=searchitem).first()
          if product:
              return redirect('collections/'+product.category.slug+'/'+product.slug+' ')
          else:
              messages.info(reqeust, 'No Found Matched Your Search')
              return redirect(reqeust.META.get("HTTP_REFERER"))
    else:
        return redirect(reqeust.META.get('HTTP_REFERER'))
    
# http://127.0.0.1:8000/collections/quran/hamzoooz
# http://127.0.0.1:8000/collections/quran/hamzoooz%20