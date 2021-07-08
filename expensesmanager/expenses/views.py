from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages

# Create your views here.


@login_required(login_url='/auth/login')
def index(request):
    categories = Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)
    context = {
        'expenses': expenses,
    }
    return render(request, 'expenses/index.html', context)


def add_expense(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        # get access to previous inputs
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Amount is a required field')
            return render(request, 'expenses/add_expense.html', context)

        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']

        description = request.POST['description']
        if not description:
            messages.error(request, 'Description is a required field')
            return render(request, 'expenses/add_expense.html', context)

    Expense.objects.create(owner=request.user,
                           amount=amount, description=description, category=category, date=date)
    messages.success(request, 'Expense saved successfully')
    return redirect('expenses')


def expense_edit(request, id):
    expenses = Expense.objects.filter(pk=id)
    context = {
        'expense': expenses
    }

    if request.method == 'GET':
        return render(request, 'expenses/edit-expense.html', context)
    else:
        messages.info(request, "Handling post form")
        return render(request, 'expenses/edit-expense.html', context)
