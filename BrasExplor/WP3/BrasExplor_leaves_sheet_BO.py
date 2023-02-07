from checkcel import Checkplate
from checkcel.validators import IntValidator, FloatValidator, TextValidator, DateValidator, UniqueValidator, SetValidator
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
        ("Plant number", IntValidator(empty_ok=False, min=1, max=5)),
        ("Survey date", DateValidator()),
        ("Leaves number", IntValidator(min=0)),
        ("4th leaf specific surface", FloatValidator(min=0, readme="4th fully developped leaf (cm²)")),
        ("Fresh 4th leaf weight", FloatValidator(min=0, readme="4th fully developped leaf, in grams")),
        ("Dry 4th leaf weight", FloatValidator(min=0, readme="4th fully developped leaf, in grams")),
        ("Fresh root weight", FloatValidator(min=0, readme="in grams")),
        ("Dry root weight", FloatValidator(min=0, readme="in grams")),
        ("IPGRI 4.2.2 (growth habit)", SetValidator(readme="Plant growth habit", valid_values=range(1, 11))),
        ("IPGRI 4.2.2 comment", TextValidator(empty_ok=True, readme="if 10 in previous column : explain the growth habit")),
        ("IPGRI 4.2.3 apex", FloatValidator(min=0, readme="Plant height to apex (cm)")),
        ("IPGRI 4.2.3 extremity", FloatValidator(min=0, readme="Plant height to extremity (cm)")),
        ("IPGRI 4.2.4 (plant width)", FloatValidator(min=0, readme="Plant width (cm)")),
        ("IPGRI 4.2.36 (leaf overlap)", SetValidator(readme="Head forming leaf overlap at terminal region", valid_values=range(1, 6))),
        ("IPGRI 4.2.38 (outer head leaves color)", SetValidator(readme="Primary colour of outer head leaves", valid_values=range(1, 7))),
        ("IPGRI 4.2.41 (head length)", FloatValidator(min=0, readme="Head length (cm)")),
        ("IPGRI 4.2.42 (head diameter", FloatValidator(min=0, readme="Head diameter (cm)")),
        ("Head weight", FloatValidator(min=0, readme="g")),
        ("IPGRI 4.2.48 (primary color inside cut)", SetValidator(readme="Primary color inside cut", valid_values=range(1, 7))),
        ("IPGRI 4.2.62 (stem and bud growth)", SetValidator(readme="Axillary stem and bud growth", valid_values=range(0, 6))),
        ("IPGRI 4.2.73 (apex branching pattern)", SetValidator(readme="Floral apex branching pattern", valid_values=range(1, 8))),
        ("IPGRI 4.2.73 comment", TextValidator(empty_ok=True, readme="if 7 in previous column : explain the floral apex branching pattern")),
        ("General remarks", TextValidator(empty_ok=True, readme="any remark regarding the plant, diseases on leaves and root if visible etc…")),
        ("Picture file name", TextValidator(readme="Full plant picture (external half root, internal half root, 4th leaf on the same picture). File name (ex : DCS001256.jpeg) corresponding to the plant", empty_ok=True)),
    ])
