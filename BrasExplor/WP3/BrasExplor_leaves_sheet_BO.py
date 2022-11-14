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
        ("Leaves number", IntValidator(min=0)),
        ("Specific surface", FloatValidator(min=0, readme="of 4th fully developped leaf")),
        ("Fresh leaf weight", FloatValidator(min=0, readme="of 4th fully developped leaf, in grams")),
        ("Dry leaf weight", FloatValidator(min=0, readme="of 4th fully developped leaf, in grams")),
        ("Fresh root weight", FloatValidator(min=0, readme="in grams")),
        ("Dry root weight", FloatValidator(min=0, readme="in grams")),
        ("IPGRI 4.2.2", SetValidator(readme="Plant growth habit", valid_values=range(1, 11))),
        ("IPGRI 4.2.2 comment", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.3 apex", FloatValidator(min=0, readme="Plant height to apex (cm)")),
        ("IPGRI 4.2.3 extremity", FloatValidator(min=0, readme="Plant height to extremity (cm)")),
        ("IPGRI 4.2.4", FloatValidator(min=0, readme="Plant width (cm)")),
        ("IPGRI 4.2.36", SetValidator(readme="Head forming leaf overlap at terminal region", valid_values=range(1, 6))),
        ("IPGRI 4.2.38", SetValidator(readme="Primary colour of outer head leaves", valid_values=range(1, 7))),
        ("IPGRI 4.2.41", FloatValidator(min=0, readme="Head length (cm)")),
        ("IPGRI 4.2.42", FloatValidator(min=0, readme="Head diameter (cm)")),
        ("Head weight", FloatValidator(min=0, readme="g")),
        ("IPGRI 4.2.48", SetValidator(readme="Primary color inside cut", valid_values=range(1, 7))),
        ("IPGRI 4.2.62", SetValidator(readme="Axillary stem and bud growth", valid_values=range(0, 6))),
        ("IPGRI 4.2.73", SetValidator(readme="Floral apex branching pattern", valid_values=range(1, 8))),
        ("IPGRI 4.2.73 comment", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.48 Exterior picture", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.48 Interior picture", TextValidator(empty_ok=True)),
        ("General remarks", TextValidator(empty_ok=True)),
    ])
