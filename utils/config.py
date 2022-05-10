import configparser


class MyConfig:
    _data = None

    def load_config(self, path):
        self._data = configparser.ConfigParser()
        self._data.read(path)

    def get_config(self):
        return self._data
