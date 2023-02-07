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
        ("IPGRI 4.2.82 (root shape)", SetValidator(readme="Root, shape in longitudinal section", valid_values=range(1, 11))),
        ("IPGRI 4.2.98 (lateral root)", SetValidator(readme="Lateral Root", valid_values=[0, 3, 5, 7])),
        ("IPGRI 4.2.92 (external root color)", SetValidator(readme="External root color", valid_values=range(1, 11))),
        ("IPGRI 4.2.92 comment", TextValidator(empty_ok=True, readme="if 10 in previous column : explain the color combination; ex : 1 and upper ring 6")),
        ("IPGRI 4.2.93 (internal root color)", SetValidator(readme="Internal root color", valid_values=range(1, 8))),
        ("IPGRI 4.2.93 comment", TextValidator(readme="if 7 in previous column : describe the color", empty_ok=True)),
        ("General remarks", TextValidator(empty_ok=True, readme="explain flowering stage according to Terres Inovia table if necessary; describe diseases on leaves and root if visible etc…")),
        ("Picture file name", TextValidator(readme="Full plant picture (external half root, internal half root, 4th leaf on the same picture). File name (ex : DCS001256.jpeg) corresponding to the plant", empty_ok=True)),
    ])
