class Maths:
    def add(self, *args):
        total = 0
        for i in args:
            total += i   #if we add number it counts how many numbers we have and multiply it by itself.
        return total
m = Maths()
print(m.add(1, 2, 3))  # Output: 6
print(m.add(1, 2))     # Output: 3
print(m.add(1, 2, 3, 4, 5))  # Output: 15
print(m.add())  # Output: 0
print(m.add(12, 90, 23, 45, 67))  # Output: 237