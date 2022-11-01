from checkcel import Checkplate
from checkcel.validators import FloatValidator, TextValidator, DateValidator, SetValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Experimental site", SetValidator(valid_values=["Le Rheu France", "Ploudaniel France", "Site1 Algeria", "Site2 Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Sampling date", DateValidator()),
        ("Analysis date", DateValidator()),
        ("N", FloatValidator()),
        ("P", FloatValidator()),
        ("K", FloatValidator()),
        ("pH", FloatValidator(min=0, max=14)),
        ("Soil structure", TextValidator()),
    ])
