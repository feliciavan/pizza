from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("pizza", views.pizza_view, name="pizza"),
    path("subs", views.subs_view, name="subs"),
    path("pasta", views.pasta_view, name="pasta"),
    path("salads", views.salads_view, name="salads"),
    path("dinner", views.dinner_view, name="dinner"),
    path("order", views.order_view, name="order"),
    path("cart", views.cart_view, name="cart"),
    path("placed", views.placed_view, name="placed"),
    path("complete", views.complete_view, name="complete"),
    path("posts", views.posts, name="posts"),
]
