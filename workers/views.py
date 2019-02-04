from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from workers.models import Employee

def index(request):
    ctx = {
        'name': 'Edgar'
    }
    return render(request, "workers/index.html", ctx)

def show_tree(request):
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
        'table_name' : 'Workers' 
    }
    return render(request, "workers/table.html" , ctx)

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

    ctx = { 'data' : table_list } 

    return JsonResponse(ctx)