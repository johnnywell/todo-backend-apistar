"""Definition of Domain Exceptiosn"""


class ConsistencyError(Exception):
    """To be raised when an internal consistency problem is detected."""
    pass


class DeletedEntityError(Exception):
    """Raised when an attempt is made to use a deleted Entity."""
    pass
