# Quiz 045


## Paper Solution
![IMG_4791](https://github.com/user-attachments/assets/bef9b686-f872-4e8e-86f9-1d98376b8ea6)

## Code
```.py

import string

class WordCounter:
    def __init__(self, text: str):
        self.text = text
        self.word_counts = {}

    def count_words(self):
        text_clean = self.text.lower()
        text_clean = text_clean.translate(str.maketrans('', '', string.punctuation))
        words = text_clean.split()

        for word in words:
            if word in self.word_counts:
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1

        return self.word_counts

    def display_word_counts(self):
        for word, count in self.word_counts.items():
            print(f"{word} : {count}")


# Example
if __name__ == "__main__":
    text = "This is a sample text. It contains some words that will be counted."
    counter = WordCounter(text)
    counter.count_words()
    counter.display_word_counts()

```

## Proof of work
![image](https://github.com/user-attachments/assets/df460ec4-8547-4e68-8f23-ad8166ec0944)
