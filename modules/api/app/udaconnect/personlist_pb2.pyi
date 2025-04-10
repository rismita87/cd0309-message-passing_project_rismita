from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Person(_message.Message):
    __slots__ = ("id", "first_name", "last_name", "company_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    first_name: str
    last_name: str
    company_name: str
    def __init__(self, id: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., company_name: _Optional[str] = ...) -> None: ...

class PersonList(_message.Message):
    __slots__ = ("people",)
    PEOPLE_FIELD_NUMBER: _ClassVar[int]
    people: _containers.RepeatedCompositeFieldContainer[Person]
    def __init__(self, people: _Optional[_Iterable[_Union[Person, _Mapping]]] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
