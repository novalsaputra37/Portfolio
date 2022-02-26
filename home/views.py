from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):

        context = {
            'loop_times' : range(1, 6)
        }
        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            name = self.request.POST.get('contact-name')
            phone = self.request.POST.get('contact-phone')
            email = self.request.POST.get('contact-email')
            subject = self.request.POST.get('subject')
            message = self.request.POST.get('contact-message')

            # print(name, phone, email, subject, message)
            message = "From : " + name + "\nEmail : " + email +"\nPhone : " + phone + "\nMessage : \n" + message

            try:
                send_mail(
                    subject,
                    message,
                    'gatotkacakost@gatotkaca-network.com',
                    ['novalsaputra37@gmail.com'],
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "message sent successfully :) " )
            return redirect ("index")
            

        return render(request, self.template_name)

# def send_mail(request):
#     if request.method == "POST":
#         name = request.POST.get('contact-name')
#         phone = request.POST.get('contact-phone')
#         email = request.POST.get('contact-email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('contact-message')
#         print(name, phone, email, subject, message)

#         return HttpResponseRedirect(reverse('index'))
#     else:
#         return HttpResponse('Invalid request')