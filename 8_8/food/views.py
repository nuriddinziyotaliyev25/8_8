from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Type, Food, Comment, User
from .serializers import TypeSerializer, FoodSerializer,\
                        CommentSerializer, RegisterSerializer
from django.db.models import Q


class TypeListGenericView(ListCreateAPIView):
    serializer_class = TypeSerializer

    def get_queryset(self, *args, **kwargs):
        types = Type.objects.all()

        try:
            if self.request.query_params.get('q', False):
                q = self.request.query_params.get('q')
                types = types.filter(Q(title__icontains=q))
        except:
            pass

        try:
            # ?o=-pk teskari tartibda, ?o=pk to'g'ri tartibda
            if self.request.query_params.get('o', False):
                types = types.order_by(self.request.query_params.get('o'))
        except:
            pass

        return types


class TypeDetailGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer



class FoodListGenericView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_queryset(self, *args, **kwargs):
        foods = Food.objects.all()

        try:
            if self.request.query_params.get('type_id', False):
                foods = foods.filter(type_id=self.request.query_params.get('type_id'))
        except:
            pass

        try:
            if self.request.query_params.get('q', False):
                q = self.request.query_params.get('q')
                foods = foods.filter(Q(title__icontains=q) | Q(ingredient__icontains=q))
        except:
            pass

        try:
            # ?o=-created_at teskari tartibda, ?o=created_at to'g'ri tartibda
            if self.request.query_params.get('o', False):
                foods = foods.order_by(self.request.query_params.get('o'))
        except:
            pass

        return foods


class FoodDetailGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CommentListMixinView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        comment = Comment.objects.all()

        try:
            if self.request.query_params.get('author_id', False):
                comment = comment.filter(author_id=self.request.query_params.get('author_id'))
        except:
            pass

        try:
            if self.request.query_params.get('food_id', False):
                comment = comment.filter(food_id=self.request.query_params.get('food_id'))
        except:
            pass

        try:
            if self.request.query_params.get('q', False):
                q = self.request.query_params.get('q')
                comment = comment.filter(Q(text__icontains=q))
        except:
            pass

        try:
            # ?o=-created_at teskari tartibda, ?o=created_at to'g'ri tartibda
            if self.request.query_params.get('o', False):
                comment = comment.order_by(self.request.query_params.get('o'))
        except:
            pass

        return comment


class CommentDetailMixinView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RegisterView(CreateAPIView):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'message': "You are logout our site"}, status=205)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

