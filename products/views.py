from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
   
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "id"


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category", "owner").all().order_by("-created_at")
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "category__name"]  # partial match supported by DRF SearchFilter
    filterset_fields = ["category"]             # filter by category id
    ordering_fields = ["price", "created_at", "stock_quantity"]

    def get_queryset(self):

        qs = super().get_queryset()
        params = self.request.query_params

        min_price = params.get("min_price")
        max_price = params.get("max_price")
        in_stock = params.get("in_stock")

        if min_price is not None:
            try:
                qs = qs.filter(price__gte=min_price)
            except ValueError:
                pass

        if max_price is not None:
            try:
                qs = qs.filter(price__lte=max_price)
            except ValueError:
                pass

        if in_stock is not None:
            val = in_stock.strip().lower()
            if val in ["true", "1", "yes"]:
                qs = qs.filter(stock_quantity__gt=0)
            elif val in ["false", "0", "no"]:
                qs = qs.filter(stock_quantity=0)

        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



