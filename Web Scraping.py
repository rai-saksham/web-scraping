from tkinter import *
from tkinter.ttk import *
from tkinter import Scrollbar
from bs4 import BeautifulSoup
import requests
import webbrowser
from selenium import webdriver

headers = {'User-Agent': 'Chrome/90.0.4430.212'}

global driver
flipkart = ''
amazon = ''
olx = ''


def flipkartfun(name):
    try:
        global flipkart
        flipkart_name = ''
        flipkart_price = 'Product Not Found'
        name1 = name.replace(" ", "+")   # iphone x  -> iphone+x
        flipkart = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(flipkart, headers=headers)
        driver.get(flipkart)

        soup = BeautifulSoup(res.text, 'html.parser')
        flipkart_page = soup.select('._4rR01T')
        flipkart_page_length = len(flipkart_page)
        for i in range(0, flipkart_page_length):
            name = name.upper()
            flipkart_name = soup.select('._4rR01T')[i].getText().strip().upper()  # New Class For Product Name
            if name in flipkart_name:
                flipkart_price = soup.select('._1_WHN1')[i].getText().strip()  # New Class For Product Price
                flipkart_name = soup.select('._4rR01T')[i].getText().strip()
                break
            else:
                i += 1
                i = int(i)
                if i == flipkart_page_length:
                    flipkart_price = 'Product Not Found'
                    break
        return f"{flipkart_name}\n\nPrice : {flipkart_price}\n"
    except ():
        flipkart_price = 'Product Not Found'
        return flipkart_price


def amazonfun(name):
    try:
        global amazon
        amazon_name = ''
        amazon_price = ''
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon = f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(amazon, headers=headers)
        driver.get(amazon)

        soup = BeautifulSoup(res.text, 'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = len(amazon_page)
        for i in range(0, amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name[0:20]:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                break
            else:
                i += 1
                i = int(i)
                if i == amazon_page_length:
                    amazon_price = 'Product Not Found'
                    break
        return f"{amazon_name}\n\nPrice : {amazon_price}\n"
    except():
        amazon_price = 'Product Not Found'
        return amazon_price


def olxfun(name):
    try:
        global olx
        olx_price = ''
        olx_loc = ''
        name1 = name.replace(" ", "-")
        olx = f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
        res = requests.get(olx, headers=headers)
        driver.get(olx)

        soup = BeautifulSoup(res.text, 'html.parser')
        olx_name = soup.select('._2tW1I')
        olx_page_length = len(olx_name)
        for i in range(0, olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                olx_name = soup.select('._2tW1I')[i].getText().strip()
                olx_loc = soup.select('.tjgMj')[i].getText().strip()
                break
            else:
                i += 1
                i = int(i)
                if i == olx_page_length:
                    olx_price = 'Product Not Found'
                    break
        return f"{olx_name}\n\nPrice : {olx_price}\n\nLocation : {olx_loc}"
    except():
        olx_price = 'Product Not Found'
        return olx_price


def urls():
    global flipkart
    global amazon
    global olx
    return f"{flipkart}\n\n\n{amazon}\n\n\n{olx}"


def open_url(event):
    global flipkart
    global amazon
    global olx
    webbrowser.open_new(flipkart)
    webbrowser.open_new(amazon)
    webbrowser.open_new(olx)


def search():
    global driver
    path = "chromedriver.exe"
    driver = webdriver.Chrome(path)
    search_button.place_forget()

    box1.delete(1.0, "end")
    box2.delete(1.0, "end")
    box3.delete(1.0, "end")
    box4.delete(1.0, "end")

    t1 = flipkartfun(product_name.get())
    t2 = amazonfun(product_name.get())
    t3 = olxfun(product_name.get())
    driver.quit()
    t4 = urls()

    box1.insert(1.0, t1)
    box2.insert(1.0, t2)
    box3.insert(1.0, t3)
    box4.insert(1.0, t4)


window = Tk()
window.wm_title("Prise comparison")
window.geometry("820x600+200+20")

bg = PhotoImage(file="background.png")

# Show image using label
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

lable_one = Label(window, text="Enter Product Name :", font=("Bold courier", 12), background='white')
lable_one.grid(row=0, column=0, pady=5)

product_name = StringVar()
product_name_entry = Entry(window, textvariable=product_name, width=60)
product_name_entry.grid(row=0, column=0, pady=5, columnspan=2)

search_button = Button(window, text="Search", width=12, command=search)
search_button.grid(row=1, column=0, pady=5, columnspan=2)

photo_1 = PhotoImage(file="flipkart-logo.png")
l1 = Label(window, image=photo_1, background='white')
photo_2 = PhotoImage(file="Amazon-logo2.png")
l2 = Label(window, image=photo_2, background='white')
photo_3 = PhotoImage(file="OLX_Logo2.png")
l3 = Label(window, image=photo_3, background='white')

l4 = Label(window, text="All Urls", font=("Bold courier", 20), background='white')

l1.grid(row=2, column=0, pady=5)
l2.grid(row=3, column=0, pady=5)
l3.grid(row=4, column=0, pady=5)
l4.grid(row=5, column=0, pady=5)

scrollbar = Scrollbar(window)
box1 = Text(window, height=5, width=70, yscrollcommand=scrollbar.set)
box2 = Text(window, height=5, width=70, yscrollcommand=scrollbar.set)
box3 = Text(window, height=7, width=70, yscrollcommand=scrollbar.set)
box4 = Text(window, height=10, width=70, yscrollcommand=scrollbar.set, fg="blue", cursor="hand2")

box1.grid(row=2, column=1, pady=5, padx=10)
box2.grid(row=3, column=1, pady=5, padx=10)
box3.grid(row=4, column=1, pady=5, padx=10)
box4.grid(row=5, column=1, pady=5, padx=10)

box4.bind("<Button-1>", open_url)

window.mainloop()
