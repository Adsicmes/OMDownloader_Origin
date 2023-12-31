from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from loguru import logger

from packages.services import initPreUILoaded, initAfterUILoaded
from packages.view import MainWindowV2


def runApp():
    app = QtWidgets.QApplication()

    logger.info("Executing pre initialization...")
    initPreUILoaded()
    logger.info("Successfully executed pre initialization.")

    logger.info("Initializing window...")
    wd = MainWindowV2()
    logger.info("Successfully initialized window.")

    wd.show()
    QApplication.processEvents()
    logger.info("Starting process events.")

    logger.info("Executing after-ui initialization...")
    initAfterUILoaded()
    logger.info("Successfully executed after-ui initialization.")

    logger.info("Show window.")
    app.exec()


if __name__ == '__main__':
    runApp()
