from django import forms
from .models import LandInfo
from django.utils.translation import gettext_lazy as _


class LandRegister(forms.ModelForm):
    RENTAL="RENTAL"
    AVAILABLE="AVAILABLE"
    SOLD="SOLD"

    STATUS=(
        (RENTAL,'Rental'),
        (AVAILABLE,'Available'),
        (SOLD,'Sold'),
    )
    land_status = forms.ChoiceField(required=True, choices=STATUS)
    class Meta():
        model = LandInfo
        fields = ('email','plot','land_size','description','price','location','image','lga_situated','state','land_status','certificate')
        labels={'email':_('Email'),'plot':_('Plot'),'land_size':_('Land size'),
                'description':_('Land description'),'price':_('Price'),
                'location':_('Location'),'image':_('Land image'),'lga_situated':_('LGA situated'),
                'state':_('State'),'land_status':_('Land status'),'certificate':_('Certificate of occupancy')}
