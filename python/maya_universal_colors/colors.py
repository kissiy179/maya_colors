# -*- coding: utf-8 -*-
from collections import OrderedDict
import universal_colors.colors as universal_colors_
import color

colors = OrderedDict()

for key, values in universal_colors_.colors.colors.items():
    colors[key] = color.Color(*values)
