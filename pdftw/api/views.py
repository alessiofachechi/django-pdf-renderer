# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from pdftw.api.models import Product
from pdftw.api.renderers import TemplatePDFRenderer
from pdftw.api.serializers import ProductSerializer


class ProductsView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects


class ProductView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects
    template_name = 'api/product.html'
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, TemplatePDFRenderer]

    def retrieve(self, request, pk, *args, format=None, **kwargs):
        response = super().retrieve(request, *args, **kwargs)

        if format == 'pdf':
            filename = f'product-{pk}.pdf'
            response['Content-Disposition'] = f'attachment; filename={filename}'

        return response
