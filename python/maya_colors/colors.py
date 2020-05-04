# -*- coding: utf-8 -*-
from collections import OrderedDict
import cud_colors.colors as cud_colors_
import color

cud_colors = OrderedDict()

for key, values in cud_colors_.all_colors.items():
    cud_colors[key] = color.Color(*values)
