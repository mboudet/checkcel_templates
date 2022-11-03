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
        ("Specific surface", FloatValidator()),
        ("Fresh weight", FloatValidator()),
        ("Dry weight", FloatValidator()),
        ("IPGRI 4.2.2", IntValidator(readme="Plant growth habit", min=1, max=10)),
        ("IPGRI 4.2.2 comment", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.3 apex", FloatValidator(readme="Plant height to apex (cm)")),
        ("IPGRI 4.2.3 extremity", FloatValidator(readme="Plant height to extremity (cm)")),
        ("IPGRI 4.2.4", FloatValidator(readme="Plant width (cm)")),
        ("IPGRI 4.2.32", IntValidator(readme="Head forming leaf overlap at terminal region", min=1, max=5)),
        ("IPGRI 4.2.38", IntValidator(readme="Primary colour of outer head leaves", min=1, max=6)),
        ("IPGRI 4.2.41", FloatValidator(readme="Head length (cm)")),
        ("IPGRI 4.2.42", FloatValidator(readme="Head diameter (cm)")),
        ("Head weight", FloatValidator(readme="g")),
        ("IPGRI 4.2.48", IntValidator(readme="Primary color inside cut)", min=1, max=6)),
        ("IPGRI 4.2.48 Exterior picture", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.48 Interior picture", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.62", IntValidator(readme="Axillary stem and bud growth", min=1, max=5)),
        ("IPGRI 4.2.73", IntValidator(readme="Floral apex branching pattern", min=1, max=7)),
        ("IPGRI 4.2.73 comment", TextValidator(empty_ok=True)),
    ])
