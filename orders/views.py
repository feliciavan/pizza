from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Pizza, PizzaPrice, PizzaTopping, Salads, DinnerPlatters
from .models import DinnerPlattersPrice, Pasta, Subs, SubsPrice, SubsSteak
from .models import SubsSteakPrice, Order

num_order = 0
p = {}
order = {}
toppings = 0
# Create your views here.
@ensure_csrf_cookie
def index(request):
    global num_order
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    try:
        num_order = len(Order.objects.filter(user=request.user))
    except:
        num_order = 0
    context = {
        "user": request.user,
        "toppings": PizzaTopping.objects.all(),
        "num_order": num_order,
    }
    return render(request, "orders/pizza.html", context)

def login_view(request):
    global num_order
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_staff == True:
            context = {
                "order": Order.objects.all(),
            }
            return render(request, "orders/boss.html", context)
        else:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def signup_view(request):
    try:
        name = request.POST["name"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        user = authenticate(username=name, password=password)
        if user is not None:
            return render(request, "orders/signup.html", {"message": "Existing user name."})
        new_user = User.objects.create_user(name, email, password)
        new_user.active = True
        new_user.first_name = firstname
        new_user.last_name = lastname
        new_user.save()
        login(request, new_user)
        return HttpResponseRedirect(reverse("index"))
    except:
        return render(request, "orders/signup.html", {"message": None})

def pizza_view(request):
    global num_order
    global p
    global toppings
    try:
        num_order = len(Order.objects.filter(user=request.user))
    except:
        num_order = 0
    if request.method == "POST":
        context = {
            "toppings": PizzaTopping.objects.all(),
            "num_order":  num_order,
        }
        type = request.POST.getlist('type[]')
        if not type:
            context.update( {"message": "You have to choose one type."})
            return render(request, "orders/pizza.html", context)
        else:
            if len(type) > 1:
                context.update( {"message": "One type at one time."} )
                return render(request, "orders/pizza.html", context)
            else:
                type_res = type[0]

        size = request.POST.getlist('size[]')
        if len(size) > 1:
            context.update( {"message": "One size at one time."} )
            return render(request, "orders/pizza.html", context)
        if not size:
            context.update( {"message": "You have to choose one size."})
            return render(request, "orders/pizza.html", context)
        size_res = size[0]
        flavor = request.POST.getlist('flavor[]')
        if not flavor:
            context.update( {"message": "You have to choose one flavor."})
            return render(request, "orders/pizza.html", context)
        if len(flavor) > 1:
            context.update({"message": "One flavor at one time."})
            return render(request, "orders/pizza.html", context)
        if flavor[0] == "toppings":
            top = request.POST.getlist('top[]')
            if len(top) > 3:
                context.update({"message": "3 toppings at most."})
                return render(request, "orders/pizza.html", context)
            elif not top:
                context.update({"message": "You have to choose one topping."})
                return render(request, "orders/pizza.html", context)
            else:
                top_res = len(top)
                toppings = top
                boo_res = False
        else:
            top = request.POST.getlist('top[]')
            if top:
                context.update({"message": "You can not choose toppings with " + flavor[0] + " pizza."})
                toppings = 0
                return render(request, "orders/pizza.html", context)
            else:
                top_res = 0
                toppings = 0
                if flavor[0] == "cheese":
                    boo_res = False
                else:
                    boo_res = True
        p = PizzaPrice.objects.get(kind__size=size_res, kind__kind=type_res, kind__num_toppings=top_res, kind__speical=boo_res)
        context.update({"price": p.price})
        return render(request, "orders/pizza.html", context)
    else:
        context = {
            "toppings": PizzaTopping.objects.all(),
            "num_order":  num_order,
        }
        return render(request, "orders/pizza.html", context)

def subs_view(request):
    global num_order
    global p
    global toppings
    toppings = 0
    if request.method == "POST":
        context = {
            "subs": Subs.objects.filter(size="small", extracheese=True),
            "steaks": SubsSteak.objects.filter(size="small", extracheese=True),
            "num_order":  num_order,
        }
        sub = request.POST.getlist('sub[]')
        if len(sub) > 1:
            context.update( {"message": "One type at one time."} )
            return render(request, "orders/subs.html", context)
        if not sub:
            context.update( {"message": "You have to choose one type."})
            return render(request, "orders/subs.html", context)
        sub_res = sub[0]
        size = request.POST.getlist('size[]')
        if len(size) > 1:
            context.update( {"message": "One size at one time."} )
            return render(request, "orders/subs.html", context)
        if not size:
            context.update( {"message": "You have to choose one size."})
            return render(request, "orders/subs.html", context)
        size_res = size[0]
        extra = request.POST.getlist('extra[]')
        if len(extra) > 1:
            context.update( {"message": "You can not choose yes and no at the same time."} )
            return render(request, "orders/subs.html", context)
        if not extra:
            context.update( {"message": "Do you need extra cheese?"})
            return render(request, "orders/subs.html", context)
        if extra[0] == "yes":
            extra_res = True
        else:
            extra_res = False

        addon = request.POST.getlist('addon[]')
        if sub_res == "steak":
            if len(addon) > 1:
                context.update( {"message": "One add-on at one time."} )
                return render(request, "orders/subs.html", context)
            if not addon:
                p = SubsPrice.objects.get(kind__kind=sub_res, kind__size=size_res, kind__extracheese=extra_res)
                context.update({"price": p.price})
                return render(request, "orders/subs.html", context)
            add = addon[0]
            p = SubsSteakPrice.objects.get(kind__addonkind=add, kind__size=size_res, kind__extracheese=extra_res)
            context.update({"price": p.price})
            return render(request, "orders/subs.html", context)
        else:
            if addon:
                context.update( {"message": "No add-on is allowed."} )
                return render(request, "orders/subs.html", context)
            else:
                p = SubsPrice.objects.get(kind__kind=sub_res, kind__size=size_res, kind__extracheese=extra_res)
                context.update( {"price": p.price})
                return render(request, "orders/subs.html", context)
    else:
        context = {
            "subs": Subs.objects.filter(size="small", extracheese=True),
            "steaks": SubsSteak.objects.filter(size="small", extracheese=True),
            "num_order":  num_order,
        }
        return render(request, "orders/subs.html", context)

def pasta_view(request):
    global num_order
    global p
    global toppings
    toppings = 0
    if request.method == "POST":
        context = {
            "pastas": Pasta.objects.all(),
        }
        apasta = request.POST.getlist('pasta[]')
        if apasta:
            num_order = int(num_order) + int(len(apasta));
            context.update({"num_order": num_order})
            for ap in apasta:
                p = Pasta.objects.get(kind=ap)
                Order.objects.create(user=request.user, product=p.kind, price=p.price)
            return render(request, "orders/pasta.html", context)
        else:
            context.update({"num_order": num_order})
            context.update({"message": "You have not chosen yet."})
            return render(request, "orders/pasta.html", context)
    else:
        context = {
            "pastas": Pasta.objects.all(),
            "num_order":  num_order,
        }
        return render(request, "orders/pasta.html", context)

def salads_view(request):
    global num_order
    global p
    global toppings
    toppings = 0
    if request.method == "POST":
        context = {
            "salads": Salads.objects.all(),
        }
        salad = request.POST.getlist('salad[]')
        if salad:
            num_order = num_order + int(len(salad));
            context.update({"num_order": num_order})
            for sa in salad:
                p = Salads.objects.get(kind=sa)
                Order.objects.create(user=request.user, product=p.kind, price=p.price)
            return render(request, "orders/salads.html", context)
        else:
            context.update({"num_order": num_order})
            context.update({"message": "You have not chosen yet."})
            return render(request, "orders/salads.html", context)
    else:
        context = {
            "salads": Salads.objects.all(),
            "num_order":  num_order,
        }
        return render(request, "orders/salads.html", context)

def dinner_view(request):
    global num_order
    global p
    global toppings
    toppings = 0
    if request.method == "POST":
        context = {
            "dinners": DinnerPlatters.objects.filter(size="small"),
            "num_order":  num_order,
        }
        dinner = request.POST.getlist('dinner[]')
        if len(dinner) > 1:
            context.update( {"message": "One type at one time."} )
            return render(request, "orders/dinner.html", context)
        if not dinner:
            context.update( {"message": "You have to choose one type."})
            return render(request, "orders/dinner.html", context)
        dinner_res = dinner[0]
        size = request.POST.getlist('size[]')
        if len(size) > 1:
            context.update( {"message": "One size at one time."} )
            return render(request, "orders/dinner.html", context)
        if not size:
            context.update( {"message": "You have to choose one size."})
            return render(request, "orders/dinner.html", context)
        size_res = size[0]
        p = DinnerPlattersPrice.objects.get(kind__kind=dinner_res, kind__size=size_res)
        context.update({"price": p.price})
        return render(request, "orders/dinner.html", context)
    else:
        context = {
            "dinners": DinnerPlatters.objects.filter(size="small"),
            "num_order":  num_order,
        }
        return render(request, "orders/dinner.html", context)

def order_view(request):
    global num_order
    global p
    global toppings
    num_order = request.POST["num_order"]
    Order.objects.create(user=request.user, product=p.kind, price=p.price, toppings=toppings)
    return JsonResponse({"num_order": num_order})

def cart_view(request):
    orders = Order.objects.filter(user=request.user)
    price = 0
    for order in orders:
        if order.status == "unplaced":
            price = price + order.price

    context = {
        "order": orders,
        "price": round(price,2),
    }
    return render(request, "orders/cart.html", context)

def placed_view(request):
    global num_order
    try:
        orders = Order.objects.filter(user=request.user)
        num_order = len(orders)
        for order in orders:
            order.status = "placed"
            order.save()

    except:
        num_order = 0
    context = {
        "order": orders,
        "message": "Thank you! Your order is placed."
    }
    return render(request, "orders/cart.html", context)

def complete_view(request):
    user = request.POST["user"]
    product = request.POST["product"]
    com = Order.objects.get(user=user,product=product)
    com.status = "completed"
    com.save()
    return HttpResponse("done")
