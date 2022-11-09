from checkcel import Checkplate
from checkcel.validators import IntValidator, DateValidator, UniqueValidator, TextValidator, SetValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    metadata = ["Submitter", "Submission date", "Version"]
    validators = OrderedDict([
        ("Id", UniqueValidator()),
        ("Multiplied Population", TextValidator()),
        ("Experimental site", SetValidator(valid_values=["Le Rheu France", "Ploudaniel France", "Site1 Algeria", "Site2 Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Block", IntValidator(min=1, max=3)),
        ("Harvest date", DateValidator()),
        ("Mean seed weight", TextValidator()),
        ("Picture", TextValidator(empty_ok=True))
    ])
