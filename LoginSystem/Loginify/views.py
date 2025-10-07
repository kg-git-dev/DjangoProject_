from rest_framework import status
from rest_framework.response import Response
from .serializers import UserDetailsSerializer
from .models import UserDetails
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect

# Create your views here.
def hello_world(request):
    return Response("Hello World", status=status.HTTP_200_OK)
    
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
        return redirect('login')
    
class LogInView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        return Response({})

    def post(self, request):
        email = request.data.get('Email')
        password = request.data.get('Password')

        print(email, password)

        if not email or not password:
            return Response(
                {'error': 'Email and Password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = UserDetails.objects.get(Email=email)
            if not password == user.Password:
                raise UserDetails.DoesNotExist
            else:
                return redirect('login_success')
        
        except UserDetails.DoesNotExist:
            return Response(
                {'error': 'Invalid Credentials'},
                status=status.HTTP_400_BAD_REQUEST
        )

class LoginSuccessView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login_success.html'

    def get(self, request):
        return Response({})