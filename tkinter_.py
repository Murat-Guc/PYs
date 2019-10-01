import tkinter as tk
from tkinter import messagebox

pencere = tk.Tk()
pencere.title("s1gn_1n")
pencere.wm_iconbitmap('icon.ico')
pencere.resizable(False, False)

def girisyap():
    global girisbutonu
    kullaniciadi = entry1.get()
    sifre = entry2.get()
    if kullaniciadi == "murat" and sifre == "admin":
        messagebox.showinfo("s1gn_1n", "Giris basarili!")
        makina = tk.Tk()
        makina.title("mach1n3")
        pencere.destroy()

        def toplamaislem():
            def toplama():
                sayi1 = int(toplamaentry1.get())
                sayi2 = int(toplamaentry2.get())
                sonuc = sayi1 + sayi2
                sonuc1 = tk.Label(makina, text = sonuc)
                sonuc1.grid(row = 9, column = 1)
            metin = tk.Label(makina, text="Toplamak istediginiz;")
            metin.grid(row=6)
            toplamaetiket1 = tk.Label(makina, text="İlk sayı: ")
            toplamaetiket1.grid(row=7)
            toplamaentry1 = tk.Entry(makina)
            toplamaentry1.grid(row=7, column=1)
            toplamaetiket2 = tk.Label(makina, text="İkinci sayı: ")
            toplamaetiket2.grid(row=8)
            toplamaentry2 = tk.Entry(makina)
            toplamaentry2.grid(row=8, column=1)
            toplabutonu = tk.Button(makina, text="Topla: ", command = toplama, width = 10,fg = "white",bg = "gray", relief="ridge")
            toplabutonu.grid(row = 9, columnspan = 2)
            toplabutonu.pack
        def carpmaislem():
            def carpma():
                sayi1 = int(carpmaentry1.get())
                sayi2 = int(carpmaentry2.get())
                sonuc = sayi1 * sayi2
                sonuc1 = tk.Label(makina, text = sonuc)
                sonuc1.grid(row = 9, column = 1)
            metin = tk.Label(makina, text="Carpmak istediginiz;")
            metin.grid(row=6)
            carpmaetiket1 = tk.Label(makina, text="İlk sayı: ")
            carpmaetiket1.grid(row=7)
            carpmaentry1 = tk.Entry(makina)
            carpmaentry1.grid(row=7, column=1)
            carpmaetiket2 = tk.Label(makina, text="İkinci sayı: ")
            carpmaetiket2.grid(row=8)
            carpmaentry2 = tk.Entry(makina)
            carpmaentry2.grid(row=8, column=1)
            carpbutonu = tk.Button(makina, text="Carp: ", command = carpma, width = 10,fg = "white",bg = "gray", relief="ridge")
            carpbutonu.grid(row = 9, columnspan = 2)
            carpbutonu.pack
        def cikarmaislem():
            def cikarma():
                sayi1 = int(cikarmaentry1.get())
                sayi2 = int(cikarmaentry2.get())
                sonuc = sayi1 - sayi2
                sonuc1 = tk.Label(makina, text = sonuc)
                sonuc1.grid(row = 9, column = 1)
            metin = tk.Label(makina, text="Cikarmak istediginiz;")
            metin.grid(row=6)
            cikarmaetiket1 = tk.Label(makina, text="İlk sayı: ")
            cikarmaetiket1.grid(row=7)
            cikarmaentry1 = tk.Entry(makina)
            cikarmaentry1.grid(row=7, column=1)
            cikarmaetiket2 = tk.Label(makina, text="İkinci sayı: ")
            cikarmaetiket2.grid(row=8)
            cikarmaentry2 = tk.Entry(makina)
            cikarmaentry2.grid(row=8, column=1)
            cikarbutonu = tk.Button(makina, text="Cıkar: ", command = cikarma, width = 10,fg = "white",bg = "gray", relief="ridge")
            cikarbutonu.grid(row = 9, columnspan = 2)
            cikarbutonu.pack
        def bolmeislem():
            def bolme():
                sayi1 = int(bolmeentry1.get())
                sayi2 = int(bolmeentry2.get())
                sonuc = sayi1 / sayi2
                sonuc1 = tk.Label(makina, text = sonuc)
                sonuc1.grid(row = 9, column = 1)
            metin = tk.Label(makina, text="Bolmek istediginiz;")
            metin.grid(row=6)
            bolmeetiket1 = tk.Label(makina, text="İlk sayı: ")
            bolmeetiket1.grid(row=7)
            bolmeentry1 = tk.Entry(makina)
            bolmeentry1.grid(row=7, column=1)
            bolmeetiket2 = tk.Label(makina, text="İkinci sayı: ")
            bolmeetiket2.grid(row=8)
            bolmeentry2 = tk.Entry(makina)
            bolmeentry2.grid(row=8, column=1)
            bolbutonu = tk.Button(makina, text="Bol: ", command = bolme, width = 10,fg = "white",bg = "gray", relief="ridge")
            bolbutonu.grid(row = 9, columnspan = 2)
            bolbutonu.pack
        def bolumislem():
            def bolum():
                sayi1 = int(bolumentry1.get())
                sayi2 = int(bolumentry2.get())
                sonuc = sayi1 // sayi2
                sonuc1 = tk.Label(makina, text = sonuc)
                sonuc1.grid(row = 9, column = 1)
            metin = tk.Label(makina, text="Bolumunu istediginiz islemin;")
            metin.grid(row=6)
            bolumetiket1 = tk.Label(makina, text="İlk sayı: ")
            bolumetiket1.grid(row=7)
            bolumentry1 = tk.Entry(makina)
            bolumentry1.grid(row=7, column=1)
            bolumetiket2 = tk.Label(makina, text="İkinci sayı: ")
            bolumetiket2.grid(row=8)
            bolumentry2 = tk.Entry(makina)
            bolumentry2.grid(row=8, column=1)
            bolumbutonu = tk.Button(makina, text="Bolum: ", command = bolum, width = 10,fg = "white",bg = "gray", relief="ridge")
            bolumbutonu.grid(row = 9, columnspan = 2)
            bolumbutonu.pack
        def kalanislem():
            def kalan():
                sayi1 = int(kalanentry1.get())
                sayi2 = int(kalanentry2.get())
                sonuc = sayi1 % sayi2
                sonuc1 = tk.Label(makina, text = sonuc)
                sonuc1.grid(row = 9, column = 1)
            metin = tk.Label(makina, text="Kalanini istediginiz islemin;")
            metin.grid(row=6)
            kalanetiket1 = tk.Label(makina, text="İlk sayı: ")
            kalanetiket1.grid(row=7)
            kalanentry1 = tk.Entry(makina)
            kalanentry1.grid(row=7, column=1)
            kalanetiket2 = tk.Label(makina, text="İkinci sayı: ")
            kalanetiket2.grid(row=8)
            kalanentry2 = tk.Entry(makina)
            kalanentry2.grid(row=8, column=1)
            kalanbutonu = tk.Button(makina, text="Kalan: ", command = kalan, width = 10,fg = "white",bg = "gray", relief="ridge")
            kalanbutonu.grid(row = 9, columnspan = 2)
            kalanbutonu.pack
        def uslusayiislem():
            def uslusayi():
                sayi1 = int(uslusayientry1.get())
                sayi2 = int(uslusayientry2.get())
                sonuc = sayi1 ** sayi2
                sonuc1 = tk.Label(makina, text = sonuc)
                sonuc1.grid(row = 9, column = 1)
            metin = tk.Label(makina, text="Istedigniz islemin;")
            metin.grid(row=6)
            uslusayietiket1 = tk.Label(makina, text="Tabani: ")
            uslusayietiket1.grid(row=7)
            uslusayientry1 = tk.Entry(makina)
            uslusayientry1.grid(row=7, column=1)
            uslusayietiket2 = tk.Label(makina, text="Kuvveti: ")
            uslusayietiket2.grid(row=8)
            uslusayientry2 = tk.Entry(makina)
            uslusayientry2.grid(row=8, column=1)
            uslusayibutonu = tk.Button(makina, text="Sonuc: ", command = uslusayi, width = 10,fg = "white",bg = "gray", relief="ridge")
            uslusayibutonu.grid(row = 9, columnspan = 2)
            uslusayibutonu.pack
        def kokislem():
            def kok():
                sayi1 = int(kokentry1.get())
                sonuc = sayi1 **(0.5)
                sonuc1 = tk.Label(makina, text = sonuc)
                sonuc1.grid(row = 9, column = 1)
            metin = tk.Label(makina, text="Kokunu istediginiz;")
            metin.grid(row=6)
            koketiket1 = tk.Label(makina, text="Sayi: ")
            koketiket1.grid(row=7)
            kokentry1 = tk.Entry(makina)
            kokentry1.grid(row=7, column=1)
            kokbutonu = tk.Button(makina, text="Sonuc: ", command = kok, width = 10,fg = "white",bg = "gray", relief="ridge")
            kokbutonu.grid(row = 9, columnspan = 2)
            kokbutonu.pack
        def ikidenklem():
            def ikidenklem():
                a = int(ikidenklementry1.get())
                b = int(ikidenklementry2.get())
                c = int(ikidenklementry3.get())
                delta = (b * b - 4 * a * c)
                if (delta < 0):
                    metin = tk.Label(makina, text = "Denklemin reel koku yoktur.")
                    metin.grid(row = 11, column = 1)
                if (delta == 0):
                    global x2
                    metin = tk.Label(makina, text="Denkleminiz tam karedir.")
                    metin.grid(row=11, column=1)
                    x2 = (-b + delta ** 0.5) / (2 * a)
                    sonuc = x2
                    sonuc1 = tk.Label(makina, text=sonuc)
                    sonuc1.grid(row=10, column=1)
                x1 = (-b - delta ** 0.5) / (2 * a)
                x2 = (-b + delta ** 0.5) / (2 * a)
                sonuc = x1, x2
                sonuc1 = tk.Label(makina, text = sonuc)
                sonuc1.grid(row = 10, column = 1)
            metin = tk.Label(makina, text="ax^2 + bx + c = 0")
            metin.grid(row=6)
            ikidenklemetiket1 = tk.Label(makina, text="a:")
            ikidenklemetiket1.grid(row=7)
            ikidenklementry1 = tk.Entry(makina)
            ikidenklementry1.grid(row=7, column=1)
            ikidenklemetiket2 = tk.Label(makina, text="b:")
            ikidenklemetiket2.grid(row = 8)
            ikidenklementry2 = tk.Entry(makina)
            ikidenklementry2.grid(row = 8, column = 1)
            ikidenklemetiket3 = tk.Label(makina, text="c:")
            ikidenklemetiket3.grid(row=9)
            ikidenklementry3 = tk.Entry(makina)
            ikidenklementry3.grid(row=9, column=1)
            ikidenklembutonu = tk.Button(makina, text = "Kokler: ", command = ikidenklem, width=10, fg="white", bg="gray", relief="ridge")
            ikidenklembutonu.grid(row = 10, columnspan = 2)
            ikidenklembutonu.pack
        """def fibonacci():
            def fibonacci1():
                n = int(fibonaccientry1.get())
                if n <= 1:
                    sonuc = 0
                    sonuc1 = tk.Label(makina, text=sonuc)
                    sonuc1.grid(row=8, column=1)
                if n == 2:
                    sonuc = [0, 1]
                    sonuc1 = tk.Label(makina, text=sonuc)
                    sonuc1.grid(row=8, column=1)
                series = n - 1
                first = series[-2]
                second = series[-1]
                sonuc = series + [first + second]
                sonuc1 = tk.Label(makina, text=sonuc)
                sonuc1.grid(row=8, column=1)
            metin = tk.Label(makina, text="Fibonacci sayi dizisi")
            metin.grid(row=6)
            fibonaccietiket1 = tk.Label(makina, text="Istediğiniz basamak sayisi:")
            fibonaccietiket1.grid(row=7)
            fibonaccientry1 = tk.Entry(makina)
            fibonaccientry1.grid(row=7, column=1)
            fibonaccibutonu = tk.Button(makina, text="Fibonacci: ", command=fibonacci1, width=10, fg="white", bg="gray" , relief="ridge")
            fibonaccibutonu.grid(row = 8, columnspan = 2)
            fibonaccibutonu.pack"""

        def yenidenbaslat():
            makina.destroy()

        islem = tk.Label(makina, text = "Yapmak isteginiz islemi seciniz: ")
        islem.grid(row = 0)
        toplamabutonu = tk.Button(makina, text = "Toplama", command = toplamaislem, width = 30, height = 2, fg = "black", bg = "white", relief="ridge")
        toplamabutonu.grid(row = 1)
        cikarmabutonu = tk.Button(makina, text = "Cikarma", command = cikarmaislem, width = 30, height = 2, fg = "black", bg = "cyan", relief="ridge")
        cikarmabutonu.grid(row = 1, column = 1)
        carpmabutonu = tk.Button(makina, text = "Carpma", command = carpmaislem, width = 30, height = 2, fg = "black", bg = "cyan", relief="ridge")
        carpmabutonu.grid(row = 2)
        bolmebutonu = tk.Button(makina, text = "Bolme", command = bolmeislem, width = 30, height = 2, fg = "black", bg = "white", relief="ridge")
        bolmebutonu.grid(row = 2, column = 1)
        bolumbutonu = tk.Button(makina, text = "Bolum", command = bolumislem, width = 30, height = 2, fg = "black", bg = "white", relief="ridge")
        bolumbutonu.grid(row = 3)
        kalanbutonu = tk.Button(makina, text = "Kalan", command = kalanislem, width = 30, height = 2, fg = "black", bg = "cyan", relief="ridge")
        kalanbutonu.grid(row= 3, column = 1)
        uslusayibutonu = tk.Button(makina, text = "Uslu Sayi Bulma", command = uslusayiislem, width = 30, height = 2, fg = "black", bg = "cyan", relief="ridge")
        uslusayibutonu.grid(row = 4)
        kokalmabutonu = tk.Button(makina, text = "Kok alma", command = kokislem ,width = 30, height = 2, fg = "black", bg = "white", relief="ridge")
        kokalmabutonu.grid(row = 4, column = 1)
        denklembutonu = tk.Button(makina, text = "2. Derece Denklemde Kok Bulma", command = ikidenklem, width = 30, height = 2, fg = "black", bg = "white", relief="ridge")
        denklembutonu.grid(row = 5)
        fibonaccibutonu = tk.Button(makina, text = "Fibonacci Sayi Dizisi", width = 30, height = 2, fg = "black", bg = "cyan", relief="ridge")
        fibonaccibutonu.grid(row = 5, column = 1)
        menu = tk.Menu(makina)
        makina.config(menu=menu)
        subMenu = tk.Menu(menu)
        menu.add_cascade(label="Menu", menu=subMenu)
        subMenu.add_command(label="Yeniden Baslat", command=yenidenbaslat)

        toplamabutonu.pack
        cikarmabutonu.pack
        carpmabutonu.pack
        bolmebutonu.pack
        bolumbutonu.pack
        kalanbutonu.pack
        uslusayibutonu.pack
        kokalmabutonu.pack
        denklembutonu.pack
        fibonaccibutonu.pack

        makina.resizable(False, False)
        makina.mainloop()

    else:
        messagebox.showinfo("s1gn_1n", "Yanlis kullanici adi veya sifre!")

