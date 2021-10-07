# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView

from pdftw.api.models import Product
from pdftw.api.serializers import ProductSerializer


class ProductsView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects


class ProductView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects
