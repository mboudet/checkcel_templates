from checkcel import Checkplate
from checkcel.validators import IntValidator, DateValidator, UniqueValidator, TextValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Derived Population", UniqueValidator()),
        ("Original Population", UniqueValidator()),
        ("Block", IntValidator(min=1, max=3)),
        ("Harvest date", DateValidator()),
        ("Full flowering date", DateValidator()),
        ("Mean seed weight", TextValidator()),
    ])
