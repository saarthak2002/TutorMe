# from django import forms

# from django.contrib.auth.models import User
# from .models import Student_Profile


# class UpdateProfileForm(forms.ModelForm):
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     # email = forms.EmailField(required=True,
#     #                          widget=forms.TextInput(attrs={'class': 'form-control'}))

#     year_choices = (("1", "First Year"), ("2", "Second Year"), ("3", "Third Year"), ("4", "Fourth Year"), ("5", "Graduate"))
#     year = forms.ChoiceField(choices = year_choices)
#     # year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
#     help_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
#     bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

#     class Meta:
#         model = Student_Profile
#         fields = ['username', 'year', 'help_description', 'bio']