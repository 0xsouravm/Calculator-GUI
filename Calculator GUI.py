from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import datetime

top = Tk()
top.geometry('296x492')
top.title('Calculator')

blank = Label(top,height = '2')
blank.grid(row = 0,column = 0)
button_font = font.Font(family = 'Courier', size = '15',weight = 'bold')
answer_font = font.Font(family = 'Helvetica', size = '32',weight = 'bold')
query_entry_font = font.Font(family = 'Helvetica', size = '26')

answer_label = Label(top,font = answer_font,width = "11",height = '1',borderwidth='3',relief = 'ridge', anchor = 'w')
answer_label.grid(row = 3,column = 0,columnspan = 4,pady=4)

query_entry = Entry(top,font = query_entry_font,width = "15")
query_entry.insert(0,"")
query_entry.grid(row = 4,column = 0,columnspan = 4,pady=4)

def write(character):
    if character == '.':
        if query_entry.get()!="":
            if query_entry.get()[-1] == '.' :
                return

        if query_entry.get()=="" or not query_entry.get()[-1].isdigit() :
            character = '0.'
            query_entry.insert(END,character)
            return

    if query_entry.get()=="":
        if not character.isdigit():
            return

    if not character.isdigit() and not query_entry.get()[-1].isdigit():
        return 
    query_entry.insert(END,character)

def evaluate():
    expression = query_entry.get()
    if not expression[-1].isdigit():
        return
    operands = (expression.replace('+'," ").replace('-'," ").replace('x'," ").replace('÷'," ")).split(" ")
    if len(operands)<2:
        return
    temp = expression  
    operators = []
    
    history = open("hist.txt",'a+')
    x = str(datetime.datetime.now())
    history.write(x[:len(x)-7]+" : "+temp+"=")

    for i in range(len(temp)):
        if not temp[i].isdigit() and temp[i]!='.': 
            operators.append(temp[i])
    low = 0
    while low < len(operands) - 1:  
        high = low + 1        
        if operators[low] == '+':
            answer = float(operands[low])+float(operands[high])
        elif operators[low] == '-' :
            answer = float(operands[low])-float(operands[high])
        elif operators[low] == 'x' :
            answer = float(operands[low])*float(operands[high])
        elif operators[low] == '÷':
            if operands[high]!='0':
                answer = float(operands[low])/float(operands[high])
            else:
                answer = 'NaN'
                break
        operands[high] = answer
        low+=1
    history.write(str(answer)+'\n')
    history.close()
    answer_label.config(text = str(answer))

def clear():
    query_entry.delete(0,END)
    query_entry.insert(0,"")
    answer_label.config(text = "")

def back():
    expression = query_entry.get()
    query_entry.delete(0,END)
    query_entry.insert(0,expression[:-1])

butclear = Button(top,text = 'C',width = '11',height = '2',bg = 'tomato',font=button_font,command = clear)
butclear.grid(row = 5, column = 0,columnspan = '2',padx=2,pady=2)

butback = Button(top,text = '⌫',width = '5',height = '2',font=button_font,command = back)
butback.grid(row = 5, column = 2,padx=2,pady=2)

butminus = Button(top,text = '-',width = '5',height = '2',font=button_font,command = lambda: write('-'))
butminus.grid(row = 5, column = 3,padx=2,pady=2)


but1 = Button(top,text = '1',width = '5',height = '2',font=button_font,command = lambda: write('1'))
but1.grid(row = 6, column = 0,padx=2,pady=2)

but2 = Button(top,text = '2',width = '5',height = '2',font=button_font,command = lambda: write('2'))
but2.grid(row = 6, column = 1,padx=2,pady=2)

but3 = Button(top,text = '3',width = '5',height = '2',font=button_font,command = lambda: write('3'))
but3.grid(row = 6, column = 2,padx=2,pady=2)

butplus = Button(top,text = '+',width = '5',height = '2',font=button_font,command = lambda: write('+'))
butplus.grid(row = 6, column = 3,padx=2,pady=2)


but4 = Button(top,text = '4',width = '5',height = '2',font=button_font,command = lambda: write('4'))
but4.grid(row = 7, column = 0,padx=2,pady=2)

but5 = Button(top,text = '5',width = '5',height = '2',font=button_font,command = lambda: write('5'))
but5.grid(row = 7, column = 1,padx=2,pady=2)

but6 = Button(top,text = '6',width = '5',height = '2',font=button_font,command = lambda: write('6'))
but6.grid(row = 7, column = 2,padx=2,pady=2)

butmul = Button(top,text = 'x',width = '5',height = '2',font=button_font,command = lambda: write('x'))
butmul.grid(row = 7, column = 3,padx=2,pady=2)


but7 = Button(top,text = '7',width = '5',height = '2',font=button_font,command = lambda: write('7'))
but7.grid(row = 8, column = 0, padx=2, pady=2)

but8 = Button(top,text = '8',width = '5',height = '2',font=button_font,command = lambda: write('8'))
but8.grid(row = 8, column = 1,padx=2,pady=2)

but9 = Button(top,text = '9',width = '5',height = '2',font=button_font,command = lambda: write('9'))
but9.grid(row = 8, column = 2,padx=2,pady=2)

