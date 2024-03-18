from decimal import Decimal, getcontext


class Frange:
    """
    Frange is analog of the range(), but using float numbers
    Using convert to float, because
    Decimal(0.3) + Decimal(0.3) != Decimal(0.6)
    """
    def __init__(self, start=None, stop=None, step=None):
        getcontext().prec = 2
        self.start = float(Decimal(start)) if stop is not None else float(Decimal(0))
        self.stop = float(Decimal(stop)) if start is not None and stop is not None else float(Decimal(start))
        self.step = float(Decimal(step)) if step else float(Decimal(1))
        self.current_value = self.start

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current_value
        if value < self.stop and self.step > 0 or value > self.stop and self.step < 0:
            self.current_value += float(Decimal(self.step))
            return value
        else:
            raise StopIteration


assert (list(Frange(5)) == [0, 1, 2, 3, 4])
assert (list(Frange(2, 5)) == [2, 3, 4])
assert (list(Frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(Frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(Frange(1, 5)) == [1, 2, 3, 4])
assert (list(Frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(Frange(0, 0)) == [])
assert (list(Frange(100, 0)) == [])

print('SUCCESS!')
