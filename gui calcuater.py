from tkinter import *
from tkinter import ttk

class SimpleCalculator (Tk):

    def __init__(self):
        super().__init__()

        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, pady=(5, 5), padx=(5, 5))
        self.entry_screen_value = StringVar()
        self.screen_entry = ttk.Entry(frame, textvariable=self.entry_screen_value)
        self.screen_entry.grid(row=0, column=0, columnspan=4, sticky=(W, E), pady=(5, 5))

        btn_delete = ttk.Button(frame, text="  C  ", command = self.press_delete)
        btn_delete.grid(row=2, column=3)

        btn_9 = ttk.Button(frame, text="  9  ", command= self.press_nine)
        btn_9.grid(row=2, column=2)

        btn_8 = ttk.Button(frame, text="  8  ", command= self.press_eight)
        btn_8.grid(row=2, column=1)

        btn_7 = ttk.Button(frame, text="  7  ", command= self.press_seven)
        btn_7.grid(row=2, column=0)

        btn_add = ttk.Button(frame, text="  +  ", command=self.press_add)
        btn_add.grid(row=3, column=3)

        btn_6 = ttk.Button(frame, text="  6  ", command=self.press_six)
        btn_6.grid(row=3, column=2)

        btn_5 = ttk.Button(frame, text="  5  ", command=self.press_five)
        btn_5.grid(row=3, column=1)

        btn_4 = ttk.Button(frame, text="  4  ", command=self.press_four)
        btn_4.grid(row=3, column=0)

        btn_sub = ttk.Button(frame, text="  -  ", command=self.press_sub)
        btn_sub.grid(row=4, column=3)

        btn_3 = ttk.Button(frame, text="  3  ", command=self.press_three)
        btn_3.grid(row=4, column=2)

        btn_2 = ttk.Button(frame, text="  2  ", command=self.press_two)
        btn_2.grid(row=4, column=1)

        btn_1 = ttk.Button(frame, text="  1  ", command=self.press_one)
        btn_1.grid(row=4, column=0)

        btn_multi = ttk.Button(frame, text="  *  ", command=self.press_multi)
        btn_multi.grid(row=5, column=3)

        btn_0 = ttk.Button(frame, text="  0  ", command=self.press_zero)
        btn_0.grid(row=5, column=0, columnspan=2, sticky=(W, E))

        btn_dot = ttk.Button(frame, text="  .  ", command=self.press_dot)
        btn_dot.grid(row=5, column=2)

        btn_divide = ttk.Button(frame, text="  ÷  ", command=self.press_divide)
        btn_divide.grid(row=6, column=3)

        btn_equal = ttk.Button(frame, text="  =  ", command=self.Press_equal)
        btn_equal.grid(row=6, column=0, columnspan=3, sticky=(W, E))


        self.mainloop()

    def press_zero(self):
        self.screen_entry.insert(END, "0")

    def press_one(self):
        self.screen_entry.insert(END, "1")

    def press_two(self):
        self.screen_entry.insert(END, "2")

    def press_three(self):
        self.screen_entry.insert(END, "3")

    def press_four(self):
        self.screen_entry.insert(END, "4")

    def press_five(self):
        self.screen_entry.insert(END, "5")

    def press_six(self):
        self.screen_entry.insert(END, "6")

    def press_seven(self):
        self.screen_entry.insert(END, "7")

    def press_eight(self):
        self.screen_entry.insert(END, "8")

    def press_nine(self):
        self.screen_entry.insert(END, "9")

    def press_dot(self):
        self.screen_entry.insert(END, ".")

    def press_delete(self):
        val = self.entry_screen_value.get()[:-1]
        self.screen_entry.delete(0, END)
        self.screen_entry.insert(END, val)

    def press_add(self):
        self.screen_entry.insert(END, "+")

    def press_sub(self):
        self.screen_entry.insert(END, "-")

    def press_multi(self):
        self.screen_entry.insert(END, "*")

    def press_divide(self):
        self.screen_entry.insert(END, "÷")

    def press_square(self):
        self.screen_entry.insert(END, "√(")
        

    def Press_equal(self):
        formula = self.doMultiFirst(self.do_divide_first(self.convertTo(self.entry_screen_value.get())))

        result = 0
        temp = 0
        sign = ""
        if len(formula) == 1:
            result = formula[0]
        else:
            for di in formula:
                if di != "+" and di != "*" and di != "-" and di != "÷":
                    if sign == "+":
                        temp = float(di)
                        result += temp
                    elif sign == "-":
                        temp = float(di)
                        result -= temp
                    elif sign == "*":
                        temp = int(di)
                        result *= temp
                    elif sign == "÷":
                        temp = float(di)
                        result /= temp
                    else:
                        temp = float(di)
                        result = temp
                else:
                    if di == "+":
                        sign = "+"
                    elif di == "-":
                        sign = "-"
                    elif di == "*":
                        sign = "*"
                    elif di == "÷":
                        sign = "÷"

        self.screen_entry.delete(0, END)
        r = str(result).split(".")[-1:]
        if r[0] == '0':
            self.screen_entry.insert(END, int(result))
        else:
            self.screen_entry.insert(END, result)

        print(formula)

    # this function convert formula = "-1+11+3+5*5" to ['-1','+','11','+','3','+','5','*','5']
    def convertTo(self, nm):
        # this temp list we store our formula in it
        dd = []
        temp = ""
        for i in range(len(nm)):

            if nm[i] != "+" and nm[i] != "*" and nm[i] != "÷" and nm[i] != "-":
                temp += nm[i]

            else:
                # if our first input is -1 we need to combine it we second input and ill be like -1
                if i == 0 and nm[0] == "-":
                    temp = "-"
                else:
                    # we add prev combination like 11 to the list after we reach sign + or * or ..
                    dd += [temp]
                    dd += [nm[i]]
                    temp = ""

            if i == len(nm) - 1:
                dd += [temp]
        return dd

    # this function convert ['3','+','4','*','2','+','3'] to ['3','+','8','+','3']
    def doMultiFirst(self, ls):
        newlist = []
        for i in range(len(ls)):

            if ls[i] == "*":
                f = float(ls[i - 1])
                l = float(ls[i + 1])
                r = f * l
                ls[i + 1] = r
                ls[i] = 0
                ls[i - 1] = 0

        for k in ls:
            if k != 0:
                newlist += [k]
        return newlist

    # this function convert ['3','+','4','÷','2','+','3'] to ['3','+','2','+','3']
    def do_divide_first(self, ls):
        newlist = []
        for i in range(len(ls)):

            if ls[i] == "÷":
                f = float(ls[i - 1])
                l = float(ls[i + 1])
                r = f / l
                ls[i + 1] = r
                ls[i] = 0
                ls[i - 1] = 0

        for k in ls:
            if k != 0:
                newlist += [k]

        return newlist



if __name__ == "__main__":
    SimpleCalculator()