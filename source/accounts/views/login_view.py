from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import TemplateView

from accounts.forms import LoginForm
from accounts.models import Account


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form_data = {} if not next else {'next': next}
        form = self.form(form_data)
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        user_db = Account.objects.filter(is_active=True)
        user_input=request.POST['email']
        if not form.is_valid():
            return redirect('login')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        next = form.cleaned_data.get('next')
        print("REQUEST+++REQUSET", request)
        user = authenticate(request, email=email, password=password)
        print("USER", user)
        if not user:
            return redirect('login')
        login(request, user)
        if next:
            return redirect(next)
        return redirect('index')
