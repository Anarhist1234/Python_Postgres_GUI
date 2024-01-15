import psycopg2
from tkinter import *
from tkinter import messagebox
import pandas as pd
import datetime



def calculate_bmi():
    return True


def information_about_calls():
    conn = psycopg2.connect(host='localhost', database='postgres', user='pavel', password='30042002-')
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT id, id_users, time_call::time FROM calls")
    # Retrieve query results
    records = cur.fetchall()
    print(records)
    df = pd.DataFrame(records, columns=['id_calls', 'user_id', 'time'])
    messagebox.showinfo('bmi-pythonguides', f'{df}')
    cur.close()
    return df

def clients_information():
    conn = psycopg2.connect(host='localhost', database='postgres', user='pavel', password='30042002-')
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * from users")
    # Retrieve query results
    records = cur.fetchall()
    print(records)
    df = pd.DataFrame(records, columns=['id', 'name', 'age', 'date_connect'])
    messagebox.showinfo('bmi-pythonguides', f'{df}')
    cur.close()
    return df

if __name__ == "__main__":
    window = Tk()
    window.title('GUI')
    window.geometry('800x800')

    frame = Frame(
        window,
        padx=100,
        pady=100
    )
    frame.pack(expand=True)


    cal_btn = Button(
        frame,
        text='Clients information',
        command=clients_information
    )
    cal_btn1 = Button(
        frame,
        text='Information about calls',
        command=information_about_calls
    )
    cal_btn2 = Button(
        frame,
        text='Clients category and info',
        command=calculate_bmi
    )
    cal_btn3 = Button(
        frame,
        text='Control operators',
        command=calculate_bmi
    )
    cal_btn4 = Button(
        frame,
        text='Tarifs of calls',
        command=calculate_bmi
    )
    cal_btn5 = Button(
        frame,
        text='Location of calls',
        command=calculate_bmi
    )
    cal_btn6 = Button(
        frame,
        text='Info about telecommunication tower',
        command=calculate_bmi)
    cal_btn7 = Button(
        frame,
        text='All telephone numbers',
        command=calculate_bmi
    )
    cal_btn8 = Button(
        frame,
        text='Average time between calls each client',
        command=calculate_bmi
    )
    cal_btn9 = Button(
        frame,
        text='Whole price for calls each client today',
        command=calculate_bmi
    )

    cal_btn.grid(row=1, column=1)
    cal_btn1.grid(row=2, column=1)
    cal_btn2.grid(row=3, column=1)
    cal_btn3.grid(row=4, column=1)
    cal_btn4.grid(row=5, column=1)
    cal_btn5.grid(row=6, column=1)
    cal_btn6.grid(row=7, column=1)
    cal_btn7.grid(row=8, column=1)
    cal_btn8.grid(row=9, column=1)
    cal_btn9.grid(row=10, column=1)

    window.mainloop()

