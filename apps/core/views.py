from apps.core.models import Color
from .serializers import ColorSerializer
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, GenericViewSet


class OptionalPaginationMixin():
    def paginate_queryset(self, queryset):
        if self.request.GET and 'skip_pagination' in self.request.GET:
            return None
        else:
            return super().paginate_queryset(queryset)


class FilteredViewSet(GenericViewSet):
    filter_backends = (filters.OrderingFilter,
                       filters.DjangoFilterBackend,
                       filters.SearchFilter)
    ordering_fields = '__all__'
    filter_fields = '__all__'
    search_fields = '__all__'

    class Meta(object):
        abstract = True


class ColorViewSet(OptionalPaginationMixin, FilteredViewSet, ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    filter_fields = {
        'id': ('exact',),
        'name': ('exact', 'icontains', 'startswith', 'endswith'),
    }
    search_fields = ('id', 'name')
