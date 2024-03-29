from django.db import models
from core.models import Core


class AccountBook(Core):
    user = models.OneToOneField(
        "user.User", on_delete=models.CASCADE, related_name="accountbook"
    )
    name = models.CharField(max_length=300)

    @property
    def total_amount(self):
        income = Log.objects.filter(accountbook_id=self.id, type="income").aggregate(
            models.Sum("amount")
        )
        expenditure = Log.objects.filter(
            accountbook_id=self.id, type="expenditure"
        ).aggregate(models.Sum("amount"))
        return income["amount__sum"] - expenditure["amount__sum"]


class Log(Core):
    accountbook = models.ForeignKey(
        "accountbook.AccountBook",
        on_delete=models.CASCADE,
        related_name="logs",
    )
    amount = models.IntegerField()

    INCOME = "income"
    EXPENDITURE = "expenditure"
    TYPE_CHOICES = ((INCOME, INCOME), (EXPENDITURE, EXPENDITURE))

    type = models.CharField(choices=TYPE_CHOICES, max_length=100)
    note = models.TextField(blank=True, null=True)
