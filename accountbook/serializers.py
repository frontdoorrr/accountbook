from rest_framework import serializers
from .models import AccountBook, Log


class AccountBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBook
        fields = ("__all__",)


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = (
            "amount",
            "type",
            "note",
        )
        read_only_fields = ("accountbook",)

    def create(self, validated_data):
        user = self.context["request"].user
        accountbook = user.accountbook
        validated_data["accountbook"] = accountbook
        return super().create(validated_data)
