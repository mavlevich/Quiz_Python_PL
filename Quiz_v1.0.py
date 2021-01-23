from tkinter import *
import tkinter as tk




window = Tk()
window.geometry("1024x768")
window.title("Quiz")
ramka = Frame(window)
ramka.grid() 

wynik = 0

var1 = IntVar()
res1 = IntVar()
res2 = IntVar()

label = Label(text="1. Ile miał wagi pirwszy elektroniczny komputer ENIAC?", font=("Arial Bold", 10))
label.grid(row=0,column=0,sticky=W)

check1 = Checkbutton(text='27 ton', takefocus = 0, variable=var1)#poprawna odpowiedz
check1.grid(row=2,column=0,sticky=W)
check2 = Checkbutton(text='19 ton', takefocus = 0, variable=res1)
check2.grid(row=3,column=0,sticky=W)
check3 = Checkbutton(text='400 kg', takefocus = 0, variable=res2)
check3.grid(row=4,column=0,sticky=W)

var2 = IntVar()
res3 = IntVar()
res4 = IntVar()
label2 = Label(text="2. Maskotka Linuksa, jako oficjalne logo, to?", font=("Arial Bold", 10))
label2.grid(row=0,column=1,sticky=W)
check4 = Checkbutton(text='Kot', takefocus = 0, variable=res3)
check4.grid(row=2,column=1,sticky=W)
check5 = Checkbutton(text='Pingwin', takefocus = 0, variable=var2)#poprawna odpowiedz
check5.grid(row=3,column=1,sticky=W)
check6 = Checkbutton(text='Linus Torwald', takefocus = 0, variable=res4)
check6.grid(row=4,column=1,sticky=W)

var3 = IntVar()
res5 = IntVar()
res6 = IntVar()
label3 = Label(text="3.W którym roku był prezentowany pierwszy Iphone z ekranem dotykowym?", font=("Arial Bold", 10))
label3.grid(row=9,column=0,sticky=W)
check7 = Checkbutton(text='2007', takefocus = 0, variable=var3)#poprawna odpowiedz
check7.grid(row=10,column=0,sticky=W)
check8 = Checkbutton(text='2005', takefocus = 0,variable=res5)
check8.grid(row=11,column=0,sticky=W)
check9 = Checkbutton(text='1997', takefocus = 0,variable=res6)
check9.grid(row=12,column=0,sticky=W)

var4 = IntVar()
res7 = IntVar()
res8 = IntVar()
label4 = Label(text="4. W ktorym roku została wynaleziona pierwsza mysz komputerowa?", font=("Arial Bold", 10))
label4.grid(row=9,column=1,sticky=W)
check10 = Checkbutton(text='1968', takefocus = 0, variable=res7)
check10.grid(row=10,column=1,sticky=W)
check11 = Checkbutton(text='1964', takefocus = 0, variable=var4)#poprawna odpowiedz
check11.grid(row=11,column=1,sticky=W)
check12 = Checkbutton(text='1972', takefocus = 0, variable=res8)
check12.grid(row=12,column=1,sticky=W)

var5 = IntVar()
res9 = IntVar()
res10 = IntVar()
label5 = Label(text="5. Sredni wiek gracza gry komputerowe wynosi?", font=("Arial Bold", 10))
label5.grid(row=17,column=0,sticky=W)
check13 = Checkbutton(text='30', takefocus = 0, variable=res9)
check13.grid(row=18,column=0,sticky=W)
check14 = Checkbutton(text='27', takefocus = 0, variable=res10)
check14.grid(row=19,column=0,sticky=W)
check16 = Checkbutton(text='35', takefocus = 0, variable=var5)#poprawna odpowiedz
check16.grid(row=20,column=0,sticky=W)

var6 = IntVar()
res11 = IntVar()
res12 = IntVar()
label6 = Label(text="6. W którym roku była przedstawiona pierwsza przeglądarka internetowa?", font=("Arial Bold", 10))
label6.grid(row=17,column=1,sticky=W)
check17 = Checkbutton(text='1888', takefocus = 0, variable=res11)
check17.grid(row=18,column=1,sticky=W)
check18 = Checkbutton(text='1995', takefocus = 0, variable=res12)
check18.grid(row=19,column=1,sticky=W)
check19 = Checkbutton(text='1994', takefocus = 0, variable=var6)#poprawna odpowiedz
check19.grid(row=20,column=1,sticky=W)

var7 = IntVar()
res13 = IntVar()
res14 = IntVar()
label7 = Label(text="7. Najpopularniejszy język programowania w 2019 roku?", font=("Arial Bold", 10))
label7.grid(row=25,column=0,sticky=W)
check20 = Checkbutton(text='JavaScript', takefocus = 0, variable=var7)#poprawna odpowiedz
check20.grid(row=26,column=0,sticky=W)
check21 = Checkbutton(text='Python', takefocus = 0, variable=res13)
check21.grid(row=27,column=0,sticky=W)
check22 = Checkbutton(text='Java', takefocus = 0, variable=res14)
check22.grid(row=28,column=0,sticky=W)

