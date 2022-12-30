from rest_framework import viewsets, mixins, parsers, status, serializers, response
from rest_framework.decorators import action
from .serializers import AccountBookSerializer, AccountDetailSerializer
from .models import AccountBook, Log


class AccountBookViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = AccountBook.objects.all()
    serializer_class = AccountBookSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)


class AccountDetailViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Log.objects.all()
    serializer_class = AccountDetailSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)

    def get_serializer_class(self):
        if self.action == "copy":
            return serializers.Serializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        user = request.user
        accountbook = user.accountbook
        self.queryset = Log.objects.filter(accountbook=accountbook)
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @action(methods=["post"], url_path="copy", url_name="copy", detail=True)
    def copy(self, request, *args, **kwargs):
        obj = self.get_object()
        Log.objects.create(
            accountbook=obj.accountbook, amount=obj.amount, type=obj.type, note=obj.note
        )
        return response.Response(status=status.HTTP_201_CREATED)
