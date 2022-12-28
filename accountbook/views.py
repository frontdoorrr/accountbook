from django.shortcuts import render
from rest_framework import viewsets, mixins, parsers
from .serializers import AccountBookSerializer, AccountDetailSerializer
from .models import AccountBook, Log

# Create your views here.


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

    def list(self, request, *args, **kwargs):
        user = request.user
        accountbook = user.accountbook
        self.queryset = Log.objects.filter(accountbook=accountbook)
        return super().list(request, *args, **kwargs)
