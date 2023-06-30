import configparser
import os
from typing import TypedDict, Literal

from packages.utils import getSysUsername

CFG_PATH = f'config.{getSysUsername()}.ini'
DEFAULT_CFG = """
[View]
; All view-related configurations
i18nLanguage=auto
theme=auto
themeColor=auto

[Queue]
; All queue-related configurations
maxTaskCount=3
""".strip()


class SectionView(TypedDict):
    i18nLanguage: str
    theme: str
    themeColor: str


class Queue(TypedDict):
    maxTaskCount: int


class ConfigItem(TypedDict):
    view: SectionView
    queue: Queue


class Config:
    _config: ConfigItem

    _cfg: configparser.ConfigParser

    def __init__(self):
        self._cfg = self._readCfgFile()

        self._config = ConfigItem(
            view=SectionView(
                i18nLanguage=self._cfg.get("View", "i18nLanguage"),
                theme=self._cfg.get("View", "theme"),
                themeColor=self._cfg.get("View", "themeColor")
            ),
            queue=Queue(
                maxTaskCount=int(self._cfg.get("Queue", "maxTaskCount"))
            )
        )

    def __getitem__(self, item):
        return self._config[item]

    @staticmethod
    def _readCfgFile():
        """
        try to read config ini, if not found, create a new one
        and write default config text into it
        """
        cfg_file = configparser.ConfigParser()

        if not os.path.exists(CFG_PATH):
            with open(CFG_PATH, "w") as cfg:
                cfg.write(DEFAULT_CFG)

        cfg_file.read(CFG_PATH)
        return cfg_file

    def setViewI18nLanguage(self, value: str):
        self._config["view"]["i18nLanguage"] = value

    def setViewTheme(self, theme: Literal["dark", "light", "auto"]):
        self._config["view"]["theme"] = theme

    def setViewThemeColor(self, color: str):
        self._config["view"]["themeColor"] = color

    def setItem(self, section: str, item: str, value):
        self._config[section][item] = value
        self._cfg.set(section, item, value)
        self._save()

    def _save(self):
        self._cfg.write(open(CFG_PATH, "w"))


config = Config()  # cfg after handle