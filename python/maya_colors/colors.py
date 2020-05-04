# -*- coding: utf-8 -*-
from collections import OrderedDict
import cud_colors.colors as cud_colors_
import color

colors = OrderedDict()

for key, values in cud_colors_.colors.all_colors.items():
    colors[key] = color.Color(*values)
