from checkcel import Checkplate
from checkcel.validators import IntValidator, DateValidator, UniqueValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Derived Population", UniqueValidator()),
        ("Original Population", UniqueValidator()),
        ("Block", IntValidator(min=1, max=3)),
        ("Flowering start date", DateValidator()),
        ("50% flowering date", DateValidator(empty_ok=True)),
        ("Full flowering date", DateValidator()),
    ])
