from django.shortcuts import render

# Create your views here.
# renderizar um arquivo HMTL
def metodoProduto(request):
    return render(request, 'produtox/index.html')