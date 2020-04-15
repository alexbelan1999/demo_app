from django import forms


class Cylinder(forms.Form):
    r = forms.FloatField(label="Радиус", initial=0.0, required=True, min_value=0.0)
    h = forms.FloatField(label="Высота", initial=0.0, required=True, min_value=0.0)


class Paral(forms.Form):
    a = forms.FloatField(label="Ребро a", initial=0.0, required=True, min_value=0.0)
    b = forms.FloatField(label="Ребро b", initial=0.0, required=True, min_value=0.0)
    c = forms.FloatField(label="Ребро c", initial=0.0, required=True, min_value=0.0)
