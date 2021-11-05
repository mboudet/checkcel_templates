from checkcel import Checkplate
from checkcel.validators import SetValidator, NoValidator, DateValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Agricultural field", NoValidator()),
        ("Plot", SetValidator(valid_values=['1', '2', '3', '4', 'mixed'])),
        ("Weed Species", NoValidator()),
        ("Density", SetValidator(valid_values=['+', '1', '2', '3-', '3+', '4', '5', '6'])),
        ("Phenological stage", SetValidator(valid_values=['A', 'B', 'C', 'D', 'E'])),
        ("Survey date", DateValidator()),
        ("Session", NoValidator()),
    ])
