from django.shortcuts import render
from .models import Product,Contact, Orders, OrderUpdate
from math import ceil
from django.http import HttpResponse
import json
# from django.views.decorators.csrf import csrf_exempt
# from PayTm import Checksum
MERCHANT_KEY = 'YHyjGRMTPEtLwplL'
def index(request):
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact  = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

        submitted = True
        return render(request, "shop/contact.html",{'submitted': submitted})
    return render(request, "shop/contact.html")

def tracker(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].item_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse(e)

    return render(request, "shop/tracker.html")

def search(request):
    return render(request, "shop/search.html")

def products(request,myid):
    #viewing the products using id
    product = Product.objects.filter(id=myid)
    return render(request, "shop/productview.html", {'product': product[0]})

def checkout(request):
    if request.method  == 'POST':
        item_json = request.POST.get('itemsjson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '')+ ' ' + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(item_json=item_json, amount=amount, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)

        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed.")
        update.save()
        thank = True
        id = order.order_id
        return render(request, "shop/checkout.html", {'thanks': thank, 'id' : id})
        #paythm payment request
        # param_dict={
        #
        #     "MID": "rxazcv89315285244163",
        #     "ORDER_ID": str(order.order_id),
        #     "CUST_ID": email,
        #     "TXN_AMOUNT": str(amount),
        #     "CHANNEL_ID": "WEBSTAGING",
        #     "INDUSTRY_TYPE_ID": "Retail",
        #     "WEBSITE": "http://127.0.0.1:8000/shop/handlerequest/",
        #     "CHECKSUMHASH":"CsTeIGhOnegWColuGQaGphMizcsECToTPZ9x/oFPrNZk1TaiV2bFJZzfCwlU7/7ZDbDZIdIfCXfrNjNlFmoUjOMmg8tlR4/0gakLfFNIe2c="
        # }
        #
        # return render(request, "shop/paytm.html",{'param_dict':param_dict})
    return render(request, "shop/checkout.html")


# @csrf_exempt
# def handlerequest(request):
#     return HttpResponse('done')
#     pass