from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from .filters import CustomPackageFilter
from .models import Package, PackageType
from .serializers import PackageSerializer, PackageTypeSerializer


class PackagePagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PackageListCreateAPIView(ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    pagination_class = PackagePagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CustomPackageFilter

    def perform_create(self, serializer):
        # получение текущей сессии пользователя
        session_key = self.request.session.session_key

        # создание новой сессии, если у пользователя её нет
        if not session_key:
            self.request.session.save()
            session_key = self.request.session.session_key

        serializer.save(user_session=session_key)

    def get_queryset(self):
        session_key = self.request.session.session_key
        return Package.objects.select_related('type').filter(user_session=session_key)


class PackageDetailAPIView(RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    def get_object(self):
        obj = super().get_object()
        if obj.user_session != self.request.session.session_key:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Эта посылка не принадлежит вам.")
        return obj


class PackageTypeAPIView(ListAPIView):
    serializer_class = PackageTypeSerializer
    queryset = PackageType.objects.all()
