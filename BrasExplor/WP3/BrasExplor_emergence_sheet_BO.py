from checkcel import Checkplate
from checkcel.validators import IntValidator, TextValidator, DateValidator, UniqueValidator, SetValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Id", UniqueValidator()),
        ("Multiplied Population", TextValidator()),
        ("Experimental site", SetValidator(valid_values=["Le Rheu France", "Ploudaniel France", "Site1 Algeria", "Site2 Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Greenhouse sowing date", SetValidator()),
        ("Seed number", IntValidator()),
        ("Cotyledon stage date", DateValidator()),
        ("Cotyledon stage seedling number", IntValidator()),
        ("Cotyledon stage field agent", TextValidator()),
        ("3-5 leaves stage date", DateValidator()),
        ("3-5 leaves stage seedling number", IntValidator()),
        ("3-5 leaves stage field agent", TextValidator()),
    ])
