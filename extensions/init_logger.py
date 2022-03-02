import os
import yaml
import codecs
import logging
from logging import config
from extensions.init_dotenv import root_path


class Config:
    _cfg = {}

    @classmethod
    def load_yaml(cls, path):
        with codecs.open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    @classmethod
    def load_config(cls, config_path):
        cls._cfg = cls.load_yaml(config_path)

    @classmethod
    def get_cfg(cls):
        return cls._cfg


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class Logging:

    def __init__(self):
        self._log_cfg = None

    def init(self, log_cfg_file):
        if os.path.exists(log_cfg_file):
            with open(log_cfg_file, 'r') as f:
                self._log_cfg = yaml.safe_load(f)
                self.set_log_path()
                config.dictConfig(self._log_cfg)
        else:
            logging.basicConfig(level=logging.DEBUG)

    def set_log_path(self):
        base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        log_dir = os.path.join(base_path, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        for key in self._log_cfg["handlers"]:
            if self._log_cfg["handlers"][key].get("filename", None):
                filename = self._log_cfg["handlers"][key]["filename"]
                self._log_cfg["handlers"][key]["filename"] = os.path.join(log_dir, filename)

    def get_logger(self, logger_name):
        return logging.getLogger(logger_name)


TEST_LOGGER = Logging().get_logger("test_log")


def init_log():
    log_cfg_path = os.path.join(root_path, 'etc', 'log.yaml')
    Logging().init(log_cfg_path)