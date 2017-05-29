from abc import ABCMeta, abstractmethod

from events import Events

from domain.shared import exceptions, types


class Entity(metaclass=ABCMeta):
    """
    The base class of all entities.

    Attributes:
        id: A unique identifier
        version: An integer version.
        deleted: True if this entity should no longer be used, otherwise False.
    """

    @abstractmethod
    def __init__(self, id: types.EntityId, version: types.EntityVersion = 0) -> None:
        self._id = id
        self._version = version
        self._deleted = False
        self._events = EntityEvents()

    @abstractmethod
    def __repr__(self) -> str:
        return "{d} Entity(id={e._id}, version={e._version})".format(
            d="*Deleted*" if self._deleted else "",
            e=self
        )

    def _increment_version(self) -> None:
        self._version += 1
    
    @property
    def id(self) -> types.EntityId:
        """A string unique identifier for the entity."""
        return self._id
    
    @id.setter
    def id(self, value):
        raise exceptions.ConsistencyError("EntityId is immutable")

    @property
    def version(self):
        """An integer versions for the entity."""
        return self._version
    
    @version.setter
    def version(self, value):
        raise exceptions.ConsistencyError("Entity version can't be modified")

    @property
    def deleted(self):
       """True if this entity is marked as deleted, otherwise False."""
       return self._deleted

    def _check_not_deleted(self):
        if self._deleted:
            raise exceptions.DeletedEntityError("Attemp to use {}".format(repr(self)))


class EntityEvents(Events):
    __events__ = ('created', 'delete')
