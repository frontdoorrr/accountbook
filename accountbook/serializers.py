from rest_framework import serializers
from .models import AccountBook, Log


class AccountBookSerializer(serializers.ModelSerializer):
    total_amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = AccountBook
        fields = (
            "id",
            "user",
            "name",
            "total_amount",
            "logs",
        )


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = (
            "id",
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
