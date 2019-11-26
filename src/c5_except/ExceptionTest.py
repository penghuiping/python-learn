from types import TracebackType
from typing import Optional

import logging


class SelfDefineError(RuntimeError):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)

    def with_traceback(self, tb: Optional[TracebackType]) -> BaseException:
        return super().with_traceback(tb)


i = 0

try:
    if i == 0:
        raise SelfDefineError("i==0")
except SelfDefineError as e:
    logging.error(e)
finally:
    print("finally...")
