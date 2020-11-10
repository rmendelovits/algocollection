from typing import Any, Mapping

class AlgorithmInvoker(object):
    """The INVOKER class"""
    def __init__(self) -> None:
        self._history = []

    @property
    def history(self):
        return self._history

    def execute(self, command, param_dict: Mapping[str, Any]) -> Any:
        self._history.append(command)
        return command.execute(self, param_dict)
