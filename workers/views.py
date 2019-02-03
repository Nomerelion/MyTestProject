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
    print('hello')
    tree_nodes_list = list()
    for item in Employee.objects.all():
        tree_nodes_list.append({
            'id': item.id,
            'parent': item.parent_id if item.parent_id else '#',
            'text': 'Full name: %s, Position: %s' % (item.full_name, item.position)
        })

    print(tree_nodes_list)
    ctx = {
        'core': {
            'data' : tree_nodes_list 
        }
    }
    return JsonResponse(ctx)