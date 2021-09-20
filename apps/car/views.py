from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Brand
from .serializer import BrandSerializer


class BrandListView(ListAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()


class BrandCreateView(CreateAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()