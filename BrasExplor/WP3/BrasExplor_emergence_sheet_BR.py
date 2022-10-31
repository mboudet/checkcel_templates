from checkcel import Checkplate
from checkcel.validators import IntValidator, TextValidator, DateValidator, UniqueValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Derived Population", UniqueValidator()),
        ("Original Population", UniqueValidator()),
        ("Block", IntValidator(min=1, max=3)),
        ("Sowing date", DateValidator()),
        ("Seed number", IntValidator()),
        ("Cotyledon stage date", DateValidator()),
        ("Cotyledon stage seedling number", IntValidator()),
        ("Cotyledon stage field agent", TextValidator()),
        ("3-5 leaves stage date", DateValidator()),
        ("3-5 leaves stage seedling number", IntValidator()),
        ("3-5 leaves stage field agent", TextValidator()),
    ])
