from checkcel import Checkplate
from checkcel.validators import SetValidator, NoValidator
from collections import OrderedDict


class MyTemplate(Checkplate):
    validators = OrderedDict([
        ("Plot", SetValidator(valid_values=['1', '2', '3', '4', 'mixed'])),
        ("Adventice Species", NoValidator()),
        ("Density", SetValidator(valid_values=['<0.5 pl/m²', '0.5-1 pl/m²', '1-3 pl/m²', '3-10 pl/m²', '10-20 pl/m²', '20-50 pl/m²', '50-500 pl/m²', '>500 pl/m²'])),
        ("Plant growth", SetValidator(valid_values=['cotyledon', 'seedling', 'vegetative', 'flowering', 'fertilization'])),
        ("Agricultural field", NoValidator())
    ])
