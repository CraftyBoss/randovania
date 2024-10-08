################################################################################
## Form generated from reading UI file 'remastered_game_export_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_RemasteredGameExportDialog:
    def setupUi(self, RemasteredGameExportDialog):
        if not RemasteredGameExportDialog.objectName():
            RemasteredGameExportDialog.setObjectName("RemasteredGameExportDialog")
        RemasteredGameExportDialog.resize(537, 421)
        self.root_layout = QGridLayout(RemasteredGameExportDialog)
        self.root_layout.setSpacing(6)
        self.root_layout.setContentsMargins(11, 11, 11, 11)
        self.root_layout.setObjectName("root_layout")
        self.input_file_label = QLabel(RemasteredGameExportDialog)
        self.input_file_label.setObjectName("input_file_label")
        self.input_file_label.setMaximumSize(QSize(16777215, 20))

        self.root_layout.addWidget(self.input_file_label, 1, 0, 1, 2)

        self.description_label = QLabel(RemasteredGameExportDialog)
        self.description_label.setObjectName("description_label")
        self.description_label.setWordWrap(True)

        self.root_layout.addWidget(self.description_label, 0, 0, 1, 3)

        self.target_platform_layout = QHBoxLayout()
        self.target_platform_layout.setSpacing(6)
        self.target_platform_layout.setObjectName("target_platform_layout")
        self.target_platform_label = QLabel(RemasteredGameExportDialog)
        self.target_platform_label.setObjectName("target_platform_label")

        self.target_platform_layout.addWidget(self.target_platform_label)

        self.atmosphere_radio = QRadioButton(RemasteredGameExportDialog)
        self.atmosphere_radio.setObjectName("atmosphere_radio")

        self.target_platform_layout.addWidget(self.atmosphere_radio)

        self.ryujinx_radio = QRadioButton(RemasteredGameExportDialog)
        self.ryujinx_radio.setObjectName("ryujinx_radio")

        self.target_platform_layout.addWidget(self.ryujinx_radio)

        self.ryujinx_legacy_radio = QRadioButton(RemasteredGameExportDialog)
        self.ryujinx_legacy_radio.setObjectName("ryujinx_legacy_radio")

        self.target_platform_layout.addWidget(self.ryujinx_legacy_radio)

        self.root_layout.addLayout(self.target_platform_layout, 4, 0, 1, 3)

        self.input_file_button = QPushButton(RemasteredGameExportDialog)
        self.input_file_button.setObjectName("input_file_button")
        self.input_file_button.setMaximumSize(QSize(100, 16777215))

        self.root_layout.addWidget(self.input_file_button, 2, 2, 1, 1)

        self.output_tab_widget = QTabWidget(RemasteredGameExportDialog)
        self.output_tab_widget.setObjectName("output_tab_widget")
        self.tab_sd_card = QWidget()
        self.tab_sd_card.setObjectName("tab_sd_card")
        self.verticalLayout = QVBoxLayout(self.tab_sd_card)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sd_label = QLabel(self.tab_sd_card)
        self.sd_label.setObjectName("sd_label")

        self.verticalLayout.addWidget(self.sd_label)

        self.sd_driver_layout = QHBoxLayout()
        self.sd_driver_layout.setSpacing(6)
        self.sd_driver_layout.setObjectName("sd_driver_layout")
        self.sd_combo = QComboBox(self.tab_sd_card)
        self.sd_combo.addItem("")
        self.sd_combo.setObjectName("sd_combo")

        self.sd_driver_layout.addWidget(self.sd_combo)

        self.sd_non_removable = QCheckBox(self.tab_sd_card)
        self.sd_non_removable.setObjectName("sd_non_removable")

        self.sd_driver_layout.addWidget(self.sd_non_removable)

        self.sd_refresh_button = QPushButton(self.tab_sd_card)
        self.sd_refresh_button.setObjectName("sd_refresh_button")

        self.sd_driver_layout.addWidget(self.sd_refresh_button)

        self.verticalLayout.addLayout(self.sd_driver_layout)

        self.sd_mod_manager_check = QCheckBox(self.tab_sd_card)
        self.sd_mod_manager_check.setObjectName("sd_mod_manager_check")

        self.verticalLayout.addWidget(self.sd_mod_manager_check)

        self.output_tab_widget.addTab(self.tab_sd_card, "")
        self.tab_ftp = QWidget()
        self.tab_ftp.setObjectName("tab_ftp")
        self.tab_ftp_layout = QGridLayout(self.tab_ftp)
        self.tab_ftp_layout.setSpacing(6)
        self.tab_ftp_layout.setContentsMargins(11, 11, 11, 11)
        self.tab_ftp_layout.setObjectName("tab_ftp_layout")
        self.ftp_description_label = QLabel(self.tab_ftp)
        self.ftp_description_label.setObjectName("ftp_description_label")
        self.ftp_description_label.setWordWrap(True)
        self.ftp_description_label.setOpenExternalLinks(True)

        self.tab_ftp_layout.addWidget(self.ftp_description_label, 0, 0, 1, 4)

        self.ftp_anonymous_check = QCheckBox(self.tab_ftp)
        self.ftp_anonymous_check.setObjectName("ftp_anonymous_check")

        self.tab_ftp_layout.addWidget(self.ftp_anonymous_check, 1, 0, 1, 1)

        self.ftp_username_edit = QLineEdit(self.tab_ftp)
        self.ftp_username_edit.setObjectName("ftp_username_edit")

        self.tab_ftp_layout.addWidget(self.ftp_username_edit, 1, 1, 1, 1)

        self.ftp_password_edit = QLineEdit(self.tab_ftp)
        self.ftp_password_edit.setObjectName("ftp_password_edit")

        self.tab_ftp_layout.addWidget(self.ftp_password_edit, 1, 2, 1, 2)

        self.ftp_ip_label = QLabel(self.tab_ftp)
        self.ftp_ip_label.setObjectName("ftp_ip_label")

        self.tab_ftp_layout.addWidget(self.ftp_ip_label, 2, 0, 1, 1)

        self.ftp_ip_edit = QLineEdit(self.tab_ftp)
        self.ftp_ip_edit.setObjectName("ftp_ip_edit")

        self.tab_ftp_layout.addWidget(self.ftp_ip_edit, 2, 1, 1, 1)

        self.ftp_port_edit = QLineEdit(self.tab_ftp)
        self.ftp_port_edit.setObjectName("ftp_port_edit")
        self.ftp_port_edit.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.tab_ftp_layout.addWidget(self.ftp_port_edit, 2, 2, 1, 1)

        self.ftp_test_button = QPushButton(self.tab_ftp)
        self.ftp_test_button.setObjectName("ftp_test_button")

        self.tab_ftp_layout.addWidget(self.ftp_test_button, 2, 3, 1, 1)

        self.output_tab_widget.addTab(self.tab_ftp, "")
        self.tab_ryujinx = QWidget()
        self.tab_ryujinx.setObjectName("tab_ryujinx")
        self.horizontalLayout_2 = QVBoxLayout(self.tab_ryujinx)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.layout_linux_choice = QHBoxLayout()
        self.layout_linux_choice.setSpacing(6)
        self.layout_linux_choice.setObjectName("layout_linux_choice")
        self.linux_flatpak_radio = QRadioButton(self.tab_ryujinx)
        self.linux_flatpak_radio.setObjectName("linux_flatpak_radio")
        self.linux_flatpak_radio.setChecked(True)

        self.layout_linux_choice.addWidget(self.linux_flatpak_radio)

        self.linux_native_radio = QRadioButton(self.tab_ryujinx)
        self.linux_native_radio.setObjectName("linux_native_radio")
        self.linux_native_radio.setChecked(False)

        self.layout_linux_choice.addWidget(self.linux_native_radio)

        self.horizontalLayout_2.addLayout(self.layout_linux_choice)

        self.ryujinx_label = QLabel(self.tab_ryujinx)
        self.ryujinx_label.setObjectName("ryujinx_label")
        self.ryujinx_label.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.ryujinx_label)

        self.output_tab_widget.addTab(self.tab_ryujinx, "")
        self.tab_custom_path = QWidget()
        self.tab_custom_path.setObjectName("tab_custom_path")
        self.gridLayout_3 = QGridLayout(self.tab_custom_path)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.custom_path_edit = QLineEdit(self.tab_custom_path)
        self.custom_path_edit.setObjectName("custom_path_edit")

        self.gridLayout_3.addWidget(self.custom_path_edit, 1, 0, 1, 1)

        self.custom_path_button = QPushButton(self.tab_custom_path)
        self.custom_path_button.setObjectName("custom_path_button")
        self.custom_path_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.custom_path_button, 1, 1, 1, 1)

        self.custom_path_label = QLabel(self.tab_custom_path)
        self.custom_path_label.setObjectName("custom_path_label")
        self.custom_path_label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.custom_path_label, 0, 0, 1, 2)

        self.output_tab_widget.addTab(self.tab_custom_path, "")

        self.root_layout.addWidget(self.output_tab_widget, 6, 0, 2, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.root_layout.addItem(self.verticalSpacer, 5, 0, 1, 3)

        self.auto_save_spoiler_check = QCheckBox(RemasteredGameExportDialog)
        self.auto_save_spoiler_check.setObjectName("auto_save_spoiler_check")

        self.root_layout.addWidget(self.auto_save_spoiler_check, 9, 0, 1, 1)

        self.accept_button = QPushButton(RemasteredGameExportDialog)
        self.accept_button.setObjectName("accept_button")

        self.root_layout.addWidget(self.accept_button, 10, 0, 1, 1)

        self.cancel_button = QPushButton(RemasteredGameExportDialog)
        self.cancel_button.setObjectName("cancel_button")

        self.root_layout.addWidget(self.cancel_button, 10, 2, 1, 1)

        self.line = QFrame(RemasteredGameExportDialog)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.root_layout.addWidget(self.line, 3, 0, 1, 3)

        self.input_file_edit = QLineEdit(RemasteredGameExportDialog)
        self.input_file_edit.setObjectName("input_file_edit")

        self.root_layout.addWidget(self.input_file_edit, 2, 0, 1, 2)

        self.retranslateUi(RemasteredGameExportDialog)

        self.output_tab_widget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(RemasteredGameExportDialog)

    # setupUi

    def retranslateUi(self, RemasteredGameExportDialog):
        RemasteredGameExportDialog.setWindowTitle(
            QCoreApplication.translate("RemasteredGameExportDialog", "Game Patching", None)
        )
        self.input_file_label.setText(
            QCoreApplication.translate(
                "RemasteredGameExportDialog", "Input Path (Unmodified Remastered extracted RomFS)", None
            )
        )
        self.description_label.setText(
            QCoreApplication.translate(
                "RemasteredGameExportDialog",
                "<html><head/><body><p>In order to create the randomized game, an extracted RomFS of Metroid Prime Remastered for the Nintendo Switch is necessary.</p></body></html>",
                None,
            )
        )
        self.target_platform_label.setText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Target Platform", None)
        )
        self.atmosphere_radio.setText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Atmosph\u00e8re (Modded Switch)", None)
        )
        # if QT_CONFIG(tooltip)
        self.ryujinx_radio.setToolTip(
            QCoreApplication.translate(
                "RemasteredGameExportDialog",
                "<html><head/><body><p>Randovania only supports Ryujinx.</p><p>Use other emulators at your own risk, but do not report any issues.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.ryujinx_radio.setText(QCoreApplication.translate("RemasteredGameExportDialog", "Ryujinx", None))
        # if QT_CONFIG(tooltip)
        self.ryujinx_legacy_radio.setToolTip(
            QCoreApplication.translate(
                "RemasteredGameExportDialog",
                "<html><head/><body><p>Same as Ryujinx, but does not use exlaunch. Use in case the normal option does not work.</p><p>This mode is not compatible with Multiworld or Auto Tracker enabled.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.ryujinx_legacy_radio.setText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Ryujinx (Legacy)", None)
        )
        self.input_file_button.setText(QCoreApplication.translate("RemasteredGameExportDialog", "Select File", None))
        self.sd_label.setText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Select the drive letter for your SD Card", None)
        )
        self.sd_combo.setItemText(0, QCoreApplication.translate("RemasteredGameExportDialog", "D:", None))

        self.sd_non_removable.setText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Show non-removable", None)
        )
        self.sd_refresh_button.setText(QCoreApplication.translate("RemasteredGameExportDialog", "Refresh", None))
        self.sd_mod_manager_check.setText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Use path compatible with SimpleModManager", None)
        )
        self.output_tab_widget.setTabText(
            self.output_tab_widget.indexOf(self.tab_sd_card),
            QCoreApplication.translate("RemasteredGameExportDialog", "SD Card", None),
        )
        self.ftp_description_label.setText(
            QCoreApplication.translate(
                "RemasteredGameExportDialog",
                '<html><head/><body><p>Upload the exported mod directly to your Switch, via FTP, to a path compatible with <a href="https://github.com/nadrino/SimpleModManager/blob/master/README.md"><span style=" text-decoration: underline; color:#007af4;">SimpleModManager</span></a>.</p><p>In order to provide a FTP server in your Switch, run either <a href="https://github.com/mtheall/ftpd"><span style=" text-decoration: underline; color:#007af4;">ftpd</span></a> or <a href="https://github.com/jakibaki/sys-ftpd"><span style=" text-decoration: underline; color:#007af4;">sys-ftpd</span></a> as homebrew.</p></body></html>',
                None,
            )
        )
        self.ftp_anonymous_check.setText(QCoreApplication.translate("RemasteredGameExportDialog", "Anonymous", None))
        self.ftp_username_edit.setPlaceholderText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Username", None)
        )
        self.ftp_password_edit.setPlaceholderText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Password", None)
        )
        self.ftp_ip_label.setText(QCoreApplication.translate("RemasteredGameExportDialog", "Switch IP", None))
        self.ftp_port_edit.setText(QCoreApplication.translate("RemasteredGameExportDialog", "21", None))
        self.ftp_test_button.setText(QCoreApplication.translate("RemasteredGameExportDialog", "Test connection", None))
        self.output_tab_widget.setTabText(
            self.output_tab_widget.indexOf(self.tab_ftp),
            QCoreApplication.translate("RemasteredGameExportDialog", "Upload via FTP", None),
        )
        self.linux_flatpak_radio.setText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Use Flatpak Ryujinx folder", None)
        )
        self.linux_native_radio.setText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Use native Ryujinx folder", None)
        )
        self.ryujinx_label.setText(
            QCoreApplication.translate(
                "RemasteredGameExportDialog",
                '<html><head/><body><p>The game will be exported directly to Ryujinx\'s mod folder for Metroid Dread in this computer.</p><p>Path to be used:<br/><span style=" font-size:8pt;">{mod_path}</span></p><p>Please make sure Ryujinx is closed before exporting a game.</p></body></html>',
                None,
            )
        )
        self.output_tab_widget.setTabText(
            self.output_tab_widget.indexOf(self.tab_ryujinx),
            QCoreApplication.translate("RemasteredGameExportDialog", "Ryujinx", None),
        )
        self.custom_path_edit.setPlaceholderText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Path where to place randomized game", None)
        )
        self.custom_path_button.setText(QCoreApplication.translate("RemasteredGameExportDialog", "Select File", None))
        self.custom_path_label.setText(
            QCoreApplication.translate(
                "RemasteredGameExportDialog",
                "<html><head/><body><p>Saves the mod to a path or your choosing, leaving the responsibility of placing the files in the correct location to you.</p><p>This path and input path are not allowed to contain the other.</p><p>It's recommended to use one of the other options.</p></body></html>",
                None,
            )
        )
        self.output_tab_widget.setTabText(
            self.output_tab_widget.indexOf(self.tab_custom_path),
            QCoreApplication.translate("RemasteredGameExportDialog", "Custom Path", None),
        )
        self.auto_save_spoiler_check.setText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Include a spoiler log on same directory", None)
        )
        self.accept_button.setText(QCoreApplication.translate("RemasteredGameExportDialog", "Accept", None))
        self.cancel_button.setText(QCoreApplication.translate("RemasteredGameExportDialog", "Cancel", None))
        self.input_file_edit.setPlaceholderText(
            QCoreApplication.translate("RemasteredGameExportDialog", "Path to vanilla extracted RomFS", None)
        )

    # retranslateUi
