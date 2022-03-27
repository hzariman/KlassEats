from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FoodItem, Order, OrderItem
from user.models import User
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
# Create your views here.


def home (request):
    return render(request, 'canteen/home.html')

def dashboard_view(request):
    current_user = request.user
    if current_user.is_student == True:
        orders = Order.objects.filter(customer = current_user)
    elif current_user.is_staff == True:
        orders = Order.objects.filter(is_completed = False, deliver_by = 1)
    else:
        return redirect ('canteen:menu')
    
    context = {
        'orders' : orders
    }

    return render(request, 'canteen/dashboard.html', context)


class food_menu(ListView):
    model = FoodItem
    foodlist = FoodItem.objects.all()
    template_name = 'canteen/menu.html'
    context_object_name = 'foodlist'


class food_item_create(LoginRequiredMixin, CreateView):
    model = FoodItem
    fields = ['name','price','description']
    template_name = 'staff/create_item.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Food Item created")
        return 'menu'

class food_item_modify(LoginRequiredMixin, UpdateView):
    model = FoodItem
    fields = ['name', 'price', 'description']
    template_name = 'staff/modify_item.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Food Item created")
        return 'menu'

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order/order_details.html'

class food_item_delete (LoginRequiredMixin, DeleteView):
    model = FoodItem
    template_name = 'staff/delete_item.html'

    def get_success_url(self):
        messages.success(self.request, "Food Item Deleted")
        return reverse('canteen:menu')

class CreateOrder(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['order_items']
    template_name = 'order/create_order.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Your order has been created")
        return reverse('canteen:dashboard')
    

def add_to_cart(request, **kwargs):
    item = get_object_or_404(FoodItem, id = kwargs.get('pk'))
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
    )
    order_qs = Order.objects.filter(customer=request.user, is_completed=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.order_items.filter(id=kwargs.get('pk')).exists():
            order_item.quantity += 1
            order_item.get_total_item_price()
            order_item.save()
            order.total_sum()
            order.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("canteen:dashboard")
        else:
            order.order_items.add(order_item)
            order_item.get_total_item_price()
            order_item.save()
            order.total_sum()
            order.save()
            messages.info(request, "This item was added to your cart :( .")
            return redirect("canteen:dashboard")
    else:
        order = Order.objects.create(
            customer=request.user)
        order.order_items.add(order_item)
        order_item.get_total_item_price()
        order_item.save()
        order.total_sum()
        order.save()        
        messages.info(request, "This item was added to your cart :).")
        return redirect("canteen:dashboard")


            







