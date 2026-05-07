from django import forms

from .models import BookTable, Qrcode


class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = [
            'name',
            'email',
            'phone',
            'date',
            'time',
            'people',
            'message',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-control',
                'type': 'text',
                'name': 'name',
                'id': 'name',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars',
            }),

            'email': forms.EmailInput(attrs={
                'type': 'email',
                'class': 'form-control',
                'name': 'email',
                'id': 'email',
                'placeholder': 'Your Email',
                'data-rule': 'email',
                'data-msg': 'Please enter a valid email',
            }),

            'phone': forms.NumberInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'name': 'phone',
                'id': 'phone',
                'placeholder': 'Your Phone',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars',
            }),

            'date': forms.TextInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'name': 'date',
                'id': 'date',
                'placeholder': 'Date',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 10 chars',
            }),

            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'name': 'time',
                'id': 'time',
                'placeholder': 'Time',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars',
            }),

            'people': forms.NumberInput(attrs={
                'type': 'number',
                'class': 'form-control',
                'name': 'people',
                'id': 'people',
                'placeholder': '# of people',
                'data-rule': 'minlen:1',
                'min': 1,
                'data-msg': 'Please enter at least 1 chars',
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'name': 'message',
                'rows': '5',
                'placeholder': 'Message',
            })

        }


class QrCodeForm(forms.ModelForm):
    class Meta:
        model = Qrcode
        fields = [
            'name',
            'email',
            'phone',
            'date',
            'time',
            'people',
            'message',
        ]
