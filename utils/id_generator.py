from itertools import count


class IDGenerator:
    """
    Generates IDs like:
    ACC0001
    CAT0001
    TRN000001
    """

    def __init__(self):
        self._counters = {}

    def generate(self, prefix: str, width: int = 4) -> str:
        """
        Generate the next ID for the given prefix.
        """

        if prefix not in self._counters:
            self._counters[prefix] = count(1)

        value = next(self._counters[prefix])

        return f"{prefix}{value:0{width}d}"