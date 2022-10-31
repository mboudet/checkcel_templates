from checkcel import Checkplate
from checkcel.validators import FloatValidator, NoValidator, TextValidator, DateValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Experimental site", NoValidator()),
        ("Sampling date", DateValidator()),
        ("Analysis date", DateValidator()),
        ("N", FloatValidator()),
        ("P", FloatValidator()),
        ("K", FloatValidator()),
        ("pH", FloatValidator(min=0, max=14)),
        ("Soil structure", TextValidator()),
    ])
