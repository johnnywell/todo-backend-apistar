from typing import NewType
from uuid import UUID

from maya import MayaDT

EntityId = NewType('EntityId', UUID)
EntityVersion = NewType('EntityVersion', int)
Date = NewType('Date', MayaDT)
