from checkcel import Checkplate
from checkcel.validators import IntValidator, DateValidator, UniqueValidator, TextValidator, SetValidator, FloatValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    metadata = ["Submitter", "Submission date", "Version"]
    validators = OrderedDict([
        ("Id", UniqueValidator()),
        ("Multiplied Population", TextValidator()),
        ("Experimental site", SetValidator(valid_values=["Le Rheu France", "Ploudaniel France", "Alger Algeria", "Bejaia Algeria", "Adrar Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Type", SetValidator(valid_values=['Control', 'Sample'], readme="Whether the population is a control or a sample population")),
        ("Block", IntValidator(min=1, max=3)),
        ("Harvest date", DateValidator()),
        ("Mean seed weight", FloatValidator(min=0)),
        ("Picture", TextValidator(empty_ok=True))
    ])