var8 = IntVar()
res15 = IntVar()
res16 = IntVar()
label8 = Label( text="8. Pierwsza gra komputerowa była stworzona w ... roku?", font=("Arial Bold", 10))
label8.grid(row=25,column=1,sticky=W)
check23 = Checkbutton(text='1963', takefocus = 0, variable=res15)
check23.grid(row=26,column=1,sticky=W)
check24 = Checkbutton(text='1966', takefocus = 0, variable=res16)
check24.grid(row=27,column=1,sticky=W)
check25 = Checkbutton(text='1961', takefocus = 0, variable=var8)#poprawna odpowiedz
check25.grid(row=28,column=1,sticky=W)

var9_1 = IntVar()
var9_2 = IntVar()
res9_2 = IntVar()
label9 = Label(text="9. Tworca facebook studiował na Harvardzie? (wiel. wybór)", font=("Arial Bold", 10))
label9.grid(row=33,column=0,sticky=W)
check26= Checkbutton(text='Na wydziale informatycznym', takefocus = 0, variable=var9_1)#poprawna odpowiedz
check26.grid(row=34,column=0,sticky=W)
check27 = Checkbutton(text='Na wydziale psychologicznym', takefocus = 0, variable=res9_2)
check27.grid(row=35,column=0,sticky=W)
check28 = Checkbutton(text='Uczęszczał na kursy informatyczne', takefocus = 0, variable=var9_2) #też poprawna
check28.grid(row=36,column=0,sticky=W)

var10_1 = IntVar()
var10_2 = IntVar()
res10_2 = IntVar()
label10 = Label(text="10. Jaki z wyminionych językow są jezkami programowania (wiel. wybór)", font=("Arial Bold", 10))
label10.grid(row=33,column=1,sticky=W)
check29 = Checkbutton(text='HTML', takefocus = 0, variable=res10_2)
check29.grid(row=34,column=1,sticky=W)
check30 = Checkbutton(text='Swift', takefocus = 0, variable=var10_1)#poprawna odpowiedz
check30.grid(row=35,column=1,sticky=W)
check31 = Checkbutton(text='Go', takefocus = 0, variable=var10_2)#poprawna odpowiedz
check31.grid(row=36,column=1,sticky=W)

def checkResult():
    global wynik
    if var1.get() == 1:
        wynik+=1
    if var2.get() == 1:
        wynik+=1
    if var3.get() == 1:
        wynik+=1
    if var4.get() == 1:
        wynik+=1
    if var5.get() == 1:
        wynik+=1
    if var6.get() == 1:
        wynik+=1
    if var7.get() == 1:
        wynik+=1
    if var8.get() == 1:
        wynik+=1
    
    if var9_1.get() == 1:
        wynik+=1
    if var9_2.get() == 1:
        wynik+=1

    if var10_1.get() == 1:
        wynik+=1
    if var10_2.get() == 1:
        wynik+=1


labelTwojWynik = Label(text="Twoj wynik: ", font=("Arial Bold", 10),bg='lightgreen', width = 50)
labelTwojWynik.grid(row=40, column=0)
labelWynik = Label(text="Twoj wynik: ", font=("Arial Bold", 10),bg='lightgreen', width = 50)
labelWynik = Label(text="", font=("Arial Bold", 10),  bg='lightgreen', width = 50)
labelWynik.grid(row=40, column=1)

def showAll():
    checkResult()
    labelWynik.config(text = str(wynik)+"/12")
    Button1.config(state = tk.DISABLED)

def resetAll():
    global wynik
    Button1.config(state = tk.NORMAL)
    wynik = 0
    labelWynik.config(text = "")
    var1.set(0)
    res1.set(0)
    res2.set(0)
    
    var2.set(0)
    res3.set(0)
    res4.set(0)

    var3.set(0)
    res5.set(0)
    res6.set(0)

    var4.set(0)
    res7.set(0)
    res8.set(0)

    var5.set(0)
    res9.set(0)
    res10.set(0)

    var6.set(0)
    res11.set(0)
    res12.set(0)

    var7.set(0) 
    res13.set(0)
    res14.set(0)

    var8.set(0) 
    res15.set(0)
    res16.set(0)

    var9_1.set(0)
    var9_2.set(0)
    res9_2.set(0)

    var10_1.set(0)
    var10_2.set(0)
    res10_2.set(0) 


Button1 = Button(text="Zakoncz Quiz", font=("Arial Bold", 10))
Button1["command"]=showAll
Button1.grid(row=37,column=0,sticky=W) 

Button2 = Button(text="Quit", font=("Arial Bold", 10), command=window.quit)
Button2.grid(row=39, column=0, sticky=W)

Button3 = Button(text="Reset Quiz", font=("Arial Bold", 10), command=window.quit)
Button3["command"]=resetAll
Button3.grid(row=38, column=0, sticky=W)

mainloop()