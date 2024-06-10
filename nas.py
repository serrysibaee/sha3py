from dataclasses import dataclass


@dataclass
class Nas:
    text: str

    def get_length(self):
        return len(self.text)
