import random
import qrcode
import io
import base64

import qrcode
from project import settings
from django.contrib import messages

from django.shortcuts import render

from restaurantly.forms import BookTableForm, QrCodeForm


def index(request):
    form = BookTableForm
    context = {
        'form': form,
    }
    return render(request, 'restaurant/index.html', context)


import qrcode
import io
import base64

def book_table(request):
    if request.method == 'POST':

        qrcode_table_form = QrCodeForm(data=request.POST)
        book_table_form = BookTableForm(data=request.POST)

        if qrcode_table_form.is_valid() and book_table_form.is_valid():
            qrcode_table_form.save()
            book_table_form.save()
            messages.success(request, 'Your table was booked successfully !!!')

        data = request.POST

        name = data['name']
        email = data['email']
        phone = data['phone']
        date = data['date']
        time = data['time']
        people = data['people']
        message = data['message']

        context_data = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Date: {date}
        Time: {time}
        People: {people}
        Message: {message}
        """

        # generate QR code in memory — no file saving
        qr = qrcode.make(context_data)
        buffer = io.BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)
        qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return render(request, 'restaurant/qr_code_detail.html', context={
            'qr_code_base64': qr_base64,
            'name': name,
            'date': date,
            'time': time,
            'people': people,
        })

    return render(request, 'restaurant/components/sub_components/__book_table_form.html')

# def book_table(request):
#     if request.method == 'POST':
#
#         qrcode_table_form = QrCodeForm(data=request.POST)
#         book_table_form = BookTableForm(data=request.POST)
#
#         if qrcode_table_form and book_table_form.is_valid():
#             qrcode_table_form.save()
#             book_table_form.save()
#             messages.success(request, 'Your table was booked successfully !!!')
#
#         data = request.POST
#
#         name = data['name']
#         email = data['email']
#         phone = data['phone']
#         date = data['date']
#         time = data['time']
#         people = data['people']
#         message = data['message']
#
#         context_data = f"""
#         name: {name}
#         email: {email}
#         phone: {phone}
#         date: {date}
#         time: {time}
#         people: {people}
#         message: {message}
#         """
#
#         random_int = random.randint(1, 99999)
#         qr_code_name = f'{random_int}.png'
#
#         qr_code_data = qrcode.make(context_data)
#
#         qr_code_data.save(settings.MEDIA_ROOT / qr_code_name)
#
#         data = f"""
#         name: {name}
#         email: {email}
#         phone: {phone}
#         date: {date}
#         time: {time}
#         people: {people}
#         message: {message}
#         """
#
#         open_file = open(settings.MEDIA_ROOT / f"{random_int}.txt", "w+")
#         open_file.write(data)
#         open_file.close()
#
#         return render(request, 'restaurant/qr_code_detail.html', context={'qr_code_detail': qr_code_name,
#                                                                           'file': random_int})
#
#     return render(request, 'restaurant/components/sub_components/__book_table_form.html')
