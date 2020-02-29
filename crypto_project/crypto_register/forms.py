from django import forms
from .models import Coin

class CoinForm(forms.ModelForm):

    class Meta:
        model = Coin
        fields = '__all__'
        labels = {
            'coin_title': 'Crypto Title',
            'coin_cat' : 'Crypto Category',
            'coin_desc' : 'Crypto Description',
        }

    # def __init__(self, *args, **kwargs):
    #     super(CoinForm,self).__init__(*args, **kwargs)
    #     self.fields['coin_category_coin'].empty_label = "Choose Tag"
    #     self.fields['coin_category_coin'].required = False