from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from transaction.models import Transaction

from .forms import IncomeForm, SpentForm


@login_required
def all_transactions(request):
    spents = Transaction.objects.filter(transaction_type=0)
    incomes = Transaction.objects.filter(transaction_type=1)
    return render(request, "transaction/transaction-list.html", {"spents": spents, "incomes": incomes})


@login_required
def add_spent(request):
    if request.method == "POST":
        form = SpentForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.transaction_type = 0
            transaction.save()
            return redirect("transaction_list")
    else:
        form = SpentForm()
    return render(request, "transaction/spent.html", {"form": form})


@login_required
def add_income(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.transaction_type = 1
            transaction.save()
            return redirect("transaction_list")
    else:
        form = IncomeForm()
    return render(request, "transaction/income.html", {"form": form})
