class Solution:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)

if __name__ == '__main__':
    ob = Solution("Mihir")
    ob.display()