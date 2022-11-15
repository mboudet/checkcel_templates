from checkcel import Checkplate
from checkcel.validators import IntValidator, FloatValidator, TextValidator, DateValidator, UniqueValidator, SetValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    metadata = ["Submitter", "Submission date", "Version"]
    validators = OrderedDict([
        ("Id", UniqueValidator()),
        ("Multiplied Population", TextValidator()),
        ("Experimental site", SetValidator(valid_values=["Le Rheu France", "Ploudaniel France", "Alger Algeria", "Bejaia Algeria", "Adrar Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Block", IntValidator(min=1, max=3)),
        ("Plant number", IntValidator(min=1, max=5)),
        ("Survey date", DateValidator()),
        ("Leaves number", IntValidator(min=0)),
        ("Specific surface", FloatValidator(min=0, readme="of 4th fully developped leaf (cm²)")),
        ("Fresh leaf weight", FloatValidator(min=0, readme="of 4th fully developped leaf, in grams")),
        ("Dry leaf weight", FloatValidator(min=0, readme="of 4th fully developped leaf, in grams")),
        ("Fresh root weight", FloatValidator(min=0, readme="in grams")),
        ("Dry root weight", FloatValidator(min=0, readme="in grams")),
        ("IPGRI 4.2.82", SetValidator(readme="Root, shape in longitudinal section", valid_values=range(1, 11))),
        ("IPGRI 4.2.98", SetValidator(readme="Lateral Root", valid_values=[0, 3, 5, 7])),
        ("IPGRI 4.2.92", SetValidator(readme="Exterior root color", valid_values=range(1, 11))),
        ("IPGRI 4.2.92 comment", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.93", SetValidator(readme="Interior root color", valid_values=range(1, 8))),
        ("IPGRI 4.2.93 comment", TextValidator(readme="", empty_ok=True)),
        ("General remarks", TextValidator(empty_ok=True)),
        ("Picture", TextValidator(readme="Full plant picture (external, internal, 4th leaf on the same picture)", empty_ok=True)),
    ])
