# -*- coding: utf-8 -*-
import maya.api.OpenMaya as om2
from qtpy import *

class Color(object):

    def __init__(self, r=0, g=0, b=0):
        self.r, self.g, self.b = r, g, b
        self.values = r, g, b

    def as_QColor(self):
        return om2.MColor((i / 255.0 for i in self.values))

    def as_MColor(self):
        return QtGui.QColor(*self.values)
