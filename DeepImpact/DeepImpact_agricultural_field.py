from checkcel import Checkplate
from checkcel.validators import SetValidator, NoValidator, UniqueValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Agricultural field", UniqueValidator()),
        ("Crop", SetValidator(valid_values=['Wheat', 'Colza'])),
        ("Region", SetValidator(valid_values=['West', 'East', 'North', 'South'])),
        ("Locality", NoValidator()),
        ("GPS", NoValidator()),
        ("Organic matter supply", SetValidator(valid_values=['Yes', 'No'])),
        ("Farming type", SetValidator(valid_values=['Organic', 'Conventional'])),
        ("Soil preparation", SetValidator(valid_values=['Tillage', 'Superficial', 'No-till']))
    ])
