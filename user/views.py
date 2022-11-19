import json

from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView

from user.models import User, UserSerializer, UserPostSerializer


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super(UserListView, self).get(request, *args, **kwargs)
        user_serializer = UserSerializer(self.object_list, many=True)
        return JsonResponse(user_serializer.data, safe=False, status=200)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        try:
            super(UserDetailView, self).get(request, *args, **kwargs)
        except Http404 as error:
            return JsonResponse({'error': error.args}, status=404)
        ads_serializer = UserSerializer(self.object)
        return JsonResponse(ads_serializer.data, safe=False, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    model = User
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        super(UserCreateView, self).post(request, *args, **kwargs)
        data = json.loads(request.body)
        serializer = UserPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False, status=422)

