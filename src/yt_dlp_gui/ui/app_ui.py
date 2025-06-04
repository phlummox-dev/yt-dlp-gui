# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QToolButton, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
from . import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(816, 622)
        icon = QIcon()
        icon.addFile(u":/icon/yt-dlp-gui.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(9)
        self.centralwidget.setFont(font)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_controls = QGroupBox(self.centralwidget)
        self.gb_controls.setObjectName(u"gb_controls")
        self.verticalLayout_2 = QVBoxLayout(self.gb_controls)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.add_btn = QPushButton(self.gb_controls)
        self.add_btn.setObjectName(u"add_btn")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_btn.setIcon(icon1)
        self.add_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.add_btn)

        self.clear_btn = QPushButton(self.gb_controls)
        self.clear_btn.setObjectName(u"clear_btn")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear_btn.setIcon(icon2)
        self.clear_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.clear_btn)

        self.download_btn = QPushButton(self.gb_controls)
        self.download_btn.setObjectName(u"download_btn")
        icon3 = QIcon()
        icon3.addFile(u":/buttons/download.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.download_btn.setIcon(icon3)
        self.download_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.download_btn)


        self.gridLayout.addWidget(self.gb_controls, 0, 2, 1, 1)

        self.gb_embeds = QGroupBox(self.centralwidget)
        self.gb_embeds.setObjectName(u"gb_embeds")
        self.gb_embeds.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.gb_embeds.setFlat(False)
        self.gb_embeds.setCheckable(False)
        self.verticalLayout_3 = QVBoxLayout(self.gb_embeds)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.gb_embeds)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.sponsorblock_combo = QComboBox(self.gb_embeds)
        self.sponsorblock_combo.addItem("")
        self.sponsorblock_combo.addItem("")
        self.sponsorblock_combo.addItem("")
        self.sponsorblock_combo.setObjectName(u"sponsorblock_combo")

        self.horizontalLayout.addWidget(self.sponsorblock_combo)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.metadata_check = QCheckBox(self.gb_embeds)
        self.metadata_check.setObjectName(u"metadata_check")

        self.verticalLayout_3.addWidget(self.metadata_check)

        self.thumbnail_check = QCheckBox(self.gb_embeds)
        self.thumbnail_check.setObjectName(u"thumbnail_check")

        self.verticalLayout_3.addWidget(self.thumbnail_check)

        self.subtitles_check = QCheckBox(self.gb_embeds)
        self.subtitles_check.setObjectName(u"subtitles_check")

        self.verticalLayout_3.addWidget(self.subtitles_check)


        self.gridLayout.addWidget(self.gb_embeds, 0, 1, 1, 1)

        self.gb_status = QGroupBox(self.centralwidget)
        self.gb_status.setObjectName(u"gb_status")
        self.gridLayout_3 = QGridLayout(self.gb_status)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tw = QTreeWidget(self.gb_status)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        self.tw.setHeaderItem(__qtreewidgetitem)
        self.tw.setObjectName(u"tw")
        self.tw.header().setVisible(True)

        self.gridLayout_3.addWidget(self.tw, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.gb_status, 1, 0, 1, 3)

        self.gb_params = QGroupBox(self.centralwidget)
        self.gb_params.setObjectName(u"gb_params")
        self.verticalLayout_5 = QVBoxLayout(self.gb_params)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.link_lbl = QLabel(self.gb_params)
        self.link_lbl.setObjectName(u"link_lbl")
        self.link_lbl.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.link_lbl)

        self.link_edit = QLineEdit(self.gb_params)
        self.link_edit.setObjectName(u"link_edit")
        self.link_edit.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.link_edit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.path_lbl = QLabel(self.gb_params)
        self.path_lbl.setObjectName(u"path_lbl")
        self.path_lbl.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.path_lbl)

        self.path_edit = QLineEdit(self.gb_params)
        self.path_edit.setObjectName(u"path_edit")
        self.path_edit.setEnabled(True)
        self.path_edit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.path_edit)

        self.path_btn = QToolButton(self.gb_params)
        self.path_btn.setObjectName(u"path_btn")

        self.horizontalLayout_3.addWidget(self.path_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.format_lbl = QLabel(self.gb_params)
        self.format_lbl.setObjectName(u"format_lbl")
        self.format_lbl.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.format_lbl)

        self.format_combo = QComboBox(self.gb_params)
        self.format_combo.setObjectName(u"format_combo")

        self.horizontalLayout_2.addWidget(self.format_combo)

        self.save_preset_btn = QPushButton(self.gb_params)
        self.save_preset_btn.setObjectName(u"save_preset_btn")

        self.horizontalLayout_2.addWidget(self.save_preset_btn)

        self.filename_lbl = QLabel(self.gb_params)
        self.filename_lbl.setObjectName(u"filename_lbl")

        self.horizontalLayout_2.addWidget(self.filename_lbl)

        self.filename_edit = QLineEdit(self.gb_params)
        self.filename_edit.setObjectName(u"filename_edit")
        self.filename_edit.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.filename_edit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.gb_params, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.add_btn, self.clear_btn)
        QWidget.setTabOrder(self.clear_btn, self.download_btn)
        QWidget.setTabOrder(self.download_btn, self.tw)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"yt-dlp-gui", None))
        self.gb_controls.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
#if QT_CONFIG(tooltip)
        self.add_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.add_btn.setText("")
#if QT_CONFIG(tooltip)
        self.clear_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Clear</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.clear_btn.setText("")
#if QT_CONFIG(tooltip)
        self.download_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Download</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.download_btn.setText("")
        self.gb_embeds.setTitle(QCoreApplication.translate("MainWindow", u"Optional", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SponsorBlock", None))
        self.sponsorblock_combo.setItemText(0, "")
        self.sponsorblock_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"remove", None))
        self.sponsorblock_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"mark", None))

        self.metadata_check.setText(QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.thumbnail_check.setText(QCoreApplication.translate("MainWindow", u"Thumbnail", None))
        self.subtitles_check.setText(QCoreApplication.translate("MainWindow", u"Subtitles", None))
        self.gb_status.setTitle(QCoreApplication.translate("MainWindow", u"Downloads", None))
        ___qtreewidgetitem = self.tw.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"ETA", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Progress", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Format", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Title", None));
        self.gb_params.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.link_lbl.setText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.link_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://www.youtube.com/watch?v=dQw4w9WgXcQ", None))
        self.path_lbl.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.path_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.format_lbl.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.save_preset_btn.setText(QCoreApplication.translate("MainWindow", u"Save Preset", None))
        self.filename_lbl.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.filename_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%(title)s.%(ext)s", None))
    # retranslateUi

