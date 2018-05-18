from blog import models as m
 

class BirdModelForm(forms.ModelForm):
    class Meta:
        model = m.Bird