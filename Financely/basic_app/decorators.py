from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            print("yashwanth")
        print("how are you")
    return wrapper_func

def printview(string):
    print("subkankar")
    print("subkankar")
    print("subhankar")
    


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name


        return wrapper_func
    return decorator
# 
# def search_bar(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.is_ajax():
#             res = None
#             data = request.POST.get('searchData')
#             item = getStockInfo(data)
#             if len(item)>0 and len(data):
#                 res = item
#             else:
#                 res = 'No stocks found..'
#
#             #print(data)
#             return JsonResponse({'data':res})
#         else:
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_func


# def admin_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#
#         if group == 'Client':
#             return redirect('user-page')
#
#         if group == 'Admin':
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_function


def getout(out):
    print("geout")
    print("geout")
    print("geout")
    print("geout")
    print("geout")
    print("geout")
    print("geout")
    print("geout")
    print("geout")
    print("geout")
    print("geout")
    
