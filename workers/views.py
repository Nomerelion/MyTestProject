from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from workers.models import Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

import json

def tree(request):
    ctx = {
    }
    return render(request, 'tree.html', ctx)

def show_tree(request):
    print('hello')
    tree_nodes_list = list()
    for item in Employee.objects.all():
        tree_nodes_list.append({
            'id': item.id,
            'parent': item.parent_id if item.parent_id else '#',
            'text': 'Full name: %s, Position: %s' % (item.full_name, item.position)
        })

    ctx = {
        'core': {
            'data' : tree_nodes_list 
        }
    }
    return JsonResponse(ctx)

def table(request):
    ctx = {
        'table_name' : 'Workers',
        'table_opts': dict({},
            columns=json.dumps([
                {
                    'data': u'Name',
                    'title': u'Name'
                },
                {   
                    'data': u'Position',
                    'title': u'Position' 
                },
                {
                    'data': u'Salary',
                    'title': u'Salary'
                },
                { 
                    'data': u'Employment date',
                    'title': u'Employment date'
                }
            ])
        )    
    }
    return render(request, 'table.html' , ctx)

def show_data(request):
    table_list = list()
    for item in Employee.objects.all():
        table_list.append({
            'Name': item.full_name,
            'Position': item.position,
            'Salary': item.salary,
            'Employment date': item.employment_date,
            'extn': item.id
        })

    ctx = {
        'data' : table_list,  
    } 
    return JsonResponse(ctx)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
