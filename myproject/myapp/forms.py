from logging import PlaceHolder
from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
    }))
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your comment'
    }))
    
    class Meta:
        model = CommentModel
        fields = ['name', 'comment']

    def clean(self):
        # data is fetched using the super function of django
        super(CommentForm, self).clean()

        name  = self.cleaned_data.get('name')
        comment = self.cleaned_data.get('comment')


        if len(name) < 3:
            self._errors['name'] = self.error_class([
                'Name should be more than 3 character'
            ])
        if len(comment) < 4:
            self._errors['comment'] = self.error_class([
                'comment should be more than 4 characters'
            ])
        return self.cleaned_data
