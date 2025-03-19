# Abstract Classes - Abstract Base Class (ABC)
# ABCs are used as contracts for defining
# new classes. They can force other classes
# to create concrete methods. They can also have
# their own concrete methods.
# @abstractmethods are methods without a body.
# The rules for abstract classes with abstract
# methods are that they CANNOT be instantiated
# directly.
# Abstract methods MUST be implemented
# in subclasses (@abstractmethod).
# An abstract class in Python has its metaclass
# as ABCMeta.
# It is possible to create @property, @setter, @classmethod,
# @staticmethod, and @method as abstract, for that
# use @abstractmethod as the innermost decorator.

from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


l = LogPrintMixin()
l.log_error('Hi')
