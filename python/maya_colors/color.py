# -*- coding: utf-8 -*-
import maya.api.OpenMaya as om2
from qtpy import QtGui

class Color(object):

    def __init__(self, r=0, g=0, b=0, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.values = r, g, b, a
        self.normalized_values = tuple(i / 255.0 for i in self.values)

    def __repr__(self):
        return '{module}.{cls}({r}, {g}, {b}, {a})'.format(module=__name__, cls=type(self).__name__, r=self.r, g=self.g, b=self.b, a=self.a)

    def as_MColor(self):
        return om2.MColor(self.normalized_values)

    def as_QColor(self):
        return QtGui.QColor(*self.values)
