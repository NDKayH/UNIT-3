# Quiz 044

## Paper Solution
![IMG_4790](https://github.com/user-attachments/assets/998a52a8-cb87-474c-bfae-36385fbce8ca)

## Code
```.py

class rainDrops:
    def pour(self, n: int) -> str:
        result = ""
        
        if n % 3 == 0:
            result += "Pling"
        if n % 5 == 0:
            result += "Plang"
        if n % 7 == 0:
            result += "Plong"
        
        return result if result else str(n)


# Example
raindrop = rainDrops()
print(raindrop.pour(28))
print(raindrop.pour(30))
print(raindrop.pour(34))

```

## Proof of work
![image](https://github.com/user-attachments/assets/481e89e1-1b49-4f6f-93d8-705248f0a6ff)

