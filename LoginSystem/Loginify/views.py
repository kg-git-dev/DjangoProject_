from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import UserDetailsSerializer
from .models import UserDetails
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from rest_framework.decorators import api_view

# Create your views here.
def hello_world(request):
    return Response("Hello World", status=status.HTTP_200_OK)

# Had to use APIView here in order to render templates    
class SignUpView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'

    def get(self, request):
        return Response({})

    def post(self, request):
            
        serializer = UserDetailsSerializer(data=request.data)

        if not serializer.is_valid():
            error_message = "An account with this email may already exist or the email is incorrect"
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return redirect('log_in')
    
class LogInView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        return Response({})

    def post(self, request):
        email = request.data.get('Email')
        password = request.data.get('Password')

        if not email or not password:
            return Response(
                {'error': 'Email and Password are required.'},
                status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserDetails.objects.get(Email=email)
            if not password == user.Password:
                raise UserDetails.DoesNotExist
            else:
                return redirect('login_success')
        
        except UserDetails.DoesNotExist:
            return Response(
                {'error': 'Invalid Credentials'},
                status=status.HTTP_400_BAD_REQUEST)

class LoginSuccessView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login_success.html'

    def get(self, request):
        return Response({})

# Discovered viewsets when reading DRF docs but used functions as per instructions 
@api_view(['GET'])
def all_user_details(request):
    try:
        user = UserDetails.objects.all()
        serializer = UserDetailsSerializer(user, many=True)
        return Response(serializer.data)
    except UserDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def user_details_by_email(request, Email):
    try:
        user = UserDetails.objects.get(Email=Email)
        serializer = UserDetailsSerializer(user)
        return Response(serializer.data)
    except UserDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'PATCH'])
def update_user_details(request, Email):
    try:
        user = UserDetails.objects.get(Email=Email)
    except UserDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserDetailsSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, Email):
    try:
        user = UserDetails.objects.get(Email=Email)
    except UserDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response({'message':'Succesfully deleted user'}, status=status.HTTP_200_OK)
