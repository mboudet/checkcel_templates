from checkcel import Checkplate
from checkcel.validators import IntValidator, TextValidator, DateValidator, UniqueValidator, SetValidator, FloatValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    metadata = ["Submitter", "Submission date", "Version"]
    validators = OrderedDict([
        ("Id", UniqueValidator()),
        ("Multiplied Population", TextValidator()),
        ("Experimental site", SetValidator(valid_values=["Le Rheu France", "Ploudaniel France", "Alger Algeria", "Bejaia Algeria", "Adrar Algeria", "Tunisia", "Slovenia", "Italy"])),
        ("Type", SetValidator(valid_values=['Control', 'Sample'], readme="Whether the population is a control or a sample population")),
        ("Block", IntValidator(min=1, max=3)),
        ("Survey date", DateValidator()),
        ("Flowering %", FloatValidator(min=0)),
        ("Survey date 2", DateValidator(empty_ok=True)),
        ("Flowering % 2", FloatValidator(min=0, empty_ok=True)),
        ("Survey date 3", DateValidator(empty_ok=True)),
        ("Flowering % 3", FloatValidator(min=0, empty_ok=True)),
        ("Survey date 4", DateValidator(empty_ok=True)),
        ("Flowering % 4", FloatValidator(min=0, empty_ok=True)),
        ("Survey date 5", DateValidator(empty_ok=True)),
        ("Flowering % 5", FloatValidator(min=0, empty_ok=True)),
        ("Survey date 6", DateValidator(empty_ok=True)),
        ("Flowering % 6", FloatValidator(min=0, empty_ok=True)),
        ("Survey date 7", DateValidator(empty_ok=True)),
        ("Flowering % 7", FloatValidator(min=0, empty_ok=True)),
        ("Survey date 8", DateValidator(empty_ok=True)),
        ("Flowering % 8", FloatValidator(min=0, empty_ok=True)),
        ("Survey date 9", DateValidator(empty_ok=True)),
        ("Flowering % 9", FloatValidator(min=0, empty_ok=True)),
        ("Survey date 10", DateValidator(empty_ok=True)),
        ("Flowering % 10", FloatValidator(min=0, empty_ok=True)),
    ])
