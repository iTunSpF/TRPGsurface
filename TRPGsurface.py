# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TRPGsurface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TRPGsurface(object):
    def setupUi(self, TRPGsurface):
        TRPGsurface.setObjectName("TRPGsurface")
        TRPGsurface.resize(641, 792)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TRPGsurface.sizePolicy().hasHeightForWidth())
        TRPGsurface.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 42, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 42, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 42, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 42, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        TRPGsurface.setPalette(palette)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(TRPGsurface)
        self.horizontalLayout_7.setContentsMargins(-1, -1, 9, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.line_12 = QtWidgets.QFrame(TRPGsurface)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_6.addWidget(self.line_12)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.line_14 = QtWidgets.QFrame(TRPGsurface)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_7.addWidget(self.line_14)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fontsize_on = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontsize_on.sizePolicy().hasHeightForWidth())
        self.fontsize_on.setSizePolicy(sizePolicy)
        self.fontsize_on.setMinimumSize(QtCore.QSize(80, 40))
        self.fontsize_on.setMaximumSize(QtCore.QSize(300, 110))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.fontsize_on.setFont(font)
        self.fontsize_on.setObjectName("fontsize_on")
        self.horizontalLayout.addWidget(self.fontsize_on)
        self.fontsize_off = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontsize_off.sizePolicy().hasHeightForWidth())
        self.fontsize_off.setSizePolicy(sizePolicy)
        self.fontsize_off.setMinimumSize(QtCore.QSize(80, 40))
        self.fontsize_off.setMaximumSize(QtCore.QSize(300, 110))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.fontsize_off.setFont(font)
        self.fontsize_off.setObjectName("fontsize_off")
        self.horizontalLayout.addWidget(self.fontsize_off)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.line_10 = QtWidgets.QFrame(TRPGsurface)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_7.addWidget(self.line_10)
        self.calendar = QtWidgets.QCalendarWidget(TRPGsurface)
        self.calendar.setSelectedDate(QtCore.QDate(1918, 7, 11))
        self.calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendar.setObjectName("calendar")
        self.verticalLayout_7.addWidget(self.calendar)
        self.line_3 = QtWidgets.QFrame(TRPGsurface)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.add3hour = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add3hour.sizePolicy().hasHeightForWidth())
        self.add3hour.setSizePolicy(sizePolicy)
        self.add3hour.setMinimumSize(QtCore.QSize(80, 40))
        self.add3hour.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.add3hour.setFont(font)
        self.add3hour.setObjectName("add3hour")
        self.verticalLayout_10.addWidget(self.add3hour)
        self.add1hour = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add1hour.sizePolicy().hasHeightForWidth())
        self.add1hour.setSizePolicy(sizePolicy)
        self.add1hour.setMinimumSize(QtCore.QSize(80, 40))
        self.add1hour.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.add1hour.setFont(font)
        self.add1hour.setObjectName("add1hour")
        self.verticalLayout_10.addWidget(self.add1hour)
        self.label_9 = QtWidgets.QLabel(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(80, 40))
        self.label_9.setMaximumSize(QtCore.QSize(300, 130))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.minus1hour = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus1hour.sizePolicy().hasHeightForWidth())
        self.minus1hour.setSizePolicy(sizePolicy)
        self.minus1hour.setMinimumSize(QtCore.QSize(80, 40))
        self.minus1hour.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.minus1hour.setFont(font)
        self.minus1hour.setObjectName("minus1hour")
        self.verticalLayout_10.addWidget(self.minus1hour)
        self.minus3hour = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus3hour.sizePolicy().hasHeightForWidth())
        self.minus3hour.setSizePolicy(sizePolicy)
        self.minus3hour.setMinimumSize(QtCore.QSize(80, 40))
        self.minus3hour.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.minus3hour.setFont(font)
        self.minus3hour.setObjectName("minus3hour")
        self.verticalLayout_10.addWidget(self.minus3hour)
        self.verticalLayout_4.addLayout(self.verticalLayout_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.add10min = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add10min.sizePolicy().hasHeightForWidth())
        self.add10min.setSizePolicy(sizePolicy)
        self.add10min.setMinimumSize(QtCore.QSize(80, 40))
        self.add10min.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.add10min.setFont(font)
        self.add10min.setObjectName("add10min")
        self.verticalLayout_11.addWidget(self.add10min)
        self.add5min = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add5min.sizePolicy().hasHeightForWidth())
        self.add5min.setSizePolicy(sizePolicy)
        self.add5min.setMinimumSize(QtCore.QSize(80, 40))
        self.add5min.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.add5min.setFont(font)
        self.add5min.setObjectName("add5min")
        self.verticalLayout_11.addWidget(self.add5min)
        self.label_10 = QtWidgets.QLabel(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(80, 40))
        self.label_10.setMaximumSize(QtCore.QSize(300, 130))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.minus5min = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus5min.sizePolicy().hasHeightForWidth())
        self.minus5min.setSizePolicy(sizePolicy)
        self.minus5min.setMinimumSize(QtCore.QSize(80, 40))
        self.minus5min.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.minus5min.setFont(font)
        self.minus5min.setObjectName("minus5min")
        self.verticalLayout_11.addWidget(self.minus5min)
        self.minus10min = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus10min.sizePolicy().hasHeightForWidth())
        self.minus10min.setSizePolicy(sizePolicy)
        self.minus10min.setMinimumSize(QtCore.QSize(80, 40))
        self.minus10min.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.minus10min.setFont(font)
        self.minus10min.setObjectName("minus10min")
        self.verticalLayout_11.addWidget(self.minus10min)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.line_4 = QtWidgets.QFrame(TRPGsurface)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_7.addWidget(self.line_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 35))
        self.label_4.setMaximumSize(QtCore.QSize(80, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.place_pathchooser = QtWidgets.QPushButton(TRPGsurface)
        self.place_pathchooser.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.place_pathchooser.sizePolicy().hasHeightForWidth())
        self.place_pathchooser.setSizePolicy(sizePolicy)
        self.place_pathchooser.setMinimumSize(QtCore.QSize(0, 35))
        self.place_pathchooser.setMaximumSize(QtCore.QSize(90, 240))
        self.place_pathchooser.setObjectName("place_pathchooser")
        self.horizontalLayout_3.addWidget(self.place_pathchooser)
        self.place_combo = QtWidgets.QComboBox(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.place_combo.sizePolicy().hasHeightForWidth())
        self.place_combo.setSizePolicy(sizePolicy)
        self.place_combo.setMinimumSize(QtCore.QSize(0, 40))
        self.place_combo.setMaximumSize(QtCore.QSize(999, 240))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.place_combo.setFont(font)
        self.place_combo.setObjectName("place_combo")
        self.horizontalLayout_3.addWidget(self.place_combo)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 35))
        self.label_5.setMaximumSize(QtCore.QSize(80, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.character_pathchooser = QtWidgets.QPushButton(TRPGsurface)
        self.character_pathchooser.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.character_pathchooser.sizePolicy().hasHeightForWidth())
        self.character_pathchooser.setSizePolicy(sizePolicy)
        self.character_pathchooser.setMinimumSize(QtCore.QSize(0, 35))
        self.character_pathchooser.setMaximumSize(QtCore.QSize(90, 240))
        self.character_pathchooser.setObjectName("character_pathchooser")
        self.horizontalLayout_4.addWidget(self.character_pathchooser)
        self.character_combo = QtWidgets.QComboBox(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.character_combo.sizePolicy().hasHeightForWidth())
        self.character_combo.setSizePolicy(sizePolicy)
        self.character_combo.setMinimumSize(QtCore.QSize(0, 40))
        self.character_combo.setMaximumSize(QtCore.QSize(999, 240))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.character_combo.setFont(font)
        self.character_combo.setObjectName("character_combo")
        self.horizontalLayout_4.addWidget(self.character_combo)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.clear_button = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setMinimumSize(QtCore.QSize(0, 40))
        self.clear_button.setMaximumSize(QtCore.QSize(9999, 200))
        font = QtGui.QFont()
        font.setFamily("????????????????????? M")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_5.addWidget(self.clear_button)
        self.apply_button = QtWidgets.QPushButton(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_button.sizePolicy().hasHeightForWidth())
        self.apply_button.setSizePolicy(sizePolicy)
        self.apply_button.setMinimumSize(QtCore.QSize(0, 40))
        self.apply_button.setMaximumSize(QtCore.QSize(9999, 200))
        font = QtGui.QFont()
        font.setFamily("????????????????????? M")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.apply_button.setFont(font)
        self.apply_button.setAutoFillBackground(False)
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout_5.addWidget(self.apply_button)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.line_11 = QtWidgets.QFrame(TRPGsurface)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_7.addWidget(self.line_11)
        self.label = QtWidgets.QLabel(TRPGsurface)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(2, 4)
        self.verticalLayout_7.setStretch(4, 4)
        self.verticalLayout_7.setStretch(6, 4)
        self.verticalLayout_7.setStretch(8, 4)
        self.verticalLayout_7.setStretch(9, 6)
        self.verticalLayout_7.setStretch(11, 1)
        self.verticalLayout_7.setStretch(12, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.line_7 = QtWidgets.QFrame(TRPGsurface)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_6.addWidget(self.line_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.text_Browser = QtWidgets.QTextBrowser(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_Browser.sizePolicy().hasHeightForWidth())
        self.text_Browser.setSizePolicy(sizePolicy)
        self.text_Browser.setMinimumSize(QtCore.QSize(320, 0))
        self.text_Browser.setMaximumSize(QtCore.QSize(99999, 160))
        self.text_Browser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.text_Browser.setObjectName("text_Browser")
        self.verticalLayout_8.addWidget(self.text_Browser)
        self.character_image = QtWidgets.QGraphicsView(TRPGsurface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.character_image.sizePolicy().hasHeightForWidth())
        self.character_image.setSizePolicy(sizePolicy)
        self.character_image.setMinimumSize(QtCore.QSize(0, 300))
        self.character_image.setMaximumSize(QtCore.QSize(1200, 2400))
        self.character_image.setObjectName("character_image")
        self.verticalLayout_8.addWidget(self.character_image)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(2, 7)
        self.verticalLayout_8.setStretch(3, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.line_13 = QtWidgets.QFrame(TRPGsurface)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout_6.addWidget(self.line_13)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(3, 2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.retranslateUi(TRPGsurface)
        QtCore.QMetaObject.connectSlotsByName(TRPGsurface)

    def retranslateUi(self, TRPGsurface):
        _translate = QtCore.QCoreApplication.translate
        TRPGsurface.setWindowTitle(_translate("TRPGsurface", "????????????????????????"))
        self.fontsize_on.setText(_translate("TRPGsurface", "?????? +"))
        self.fontsize_off.setText(_translate("TRPGsurface", "?????? -"))
        self.add3hour.setText(_translate("TRPGsurface", "+3 ??????"))
        self.add1hour.setText(_translate("TRPGsurface", "+1 ??????"))
        self.label_9.setText(_translate("TRPGsurface", "??????"))
        self.minus1hour.setText(_translate("TRPGsurface", "-1 ??????"))
        self.minus3hour.setText(_translate("TRPGsurface", "-3 ??????"))
        self.add10min.setText(_translate("TRPGsurface", "+10 ??????"))
        self.add5min.setText(_translate("TRPGsurface", "+5 ??????"))
        self.label_10.setText(_translate("TRPGsurface", "??????"))
        self.minus5min.setText(_translate("TRPGsurface", "-5 ??????"))
        self.minus10min.setText(_translate("TRPGsurface", "-10 ??????"))
        self.label_4.setText(_translate("TRPGsurface", "??????"))
        self.place_pathchooser.setText(_translate("TRPGsurface", "????????????"))
        self.label_5.setText(_translate("TRPGsurface", "??????"))
        self.character_pathchooser.setText(_translate("TRPGsurface", "????????????"))
        self.clear_button.setText(_translate("TRPGsurface", "kp"))
        self.apply_button.setText(_translate("TRPGsurface", "??????"))
        self.label.setText(_translate("TRPGsurface", "ver 1.0.0 ---- ???"))
        self.text_Browser.setHtml(_translate("TRPGsurface", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">1918 ???</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">7 ??? 14 ???</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">?????? </span><span style=\" font-size:36pt; font-weight:600; color:#0011ff;\">13:00</span><span style=\" font-size:36pt; font-weight:600;\"> </span></p></body></html>"))
