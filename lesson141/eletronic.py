from log import LogFileMixin


class Electronic:
    def __init__(self, name):
        self._name = name
        self._is_on = False

    def turn_on(self):
        if not self._is_on:
            self._is_on = True

    def turn_off(self):
        if self._is_on:
            self._is_on = False


class Smartphone(Electronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()

        if self._is_on:
            msg = f'{self._name} is now ON'
            self.log_success(msg)

    def turn_off(self):
        super().turn_off()

        if not self._is_on:
            msg = f'{self._name} is now OFF'
            self.log_error(msg)
