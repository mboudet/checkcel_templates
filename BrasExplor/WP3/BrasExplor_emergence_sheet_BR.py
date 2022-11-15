from checkcel import Checkplate
from checkcel.validators import IntValidator, TextValidator, DateValidator, UniqueValidator, SetValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    metadata = ["Submitter", "Submission date", "Version"]
    validators = OrderedDict([
        ("Id", UniqueValidator()),
        ("Multiplied Population", TextValidator()),
        ("Experimental site", SetValidator(valid_values=["Le Rheu France", "Ploudaniel France", "Alger Algeria", "Bejaia Algeria", "Adrar Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Block", IntValidator(min=1, max=3)),
        ("Sowing date", DateValidator()),
        ("Seed number", IntValidator(min=0)),
        ("Cotyledon stage date", DateValidator()),
        ("Cotyledon stage seedling number", IntValidator(min=0)),
        ("Cotyledon stage field agent", TextValidator()),
        ("3-5 leaves stage date", DateValidator()),
        ("3-5 leaves stage seedling number", IntValidator(min=0)),
        ("3-5 leaves stage field agent", TextValidator()),
    ])