def hakkinda():
    messagebox.showinfo("Hakkinda", "Software\n\n16.09.2016\nSürüm: 0.1")

user = tk.Label(pencere,text = "Kullanici Adi:")
password = tk.Label(pencere,text = "Sifre:")
user.grid(row = 1)
password.grid(row = 2)
foto = tk.PhotoImage(file = "log1n.gif")
fotoetiket = tk.Label(pencere, image = foto)
fotoetiket.grid(row = 0, columnspan = 2)
entry1 = tk.Entry(pencere)
entry2 = tk.Entry(pencere, show="*")
entry1.grid(row = 1, column = 1)
entry2.grid(row = 2, column = 1)
tik = tk.Checkbutton(pencere, text = "Beni hatirla")
tik.grid(columnspan = 2)
girisbutonu = tk.Button(pencere, text = "Giris Yap", command = girisyap, width = 20,fg = "white",bg = "gray", relief="ridge")
girisbutonu.grid(row = 5, column = 1)
cikisbutonu = tk.Button(pencere, text = "Cikis", command = pencere.destroy, width = 10,fg = "white",bg = "gray", relief="ridge")
cikisbutonu.grid(row = 5)

menu = tk.Menu(pencere)
pencere.config(menu = menu)
subMenu = tk.Menu(menu)
menu.add_cascade(label = "Menu", menu = subMenu)
subMenu.add_command(label = "Hakkinda", command = hakkinda)
subMenu.add_separator()
subMenu.add_command(label = "Cikis", command = pencere.destroy)

cikisbutonu.pack
girisbutonu.pack

pencere.mainloop()

