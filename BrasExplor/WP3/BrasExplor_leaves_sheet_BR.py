from checkcel import Checkplate
from checkcel.validators import IntValidator, FloatValidator, TextValidator, DateValidator, UniqueValidator, SetValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Id", UniqueValidator()),
        ("Multiplied Population", TextValidator()),
        ("Experimental site", SetValidator(valid_values=["Le Rheu France", "Ploudaniel France", "Site1 Algeria", "Site2 Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Block", IntValidator(min=1, max=3)),
        ("Plant number", IntValidator(min=1, max=5)),
        ("Survey date", DateValidator()),
        ("Leaves number", IntValidator()),
        ("Specific surface", FloatValidator()),
        ("Fresh weight", FloatValidator()),
        ("Dry weight", FloatValidator()),
        ("IPGRI 4.2.98", SetValidator(readme="Lateral Root", valid_values=[0, 3, 5, 7])),
        ("IPGRI 4.2.92", IntValidator(readme="Exterior root color", min=1, max=10)),
        ("IPGRI 4.2.92 comment", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.93", IntValidator(readme="Interior root color", min=1, max=7)),
        ("IPGRI 4.2.93 comment", TextValidator(readme="", empty_ok=True)),
        ("Exterior root picture", TextValidator(empty_ok=True)),
        ("Interior root picture", TextValidator(empty_ok=True)),
    ])
