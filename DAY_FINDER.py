# importing required modules

from tkinter import *
from tkinter import ttk, messagebox

# Creating parent window.

root = Tk()
root.title('DAY Finder')
root.geometry('228x380')
root.resizable(0,0)


def popup():
    messagebox.showerror("Icon-Error", "I'm unable to find Icon file! Click 'OK' to continue." )
    messagebox.showinfo("Don't Worry", "Program can also work without icon file also." )



try:
    root.iconbitmap('icon.ico')
except:
    popup()
else:
    pass

finally:
    label_Day= Label(root, text='Enter date :-', font=('Segoe', 12, 'bold')).grid(row=0, column=0)
    label_Month = Label(root, text='Choose Month :-', font=('Segoe', 12, 'bold')).grid(row=3, column=0)
    label_Year = Label(root, text='Enter Year (YYYY) :-', font=('Segoe', 12, 'bold')).grid(row=6, column=0)
    label_Prediction = Label(root, text='Day should be :', font=('Verdana', 12, 'bold')).grid(row=11, column=0)
    label_Copyright = Label(root, text='Developed by Shiven Saini.', font=('calibri', 10)).grid(row=16, column=0)

    # Creating Dropdown menu for Months section.


    list_months = ('January', 
                  'February', 
                  'March', 
                  'April', 
                  'May', 
                  'June', 
                  'July', 
                  'August', 
                  'September', 
                  'October', 
                  'November', 
                  'December')



    # Creating entry widgets for input from user.

    entry_Day = Entry(root, width=32, borderwidth=1, relief=SOLID)
    entry_Year = Entry(root, width=32, borderwidth=1, relief=SOLID)

    # Designing Appearance of entry widgets

    entry_Day.config(font=('Segoe', 10))
    entry_Year.config(font=('Segoe', 10))

    # Creating Dropdown menu with better UI means by using ttk Module. 

    myCombo = ttk.Combobox(root, value=list_months)   # value is list of months.
    myCombo.current(2)
    myCombo.set('January')

    # positioning input widgets.

    entry_Day.grid(row=1, column=0)
    myCombo.grid(row=4, column=0)
    entry_Year.grid(row=7, column=0)


    # Creating blank lines as row and column positioning strategies are relational in tkinter.

    label_space_1 = Label(root, text="  ").grid(row=2, column=0)
    label_space_2 = Label(root, text="  ").grid(row=5, column=0)
    label_space_4 = Label(root, text="  ").grid(row=8, column=0)
    label_space_5 = Label(root, text="  ").grid(row=10, column=0)
    label_space_6 = Label(root, text="  ").grid(row=12, column=0)
    label_space_7 = Label(root, text="  ").grid(row=14, column=0)
    label_space_8 = Label(root, text="  ").grid(row=15, column=0)

    # Creating button command or defining function.

    def computations(): 
        label_ans = Label(root, text='                            ', font=('Segoe', 14)).grid(row=13, column=0)
        month_input = str(myCombo.get())
        
        # variable initalizing

        YYYY_4_digit = int(entry_Year.get())
        G_day = int(entry_Day.get())

        # Assigning value to M_code.

        if (month_input) == 'January':
            M_code = 1
        elif (month_input) == 'February':
            M_code = 2
        elif (month_input) == 'March':
            M_code = 3
        elif (month_input) == 'April':
            M_code = 4
        elif (month_input) == 'May':
            M_code = 5
        elif (month_input) == 'June':
            M_code = 6
        elif (month_input) == 'July':
            M_code = 7   
        elif (month_input) == 'August':
            M_code = 8
        elif (month_input) == 'September':
            M_code = 9
        elif (month_input) == 'October':
            M_code = 10        
        elif (month_input) == 'November':
            M_code = 11
        elif (month_input) == 'December':
            M_code = 12


        # INITIALIZING VARIABLES.

        c_code = leap_satisfy = Qt = Rem = Rem_4 = D_day = 0

        # Computations for leap year.
        if (YYYY_4_digit % 100) == 0:
            if (YYYY_4_digit % 400) == 0:
                leap_satisfy = leap_satisfy + 1
            else:
                leap_satisfy = leap_satisfy
        else:
            if (YYYY_4_digit % 4) == 0:
                leap_satisfy = leap_satisfy + 1
            else:
                leap_satisfy = leap_satisfy

        # Computations for calculation of century code.

        c_m = (YYYY_4_digit // 100)

        if c_m == 10:
            c_code = 5
        elif c_m == 11:
            c_code = 3
        elif c_m == 12:
            c_code = 2
        elif c_m == 13:
            c_code = 0
        elif c_m == 14:
            c_code = 5
        elif c_m == 15:
            c_code = 3
        elif c_m == 16:
            c_code = 2
        elif c_m == 17:
            c_code = 0
        elif c_m == 18:
            c_code = 5
        elif c_m == 19:
            c_code = 3
        elif c_m == 20:
            c_code = 2
        elif c_m == 21:
            c_code = 0
        elif c_m == 22:
            c_code = 5
        elif c_m == 23:
            c_code = 3
        elif c_m == 24:
            c_code = 2
        elif c_m == 25:
            c_code = 0
        elif c_m == 26:
            c_code = 5
        elif c_m == 27:
            c_code = 3
        elif c_m == 28:
            c_code = 2
        elif c_m == 29:
            c_code = 0
        elif c_m == 30:
            c_code = 5
        elif c_m == 31:
            c_code = 3
        elif c_m == 32:
            c_code = 2
        elif c_m == 33:
            c_code = 0
        elif c_m == 34:
            c_code = 5
        elif c_m == 35:
            c_code = 3
        elif c_m == 36:
            c_code = 2
        elif c_m == 37:
            c_code = 0
        elif c_m == 38:
            c_code = 5
        elif c_m == 39:
            c_code = 3
        elif c_m == 40:
            c_code = 2
        elif c_m == 41:
            c_code = 0
        elif c_m == 42:
            c_code = 5
        elif c_m == 43:
            c_code = 3
        elif c_m == 44:
            c_code = 2
        elif c_m == 45:
            c_code = 0
        elif c_m == 46:
            c_code = 5
        elif c_m == 47:
            c_code = 3
        elif c_m == 48:
            c_code = 2
        elif c_m == 49:
            c_code = 0
        elif c_m == 50:
            c_code = 5
        elif c_m == 51:
            c_code = 3
        elif c_m == 52:
            c_code = 2
        elif c_m == 53:
            c_code = 0
        elif c_m == 54:
            c_code = 5
        elif c_m == 55:
            c_code = 3
        elif c_m == 56:
            c_code = 2
        elif c_m == 57:
            c_code = 0
        elif c_m == 58:
            c_code = 5
        elif c_m == 59:
            c_code = 3
        elif c_m == 60:
            c_code = 2
        elif c_m == 61:
            c_code = 0
        elif c_m == 62:
            c_code = 5
        elif c_m == 63:
            c_code = 3
        elif c_m == 64:
            c_code = 2
        elif c_m == 65:
            c_code = 0
        elif c_m == 66:
            c_code = 5
        elif c_m == 67:
            c_code = 3
        elif c_m == 68:
            c_code = 2
        elif c_m == 69:
            c_code = 0
        elif c_m == 70:
            c_code = 5
        elif c_m == 71:
            c_code = 3
        elif c_m == 72:
            c_code = 2
        elif c_m == 73:
            c_code = 0
        elif c_m == 74:
            c_code = 5
        elif c_m == 75:
            c_code = 3
        elif c_m == 76:
            c_code = 2
        elif c_m == 77:
            c_code = 0
        elif c_m == 78:
            c_code = 5
        elif c_m == 79:
            c_code = 3
        elif c_m == 80:
            c_code = 2
        elif c_m == 81:
            c_code = 0
        elif c_m == 82:
            c_code = 5
        elif c_m == 83:
            c_code = 3
        elif c_m == 84:
            c_code = 2
        elif c_m == 85:
            c_code = 0
        elif c_m == 86:
            c_code = 5
        elif c_m == 87:
            c_code = 3
        elif c_m == 88:
            c_code = 2
        elif c_m == 89:
            c_code = 0
        elif c_m == 90:
            c_code = 5
        elif c_m == 91:
            c_code = 3
        elif c_m == 92:
            c_code = 2
        elif c_m == 93:
            c_code = 0
        elif c_m == 94:
            c_code = 5
        elif c_m == 95:
            c_code = 3
        elif c_m == 96:
            c_code = 2
        elif c_m == 97:
            c_code = 0
        elif c_m == 98:
            c_code = 5
        elif c_m == 99:
            c_code = 3

        # Computations of century code end by here.

        # Calculations for year code.

        Y_2_digit = (YYYY_4_digit % 100)

        if Y_2_digit >= 12:
            Qt = (Y_2_digit // 12)
            Rem = (Y_2_digit % 12)
            Rem_4 = (Rem // 4)

        elif Y_2_digit < 12:
            Qt = (Y_2_digit // 12)
            Rem = (Y_2_digit % 12)
            if Rem < 4:
                Rem_4 = 0
            else:
                Rem_4 = Rem // 4

        Y_code = c_code + Qt + Rem + Rem_4

        if Y_code >= 7:
            Y_code = Y_code % 7
        else:
            pass

        # Computations for doomsday as per leap year sequentially.

           # Monthly_doomsday database in python script.

        if leap_satisfy == 0:
              # Doomsday calculation for non-leap years.
            if M_code == 1:
                D_day = -4
            elif M_code == 2:
                D_day = 0
            elif M_code == 3:
                D_day = 0
            elif M_code == 4:
                D_day = -3
            elif M_code == 5:
                D_day = -5
            elif M_code == 6:
                D_day = -1
            elif M_code == 7:
                D_day = -3
            elif M_code == 8:
                D_day = 1
            elif M_code == 9:
                D_day = -2
            elif M_code == 10:
                D_day = -4
            elif M_code == 11:
                D_day = 0
            else:
                D_day = -2
        else:
            # Doomsday calculation for leap years.
            if M_code == 1:
                D_day = -3
            elif M_code == 2:
                D_day = -6
            elif M_code == 3:
                D_day = 0
            elif M_code == 4:
                D_day = -3
            elif M_code == 5:
                D_day = -5
            elif M_code == 6:
                D_day = -1
            elif M_code == 7:
                D_day = -3
            elif M_code == 8:
                D_day = -6
            elif M_code == 9:
                D_day = -2
            elif M_code == 10:
                D_day = -4
            elif M_code == 11:
                D_day = 0
            else:
                D_day = -2

        # Final computations starts hereby now.

        D_difference = G_day - D_day

        # using new variable ans_day for final computations.

        Ans_day = D_difference + Y_code

        # Final Computations.

        if Ans_day >= 7:
            Ans_day = Ans_day % 7
        else:
            pass

        # final conditions declarations.

        if Ans_day == 0:
            label_ans = Label(root, text='SUNDAY', font=('Segoe', 14)).grid(row=13, column=0)
        elif Ans_day == 1:
            label_ans = Label(root, text='MONDAY', font=('Segoe', 14)).grid(row=13, column=0)
        elif Ans_day == 2:
            label_ans = Label(root, text='TUESDAY', font=('Segoe', 14)).grid(row=13, column=0)
        elif Ans_day == 3:
            label_ans = Label(root, text='WEDNESDAY', font=('Segoe', 14)).grid(row=13, column=0)
        elif Ans_day == 4:
            label_ans = Label(root, text='THURSDAY', font=('Segoe', 14)).grid(row=13, column=0)
        elif Ans_day == 5:
            label_ans = Label(root, text='FRIDAY', font=('Segoe', 14)).grid(row=13, column=0)
        elif Ans_day == 6:
            label_ans = Label(root, text='SATURDAY', font=('Segoe', 14)).grid(row=13, column=0)


    # Creating button widget

    button_action = Button(root, text='CONFIRM', borderwidth=1, font=('Times', 10, "bold"),relief=SOLID, command = computations).grid(row=9, column=0)




  


# Creating label widget stating what to enter in data field.


root.mainloop()
