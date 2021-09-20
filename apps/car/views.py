from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView

from rest_framework import filters as df

from .paginations import SmallResultsSetPagination
from .models import Brand
from .serializer import BrandSerializer


class BrandListView(ListAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    pagination_class = SmallResultsSetPagination
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
    search_fields = ('name', )
    ordering_fields = ('name', )


class BrandCreateView(CreateAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()


class BrandRetrieveView(RetrieveAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    lookup_field = 'id'


class BrandUpdateView(UpdateAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    lookup_field = 'id'


class BrandDestroyView(DestroyAPIView):
    permission_classes = ()
    queryset = Brand.objects.all()
    lookup_field = 'id'
