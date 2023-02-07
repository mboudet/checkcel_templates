from checkcel import Checkplate
from checkcel.validators import IntValidator, DateValidator, UniqueValidator, TextValidator, SetValidator, FloatValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    metadata = ["Submitter", "Submission date", "Version"]
    empty_ok = True
    validators = OrderedDict([
        ("Id", UniqueValidator(empty_ok=False)),
        ("Multiplied Population", TextValidator(empty_ok=False)),
        ("Experimental site", SetValidator(empty_ok=False, valid_values=["Le Rheu France", "Ploudaniel France", "Alger Algeria", "Bejaia Algeria", "Adrar Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Type", SetValidator(empty_ok=False, valid_values=['Control', 'Sample'], readme="Whether the population is a control or a sample population")),
        ("Block", IntValidator(empty_ok=False, min=1, max=3)),
        ("Harvest date", DateValidator()),
        ("Mean seed weight", FloatValidator(min=0)),
        ("Picture", TextValidator(empty_ok=True))
    ])
