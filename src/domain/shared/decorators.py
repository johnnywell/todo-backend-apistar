"""Domain shared decorators"""
from functools import wraps


def mutator(method):
    @wraps(method)
    def _decorator(self, *args, **kwargs):
        self._check_not_deleted()
        method(self, *args, **kwargs)
        self._increment_version()
    return _decorator


def getter(method):
    @wraps(method)
    def _decorator(self, *args, **kwargs):
        self._check_not_deleted()
        method(self, *args, **kwargs)
    return _decorator