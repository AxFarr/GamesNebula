from tkinter import *
import tkinter.messagebox as tm

class Popup(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent


#showerror, showwarning, askquestion, showinfo
    def onUserAvail(self):
        tm.showwarning("Notice", "Username is already taken.")

    def onPasswordMatch(self):
        tm.showerror("Error", "Passwords do not match.")

    def onIncorrect(self):
        tm.showerror("Error", "Username or password is incorrect.")

    def onSpecialChar(self):
        tm.showerror("Warning", "Username or password must not contain special characters (ex: * & $ @)")

    def onUserLength(self):
        tm.showerror("Error", "Username must be 4-15 characters.")

    def onPassLength(self):
        tm.showerror("Error", "Password must be 4-15 characters.")

    def onDelete(self):
        tm.askquestion("Question", "Are you sure you want to delete?")

    def onSearch(self):
        tm.showinfo("Information", "Search done, no results.")


def main():

    root = Tk()
    pu = Popup(root)
    root.mainloop()


if __name__ == '__main__':
    main()
