################################################################################
## Form generated from reading UI file 'download.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLabel, QProgressBar, QVBoxLayout


class Ui_Download:
    def setupUi(self, Download):
        if not Download.objectName():
            Download.setObjectName("Download")
        Download.setWindowModality(Qt.WindowModality.NonModal)
        Download.resize(441, 73)
        icon = QIcon()
        icon.addFile(
            ":/icon/yt-dlp-gui.ico",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        Download.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Download)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_progress = QLabel(Download)
        self.lb_progress.setObjectName("lb_progress")

        self.verticalLayout.addWidget(
            self.lb_progress, 0, Qt.AlignmentFlag.AlignHCenter
        )

        self.pb = QProgressBar(Download)
        self.pb.setObjectName("pb")
        self.pb.setValue(0)

        self.verticalLayout.addWidget(self.pb)

        self.retranslateUi(Download)

        QMetaObject.connectSlotsByName(Download)

    # setupUi

    def retranslateUi(self, Download):
        Download.setWindowTitle(
            QCoreApplication.translate("Download", "Fetching dependency...", None)
        )
        self.lb_progress.setText(
            QCoreApplication.translate("Download", "?: 0/0 [00:00<?, ?KB/s]", None)
        )

    # retranslateUi
