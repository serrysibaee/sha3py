from dataclasses import dataclass


@dataclass
class Nas:
    text: str

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_length(self):
        return len(self.text)

    def get_lines(self):
        return [l for l in self.text.split("\n") if l != ""]
    
    def get_words(self):
        pass 
