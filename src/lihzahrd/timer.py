import time


class Timer:
    """An object to track and print the time required to perform a section of code."""

    def __init__(self, name: str, display: bool = True):
        self.name: str = name
        self.display: bool = display
        self._start_time: float|None = None
        self._stop_time: float|None = None

    def start(self):
        self._start_time = time.time()
        if self.display:
            print(f"Timer {self.name} started.")

    def stop(self):
        self._stop_time = time.time()
        if self.display:
            assert self._start_time is not None
            difference_s = self._stop_time - self._start_time
            print(f"Timer {self.name} stopped: {difference_s} seconds elapsed.")

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


__all__ = (
    "Timer",
)
