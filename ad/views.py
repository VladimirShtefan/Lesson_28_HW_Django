import json

from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView

from ad.models import Ad, AdListSerializer, AdPostSerializer


def index(request):
    if request.method == 'GET':
        return JsonResponse({"status": "ok"}, status=200)


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super(AdListView, self).get(request, *args, **kwargs)
        ads_serializer = AdListSerializer(self.object_list, many=True)
        return JsonResponse(ads_serializer.data, safe=False, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    model = Ad
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        super(AdCreateView, self).post(request, *args, **kwargs)
        data = json.loads(request.body)
        serializer = AdPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False, status=422)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            super(AdDetailView, self).get(request, *args, **kwargs)
        except Http404 as error:
            return JsonResponse({'error': error.args}, status=404)
        ads_serializer = AdListSerializer(self.object)
        return JsonResponse(ads_serializer.data, safe=False, status=200)
