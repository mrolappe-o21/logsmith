import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QColor

script_dir = os.path.dirname(os.path.realpath(__file__))


class Assets:
    def __init__(self):
        self.cloud = self._resource_path('assets/cloud.svg')
        self.cloud_outline = self._resource_path('assets/cloud-outline.svg')
        self.cloud_done = self._resource_path('assets/cloud-done.svg')
        self.bug = self._resource_path('assets/bug.svg')
        self.standard = self.get_icon()

    def get_icon(self, style='full', color_code='#FFFFFF'):
        if style == 'outline':
            return self._color_icon(self.cloud_outline, color_code)
        if style == 'error':
            return self._color_icon(self.bug, color_code)
        else:
            return self._color_icon(self.cloud, color_code)

    @staticmethod
    def _color_icon(icon, color_code):
        pix_map = QPixmap(icon)
        mask = pix_map.createMaskFromColor(QColor('black'), Qt.MaskOutColor)
        pix_map.fill(QColor(color_code))
        pix_map.setMask(mask)
        return QIcon(pix_map)

    @staticmethod
    def _resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath('.'), f'{script_dir}/../{relative_path}')
