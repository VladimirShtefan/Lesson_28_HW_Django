import json

from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.exceptions import ValidationError

from ad.models import Ad, AdSerializer
from category.models import Category
from user.models import User


def index(request):
    if request.method == 'GET':
        return JsonResponse({"status": "ok"}, status=200)


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super(AdListView, self).get(request, *args, **kwargs)
        ads_serializer = AdSerializer(self.object_list, many=True)
        return JsonResponse(ads_serializer.data, safe=False, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    model = Ad
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        super(AdCreateView, self).post(request, *args, **kwargs)
        data = json.loads(request.body)
        serializer = AdSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            return JsonResponse(serializer.errors, safe=False, status=422)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            super(AdDetailView, self).get(request, *args, **kwargs)
        except Http404 as error:
            return JsonResponse({'error': error.args}, status=404)
        ads_serializer = AdSerializer(self.object)
        return JsonResponse(ads_serializer.data, safe=False, status=200)

