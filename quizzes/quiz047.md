# Quiz 047


## Paper Solution
![IMG_4788](https://github.com/user-attachments/assets/036710bd-f877-42e0-a1fe-194dfa35a3a7)


## Code
```.py

#quiz047.py

class CalorieCount:
    def __init__(self, daily_limit):
        self.daily_limit = daily_limit
        self.daily_intake = 0
        self.protein = 0
        self.carbs = 0
        self.fat = 0

    def addMeal(self, cal, pro, car, fat):
        self.daily_intake += cal
        self.protein += pro
        self.carbs += car
        self.fat += fat

    def onTrack(self):
        return self.daily_intake <= self.daily_limit

    def getProteinPercentage(self):
        if self.daily_intake == 0:
            return 0
       
        # 4 per gram
        return (4 * self.protein) / self.daily_intake

#example
sunday = CalorieCount(1500)

# Add meals
sunday.addMeal(716, 38, 38, 45)
sunday.addMeal(230, 16, 8, 12)
sunday.addMeal(568, 38, 50, 24)

# Check if on track
print("On track?", sunday.onTrack())  # Expected: False (intake is 1514 > 1500)

# Get protein percentage
print("Protein %:", sunday.getProteinPercentage())  # Expected: ~0.24

```

## Proof of work
![image](https://github.com/user-attachments/assets/77a2aa41-7b44-4b41-878c-e16b4c000695)

