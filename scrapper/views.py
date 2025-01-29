from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .services import scrape_mercado_libre, FiltroArticulos
from rest_framework import viewsets
from .models import Articulo
from .serializers import ArticuloSerializer
from .services import scrape_mercado_libre, FiltroArticulos

class SearchView(View):
    def get(self, request):
        search_term = request.GET.get('query', '')
        if not search_term:
            return JsonResponse({'error': 'No search term provided'}, status=400)
        
        products = scrape_mercado_libre(search_term)
        suggest = FiltroArticulos(products)
        response_data = {
            'products': products,
            'suggest': suggest
        }
        return JsonResponse(response_data, safe=False)
    

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer