# Abstraction
# Inheritance - is a type of relationship
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implement the log method')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        formatted_msg = f'{msg} ({self.__class__.__name__})'
        print('Saving to log:', formatted_msg)
        with open(LOG_FILE, 'a') as file:
            file.write(formatted_msg)
            file.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('something went wrong')
    lp.log_success('that is great')
    lf = LogFileMixin()
    lf.log_error('something went wrong')
    lf.log_success('that is great')
