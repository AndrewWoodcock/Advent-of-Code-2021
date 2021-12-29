

class Segment:
    def __init__(self, signal:str, type:str, ident: int):
        self.signal = signal
        self.type = type
        self.ident = ident

    def __iter__(self):
        return self

    def __next__(self):
        return self

    def count(self):
        return len(self.signal)