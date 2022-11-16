import json

from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from rest_framework.exceptions import ValidationError

from category.models import Category, CategorySerializer


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super(CategoryListView, self).get(request, *args, **kwargs)
        categories_serializer = CategorySerializer(self.object_list, many=True)
        return JsonResponse(categories_serializer.data, safe=False, status=200)

    def post(self, request):
        data = json.loads(request.body)
        serializer = CategorySerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            return JsonResponse(serializer.errors, safe=False, status=422)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            super(CategoryDetailView, self).get(request, *args, **kwargs)
        except Http404 as error:
            return JsonResponse({'error': error.args}, status=404)
        categories_serializer = CategorySerializer(self.object)
        return JsonResponse(categories_serializer.data, safe=False, status=200)
