# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)
from . import icons_rc

class Ui_Download(object):
    def setupUi(self, Download):
        if not Download.objectName():
            Download.setObjectName(u"Download")
        Download.setWindowModality(Qt.WindowModality.NonModal)
        Download.resize(441, 73)
        icon = QIcon()
        icon.addFile(u":/icon/yt-dlp-gui.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Download.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Download)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progress_lbl = QLabel(Download)
        self.progress_lbl.setObjectName(u"progress_lbl")

        self.verticalLayout.addWidget(self.progress_lbl, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pb = QProgressBar(Download)
        self.pb.setObjectName(u"pb")
        self.pb.setValue(0)

        self.verticalLayout.addWidget(self.pb)


        self.retranslateUi(Download)

        QMetaObject.connectSlotsByName(Download)
    # setupUi

    def retranslateUi(self, Download):
        Download.setWindowTitle(QCoreApplication.translate("Download", u"Fetching dependency...", None))
        self.progress_lbl.setText(QCoreApplication.translate("Download", u"?: 0/0 [00:00<?, ?KB/s]", None))
    # retranslateUi

