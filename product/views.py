from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from product.models import Shoes, Category, Confirm
from product.forms import ShoesForm
from django.shortcuts import get_object_or_404
#from decimal import Decimal


class ProductListView(ListView):
    model = Shoes
    fields = '__all__'
    context_object_name = 'shoes'
    template_name = 'product_list.html'

    def __init__(self, url=None):
        self.url = url

    def get_queryset(self):
        return Shoes.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     shoe = self.get_object()
    #     shoesList = []
    #     for item in shoe:
    #         price_decimal = Decimal(str(item.price))
    #         discount_decimal = Decimal(str(item.discount))
    #         discounted_price = price_decimal * (1 - discount_decimal / 100)
    #         item.price = {'price': price_decimal, 'sale': str(round(discounted_price))}
    #         shoesList.append(item)
    #         # print(shoesList)
    #     context['shoesList'] = shoesList
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Выбираем все товары
        show_products = Shoes.objects.all()[:12]
        context['show_products'] = show_products

        # Выбираем только товары у которых есть скидка
        discounted_products = Shoes.objects.filter(discount__gt=0, available=True)[:9]
        context['discounted_products'] = discounted_products

        return context

    # def get_products(self):
    #     category = None
    #     categories = Category.objects.all()
    #     shoes = Shoes.objects.filter(available=True)
    #
    #     if self.url:
    #         category = get_object_or_404(Category, url=self.url)
    #         shoes = shoes.filter(category=category)
    #         return {
    #             'category': category,
    #             'categories': categories,
    #             'shoes': shoes
    #         }

class ProductByCategoryListView(ListView):
    model = Shoes
    template_name = 'product_list.html'
    context_object_name = 'shoes'
    category = None

    def get_queryset(self):
        self.category = Category.objects.get(url=self.kwargs['url'])
        queryset = Shoes.objects.all().filter(category__url=self.category.url)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = f'Статьи из категории: {self.object.category.name}'
        return context

    # def get_queryset(self):
    #     queryset = Shoes.objects.filter(
    #         category__in=self.request.GET.getlist('category'),
    #         gender__in=self.request.GET.getlist('gender'),
    #         size__in=self.request.GET.getlist('size'),
    #         country_of_manufacture__in=self.request.GET.getlist('country_of_manufacture'),
    #         price__in=self.request.GET.getlist('price'),
    #         discount__in=self.request.GET.getlist('discount'),
    #         collection__in=self.request.GET.getlist('collection'),
    #         upper_material__in=self.request.GET.getlist('upper_material'),
    #         lining_material__in=self.request.GET.getlist('lining_material'),
    #         outsole_material__in=self.request.GET.getlist('outsole_material'),
    #         insole_material__in=self.request.GET.getlist('insole_material')
    #     )
    #     return queryset

class ProductDetailView(DetailView):
    model = Shoes
    # context_object_name = 'shoe'
    template_name = 'product_detail.html'


    # def __init__(self, id, url, *args, **kwargs):
    #     self.id = id
    #     self.url = url
    #     super().__init__(*args, **kwargs)
    #
    # def get(self, request):
    #     shoes = Shoes.objects.get(id=self.id)
    #     context = {
    #         'shoes': shoes,
    #         'url': self.url
    #     }
    #     return render(request, 'product_detail.html', context)

    def get_queryset(self):
        return Shoes.objects.all()

    def get_object(self, queryset=None):
        slug = self.kwargs.get('url')  # Используйте 'url' вместо 'slug'
        product_id = self.kwargs.get('id')  # Используйте 'id' вместо 'product_id'
        #print(product_id, slug)
        try:
            return get_object_or_404(Shoes, url=slug, id=product_id)
        except Shoes.DoesNotExist:
            raise Http404("Product does not exist")

    # def get_object(self):
    #     product_id = self.kwargs.get('product_id')
    #     try:
    #         return Shoes.objects.get(pk=product_id)
    #     except Shoes.DoesNotExist:
    #         raise Http404("Product does not exist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shoe = self.get_object()
        context['gender'] = shoe.gender.all()
        context['colors'] = shoe.color.all()
        context['sizes'] = shoe.size.all()
        context['collections'] = shoe.collection.all()
        context['upper_material'] = shoe.upper_material.all()
        context['lining_material'] = shoe.lining_material.all()
        context['outsole_material'] = shoe.outsole_material.all()
        context['insole_material'] = shoe.insole_material.all()

        # Выбираем только товары у которых есть скидка
        discounted_products = Shoes.objects.filter(discount__gt=0, available=True)[:9]
        context['discounted_products'] = discounted_products

        # price_decimal = Decimal(str(shoe.price))
        # discount_decimal = Decimal(str(shoe.discount))
        # discounted_price = price_decimal * (1 - discount_decimal / 100)
        # context['discounted_price'] = str(round(discounted_price))
        return context


class ProductCreateView(CreateView):
    model = Shoes
    form_class = ShoesForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoes'] = Shoes.objects.all()
        return context

class ProductDeleteView(DeleteView):
    model = Shoes
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def get_object(self, queryset=None):
        product_id = self.kwargs.get('product_id')
        return Shoes.objects.get(id=product_id)


class ConfirmView(DetailView):
    model = Confirm
    fields = '__all__'
    template_name = 'product_confirm.html'

    def get_queryset(self):
        return Shoes.objects.all()

    def get_object(self, queryset=None):
        product_id = self.kwargs.get('product_id')
        try:
            return Confirm.objects.get(id=product_id)
        except Confirm.DoesNotExist:
            product_id = None