from rezgui.qt import QtCore, QtGui
from rez.packages_ import Package
from rez.package_search import get_plugins

class PluginsList(QtGui.QTableWidget):
    def __init__(self, parent=None):
        super(PluginsList, self).__init__(0, 1, parent)

        self.plugins = []
        self.variant = None
        self.allow_selection = False

        self.setGridStyle(QtCore.Qt.DotLine)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)

        hh = self.horizontalHeader()
        hh.setStretchLastSection(True)
        hh.setVisible(False)
        vh = self.verticalHeader()
        vh.setResizeMode(QtGui.QHeaderView.ResizeToContents)
        vh.setVisible(False)

    def set_package(self, package):
        self.clear()
        if package is not None:
            plugins = self.plugins or get_plugins(package_name=package.name)
            self.setRowCount(len(plugins))
            for i, package_name in enumerate(plugins):
                item = QtGui.QTableWidgetItem(package_name)
                self.setItem(i, 0, item)

        self.plugins = plugins
        self.variant = None

    def set_variant(self, variant):
        self.clear()
        if variant is not None:
            if isinstance(variant, Package):
                self.set_package(variant)
                return

            self.set_package(variant.parent)


        self.variant = variant

    def selectionCommand(self, index, event=None):
        return QtGui.QItemSelectionModel.ClearAndSelect if self.allow_selection \
            else QtGui.QItemSelectionModel.NoUpdate
