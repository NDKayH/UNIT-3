# Quiz 043


## Paper Solution
![IMG_4785](https://github.com/user-attachments/assets/07b6c86b-aa7e-4382-8a58-6eda3095f6df)

## Code
```.py

class PalNum:
    def __init__(self, A, B):
        # Store range boundaries in instance attributes
        self.A = A
        self.B = B

    def get_pal_list(self):
        # Return a list of palindromes in [self.A, self.B]
        palindromes = []
        for num in range(self.A, self.B + 1):
            s = str(num)
            if s == s[::-1]:
                palindromes.append(num)
        return palindromes


pn1 = PalNum(1, 9)
print("A=1, B=9 ->", pn1.get_pal_list())

# another instance with A=10, B=199
pn2 = PalNum(10, 199)
print("A=10, B=199 ->", pn2.get_pal_list())

```

## Proof of work
![image](https://github.com/user-attachments/assets/c2a1ec7e-0f9d-4b7b-94a2-1989bd37a553)
