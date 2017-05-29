from events import Events

from domain.shared import exceptions
from domain.shared.decorators import getter, mutator
from domain.shared.entity import Entity
from domain.shared.types import Date, EntityId, EntityVersion


class TodoEvents(Events):
    __events__ = ('description_changed',)


class Todo(Entity):
    """
    A Todo entity.
    """

    def __init__(self, id: EntityId, description: str = "", due: Date = None,  version: EntityVersion = 0) -> None:
        super().__init__(id, version)
        self._events = TodoEvents()
        self.description = description
        self._due = due

    def __repr__(self):
        return "{d} Todo(id={e._id}, description={sd}, due={e._due}, version={e._version})".format(
            d='*Deleted*' if self._deleted else '',
            e=self,
            sd=self.short_description
        )

    @property
    @getter
    def description(self) -> str:
        return self._description

    @description.setter
    @mutator
    def description(self, value: str) -> None:
        self.validate_description(value)
        self._description = value
        self._events.description_changed()

    @staticmethod
    def validate_description(description: str) -> str:
        if len(description) < 2:
            raise exceptions.ConsistencyError("Todo description cannot be shorter than 2 characters.")

    @property
    @getter
    def short_description(self) -> str:
        return self._description if len(self._description) < 10 else self._description[:10] + '...'

