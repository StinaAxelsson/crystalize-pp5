from django import forms


class ContactForm(forms.Form):
    """
    Create a contact form to users be able to
    contact the site owner
    """
    name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True, label='Email Address')
    subject = forms.CharField(required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the fields and set focus on the
        first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholder[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
