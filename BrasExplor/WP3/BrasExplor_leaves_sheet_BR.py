from checkcel import Checkplate
from checkcel.validators import IntValidator, FloatValidator, TextValidator, DateValidator, UniqueValidator, SetValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    metadata = ["Submitter", "Submission date", "Version"]
    validators = OrderedDict([
        ("Id", UniqueValidator()),
        ("Multiplied Population", TextValidator()),
        ("Experimental site", SetValidator(valid_values=["Le Rheu France", "Ploudaniel France", "Site1 Algeria", "Site2 Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Block", IntValidator(min=1, max=3)),
        ("Plant number", IntValidator(min=1, max=5)),
        ("Survey date", DateValidator()),
        ("Leaves number", IntValidator()),
        ("Specific surface", FloatValidator(readme="of 4th fully developped leaf")),
        ("Fresh weight", FloatValidator(readme="of 4th fully developped leaf")),
        ("Dry weight", FloatValidator(readme="of 4th fully developped leaf")),
        ("IPGRI 4.2.98", SetValidator(readme="Lateral Root", valid_values=[0, 3, 5, 7])),
        ("IPGRI 4.2.92", SetValidator(readme="Exterior root color", valid_values=range(1, 11))),
        ("IPGRI 4.2.92 comment", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.93", SetValidator(readme="Interior root color", valid_values=range(1, 8))),
        ("IPGRI 4.2.93 comment", TextValidator(readme="", empty_ok=True)),
        ("Exterior root picture", TextValidator(empty_ok=True)),
        ("Interior root picture", TextValidator(empty_ok=True)),
    ])
