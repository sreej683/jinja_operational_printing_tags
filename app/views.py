from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    d={'name':'lasya','age':2}
    return render(request,'jinja_print.html',context=d)



def jinja_operations(request):
    d={'name':'pranav','age':19}
    return render(request,'jinja_operations.html',context=d)



def nestedif(request):
    d={'name':'Akarsh','age':16}
    return render(request,'nestedif.html',context=d)

def forloop(request):
    d={'name':'lasya'}
    return render(request,'forloop.html',context=d)