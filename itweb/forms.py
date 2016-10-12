from django.forms import ModelForm
from itweb.models import NewIT


class ITForm(ModelForm):
    # it_name = forms.CharField(max_length=30, required=True)
    # protocol_type = forms.CharField(max_length=10, required=True)
    # request_type = forms.CharField(max_length=10, required=True)
    # url = forms.CharField(max_length=30)
    # desc = forms.CharField(max_length=300)
    # team = forms.CharField(max_length=30)
    # author = forms.CharField(max_length=30)

    class Meta:
        model = NewIT
        fields = ['it_name', 'protocol_type', 'request_type', 'url', 'desc', 'team', 'author']
