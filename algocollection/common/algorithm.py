from typing import Any, Mapping

class Algorithm(object):
    """The COMMAND interface"""
    def __init__(self, obj) -> None:
        self._obj = obj

    def execute(self, param_dict: Mapping[str, Any]) -> Any:
        raise NotImplementedError
