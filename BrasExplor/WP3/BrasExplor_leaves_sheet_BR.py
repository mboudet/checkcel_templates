from checkcel import Checkplate
from checkcel.validators import IntValidator, FloatValidator, TextValidator, DateValidator, UniqueValidator, SetValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Derived Population", UniqueValidator()),
        ("Original Population", UniqueValidator()),
        ("Block", IntValidator(min=1, max=3)),
        ("Plant number", IntValidator(min=1, max=5)),
        ("Survey date", DateValidator()),
        ("Leaves number", IntValidator()),
        ("Specific surface", FloatValidator()),
        ("Fresh weight", FloatValidator()),
        ("Dry weight", FloatValidator()),
        ("IPGRI 4.2.98", SetValidator(valid_values=[0, 3, 5, 7])),
        ("IPGRI 4.2.92", IntValidator(min=1, max=10)),
        ("IPGRI 4.2.92 comment", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.93", IntValidator(min=1, max=7)),
        ("IPGRI 4.2.93 comment", TextValidator(empty_ok=True)),
        ("Exterior root picture", TextValidator(empty_ok=True)),
        ("Interior root picture", TextValidator(empty_ok=True)),
    ])
