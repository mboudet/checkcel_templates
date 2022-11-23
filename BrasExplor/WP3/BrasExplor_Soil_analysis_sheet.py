from checkcel import Checkplate
from checkcel.validators import FloatValidator, TextValidator, DateValidator, SetValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    metadata = ["Submitter", "Submission date", "Version"]
    validators = OrderedDict([
        ("Experimental site", SetValidator(valid_values=["Le Rheu France", "Ploudaniel France", "Alger Algeria", "Bejaia Algeria", "Adrar Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Type", SetValidator(valid_values=['Control', 'Sample'], readme="Whether the population is a control or a sample population")),
        ("Sampling date", DateValidator()),
        ("Analysis date", DateValidator()),
        ("N", FloatValidator(min=0)),
        ("P", FloatValidator(min=0)),
        ("K", FloatValidator(min=0)),
        ("pH", FloatValidator(min=0, max=14)),
        ("Soil structure", TextValidator()),
    ])
