from checkcel import Checkplate
from checkcel.validators import IntValidator, FloatValidator, TextValidator, DateValidator, UniqueValidator
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
        ("IPGRI 4.2.2", IntValidator(min=1, max=10)),
        ("IPGRI 4.2.2 comment", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.3 apex", FloatValidator()),
        ("IPGRI 4.2.3 extremity", FloatValidator()),
        ("IPGRI 4.2.4", FloatValidator()),
        ("IPGRI 4.2.32", IntValidator(min=1, max=5)),
        ("IPGRI 4.2.38", IntValidator(min=1, max=6)),
        ("IPGRI 4.2.41", FloatValidator()),
        ("IPGRI 4.2.42", FloatValidator()),
        ("IPGRI 4.2.48", IntValidator(min=1, max=6)),
        ("IPGRI 4.2.48 Exterior picture", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.48 Interior picture", TextValidator(empty_ok=True)),
        ("IPGRI 4.2.62", IntValidator(min=1, max=5)),
        ("IPGRI 4.2.73", IntValidator(min=1, max=7))
        ("IPGRI 4.2.73 comment", TextValidator(empty_ok=True)),
    ])
