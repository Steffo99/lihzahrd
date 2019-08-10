import time
import typing


class Timer:
    def __init__(self, name: str, display: bool = False):
        self.name: str = name
        self.display: bool = display
        self._start_time: typing.Optional[float] = None
        self._stop_time: typing.Optional[float] = None

    @property
    def _result(self) -> float:
        return self._stop_time - self._start_time

    def start(self):
        self._start_time = time.time()
        if self.display:
            print(f"Timer {self.name} started.")

    def stop(self):
        self._stop_time = time.time()
        if self.display:
            print(f"Timer {self.name} stopped: {self._result} seconds elapsed.")

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
