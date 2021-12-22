
class Duck:
    sound='Quack'
    walking='Walk like a duck'

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


def main():
        obj=Duck()
        obj.quack()
        obj.walk()

if __name__ == '__main__': main()
