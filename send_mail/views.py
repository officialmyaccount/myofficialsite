from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = "system@gmail.com"
        recipient_list = [
            "yamadahirotami@optsp.co.jp"
        ]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        print('メールが送信されました')
        return render(request, 'index.html')
    
    return render(request, 'contact.html')
