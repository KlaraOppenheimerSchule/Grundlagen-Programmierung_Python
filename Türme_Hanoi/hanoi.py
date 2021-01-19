class game:

    def __init__(self, height):
        self.__height = height
        self.__stack = [[], [], []]

        for i in range(self.__height, 0, -1):
            self.__stack[0].append(i)

    def solve(self):
        self.__showState()
        self.__solve(1, 3, self.__height)

        # startS, midS, endS
        # 1 = 1.Stick, 2 = 2.Stick, 3 = Stick
    def __solve(self, startS, endS, height):
        midS = 6 - startS - endS
        if(height > 0):
            self.__solve(startS, midS, height - 1)
            self.__move(startS, endS)
            self.__solve(midS, endS, height - 1)

    def __move(self, startS, endS):
        if (startS >= 1 & startS <= 3 & endS >= 1 & endS <= 3):
            self.__stack[endS - 1].append(self.__stack[startS - 1].pop())
        else:
            exit(self)

        self.__showState()

    def __showState(self):
        print("------------")
        print(self.__stack[0])
        print(self.__stack[1])
        print(self.__stack[2])


g = game(30)
g.solve()
