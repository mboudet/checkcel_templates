from checkcel import Checkplate
from checkcel.validators import SetValidator, NoValidator, UniqueValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Agricultural field", UniqueValidator()),
        ("Crop", SetValidator(valid_values=['Wheat', 'Rapeseed'])),
        ("Region", SetValidator(valid_values=['West', 'East', 'South'])),
        ("Locality", NoValidator()),
        ("GPS latitude", NoValidator()),
        ("GPS longitude", NoValidator()),
        ("Organic matter supply", SetValidator(valid_values=['Yes', 'No'])),
        ("Farming type", SetValidator(valid_values=['Organic', 'Conventional'])),
        ("Tillage system", SetValidator(valid_values=['Superficial', 'Plowing', 'No-till']))
    ])
