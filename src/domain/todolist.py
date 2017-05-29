from events import Events

from domain.shared import exceptions, types
from domain.shared.decorators import mutator
from domain.shared.entity import Entity


class TodoListEvents(Events):
    __events__ = ('created', 'deleted', 'name_changed', 'todo_added', 
                  'todo_destroyed', 'todo_toggled', 'all_todos_toggled')


class TodoList(Entity):
    """
    A Todo List which hold Todo itens and handle it's status
    """

    def __init__(self, id: types.EntityId, name: str, version: types.EntityVersion = 0) -> None:
        """
        Initialize a TodoList.

        Do NOT call it directly. Use the actory method.
        """
        super().__init__(id, version)
        self._events = TodoListEvents()
        self.name = name
        self._todos = []

    def __repr__(self):
        return "{d} TodoList(id={e._id}, name={e._name}, version={e._version}, todos=[0..{n}])".format(
            d='*Deleted*' if self._deleted else '',
            e=self,
            n=len(self._todos))

    @property
    def name(self) -> str:
        """The name of this Todo List."""
        self._check_not_deleted()
        return self._name

    @staticmethod
    def validate_name(name: str) -> str:
        if len(name) < 1:
            raise exceptions.ConsistencyError("TodoList name cannot be empty")
        return name
    
    @name.setter
    @mutator
    def name(self, value: str) -> None:
        self.validate_name(value)
        self._name = value
        self._events.name_changed()

