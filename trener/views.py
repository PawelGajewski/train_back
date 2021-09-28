from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from trener.serializers import *
from rest_framework import filters
import jwt
import datetime


class Register(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Login(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class Auth(APIView):
    def post(self, request):
        token = request.data['jwt']
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


# class FormControll(APIView):
#     def post(self, request):
#         weight = request.data['weight']
#         height = request.data['height']
#         weight = request.data['weight']
#         return Response({}, status=200)



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=username']


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class WeightView(generics.ListCreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=ownerID__id']

class ChestView(generics.ListCreateAPIView):
    queryset = Chest.objects.all()
    serializer_class = ChestSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=ownerID__id']


class BicepsView(generics.ListCreateAPIView):
    queryset = Biceps.objects.all()
    serializer_class = BicepsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=ownerID__id']


class BenchPressView(generics.ListCreateAPIView):
    queryset = BenchPress.objects.all()
    serializer_class = BenchPressSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=ownerID__id']


class SquatView(generics.ListCreateAPIView):
    queryset = Squat.objects.all()
    serializer_class = SquatSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=ownerID__id']


class DeadliftView(generics.ListCreateAPIView):
    queryset = Deadlift.objects.all()
    serializer_class = DeadliftSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=ownerID__id']