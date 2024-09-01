from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, HttpRequest
from auth_app.serializers import UserSerializer, UserCreateSerializer
from auth_app.transport import send_pin_code, fetch_recipient, send_confirmation_link
from auth_app.services import (
    add_pin,
    authenticate,
    update_or_create_user_token,
    use_pin_code,
    user_by_id,
    activate_user,
)


class UserConfirmationView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        data = None
        user_id = request.GET.get("user_id")
        if user_id:
            user = user_by_id(user_id)
            if user:
                if user.is_active:
                    activate_user(user)
                    data = "already activated"
                else:
                    activate_user(user)
                    data = "activated"
            else:
                data = "user with this user_id does't exist"
        else:
            data = "param user_id is empry or does't exist"
        response = {"data": data}
        return Response(response)


class UserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_confirmation_link(user.id, user.email)
        response = {"data": serializer.data}
        return Response(response)


class UserInfoView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest):
        serializer = UserSerializer([request.user], many=True)
        response = {"data": serializer.data}
        return Response(response)


class PinView(APIView):
    """Отправляет pin для существующего пользователя.
    Пользователь определяется по имени (номеру телефона)
     или адресу электронной почты.
    Порядок получения пользователя определяется в настройках.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        recipient = request.GET.get("recipient")
        if recipient:
            user = fetch_recipient(recipient)
            if user:
                pin = add_pin(user)
                send_pin_code(pin.pin_code, recipient)
        return Response({"data": None})


class TokenView(APIView):
    """Возвращает токен по имени пользователя и актуальному пину.
    Пользователь определяется по имени (номеру телефона)
     или адресу электронной почты.
    Порядок получения пользователя определяется в настройках.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST.get("username")
        pincode = request.POST.get("pincode")
        user = authenticate(username, pincode)
        if user is not None:
            token = update_or_create_user_token(user=user)
            if token is not None:
                use_pin_code(pincode)
                return Response({"data": {"token": token.key}})
        return Response({"data": None})
