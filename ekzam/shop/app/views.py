from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import *
from .forms import *


class MainList(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'app/main.html'

    def get_queryset(self):
        return Product.objects.all()[:5]


@login_required
def profile(request):
    order = Order.objects.filter(user=request.user)

    context = {
        "orders": order,
    }

    return render(request, 'app/profile.html', context)


class ServiceList(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'app/services.html'

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        if query:
            return Product.objects.filter(name__icontains=query)
        else:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context



def service_detail(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.product_id = id
            instance.save()
    else:
        form = OrderForm(initial={'user': request.user.pk, 'product': id})

    return render(request, "app/service_detail.html", {'product': product, 'form': form})


class RegisterView(generic.CreateView):
    model = AdvUser
    form_class = RegisterForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')

