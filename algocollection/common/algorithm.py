from typing import Any, Mapping


class Algorithm(object):
    """The COMMAND interface"""

    def execute(self, param_dict: Mapping[str, Any]) -> Any:
        raise NotImplementedError