butdivide = Button(top,text = '÷',width = '5',height = '2',font=button_font,command = lambda: write('÷'))
butdivide.grid(row = 8, column = 3,padx=2,pady=2)


but0 = Button(top,text = '0',width = '5',height = '2',font=button_font,command = lambda: write('0'))
but0.grid(row = 9, column = 1,padx=2,pady=2)

butdecimal = Button(top,text = '.',width = '5',height = '2',font=button_font,command = lambda: write('.'))
butdecimal.grid(row = 9, column = 0,padx=2,pady=2)

butequal = Button(top,text = '=',width = '11',height = '2',bg = 'spring green',font=button_font, command = evaluate)
butequal.grid(row = 9, column = 2,columnspan = 2,padx=2,pady=2)

dark = 0
def darkmode():
    global dark
    if(not dark):
        f = 'slategray4'
        b = 'gray20'
        dark = 1
        bc = 'saddle brown'
        be = 'dark green'
        bqa = 'gray26'
        fqa = 'cornsilk2'
        bt = 'rosybrown4'
        fil = on
        darbg = 'rosybrown4'
        blankbg = 'rosybrown4'
        histbg = 'gray20'
        histfg = 'slategray4'
        history_areab = 'gray26'
        history_areaf = 'cornsilk2'

    else:
        f = 'gray1'
        b = 'gray90'
        dark = 0
        bc = 'tomato'
        be = 'spring green'
        bqa = 'gray90'
        fqa = 'gray1'
        bt = 'gray90'
        fil = off
        darbg = 'gray90'
        blankbg = 'gray90'
        histbg = 'gray90'
        histfg = 'gray1'
        history_areab = 'gray90'
        history_areaf = 'gray1'

    butback.config(fg = f, bg = b)
    but1.config(fg = f, bg = b)
    but2.config(fg = f, bg = b)
    but3.config(fg = f, bg = b)
    but4.config(fg = f, bg = b)
    but5.config(fg = f, bg = b)
    but6.config(fg = f, bg = b)
    but7.config(fg = f, bg = b)
    but8.config(fg = f, bg = b)
    but9.config(fg = f, bg = b)
    but0.config(fg = f, bg = b)
    butminus.config(fg = f, bg = b)
    butplus.config(fg = f, bg = b)
    butmul.config(fg = f, bg = b)
    butdivide.config(fg = f, bg = b)
    butdecimal.config(fg = f, bg = b)
    on_off_button.config(image = fil)
    butclear.config(bg = bc)
    butequal.config(bg = be)
    query_entry.config(bg = bqa, fg = fqa)
    answer_label.config(bg = bqa, fg = fqa)
    top.config(bg = bt)
    darkm.config(bg = darbg)
    blank.config(bg = blankbg)
    show_history.config(bg = histbg, fg = histfg)
    del_history.config(bg = histbg, fg = histfg)
    hist_area.config(bg = history_areab, fg = history_areaf)

darkm = Label(top,width=10,text = 'Dark Mode')
darkm.place(x=0 ,y=10)
on = PhotoImage(file = "on.png")
off = PhotoImage(file = "off.png")
on_off_button = Button(top, image = off,bd = '0', width = '21',height = '10',font = button_font,command = darkmode)
on_off_button.place(x=72,y=15)

history_ctr = 0
i = 0
def hist_show_unshow():
    global history_ctr
    if history_ctr==0:
        file = open('hist.txt','r')
        history = file.readlines()
        file.close()
        if len(history)==0:
            messagebox.showinfo("Error",  "No History Found")
            return       
        scrollbarv.grid(row = 1, column = 3, sticky='NSW')
        scrollbarv.config(command=hist_area.yview)
        scrollbarh.grid(row = 2, column = 0, sticky='ESW',columnspan=3)
        scrollbarh.config(command=hist_area.xview)
        hist_area.grid(row = 1, column = 0, columnspan = 3)
        global i
        hist_area.config(state = NORMAL)
        for line in history[i:]: 
            hist_area.insert(INSERT,str(i+1)+'/ '+line[:11]+line[20:]+'\n')
            i+=1
        hist_area.config(state = DISABLED)
        show_history.config(text='Hide History')
        del_history.place(x = 110,y=7)
        history_ctr = 1

    else:
        scrollbarv.grid_forget()
        scrollbarh.grid_forget()
        hist_area.grid_forget()
        show_history.config(text='Show History')
        del_history.place_forget()
        history_ctr = 0

def del_hist():
    file = open("hist.txt",'w')
    file.write("")
    file.close()
    scrollbarv.grid_forget()
    scrollbarh.grid_forget()
    hist_area.grid_forget()
    show_history.config(text='Show History')
    del_history.place_forget()
    query_entry.delete(0,END)
    query_entry.insert(0,"")
    answer_label.config(text = "")
    messagebox.showinfo("Successful","History Deleted")

scrollbarv = Scrollbar(top)
scrollbarh = Scrollbar(top,orient=HORIZONTAL)
hist_area = Text(top,yscrollcommand=scrollbarv.set, xscrollcommand=scrollbarh.set, width = 34,height = 27,borderwidth='3',relief = 'ridge', wrap = NONE)
show_history = Button(top,text='Show History',command = hist_show_unshow)
show_history.place(x = 210,y=7)
del_history = Button(top,text='Delete History',command = del_hist)
top.mainloop()