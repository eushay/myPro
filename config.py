import configparser

class Config():

    _data = None

    def load_config(self, file_path: str) -> None:
        self._data = configparser.ConfigParser()
        self._data.read(file_path)

    def get_config(self):
        return self._data