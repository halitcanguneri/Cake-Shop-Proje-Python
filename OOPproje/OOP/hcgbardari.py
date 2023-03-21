from tkinter import *
import cv2
from PIL import Image, ImageTk
import sqlite3
import pandas as pd



class Visualize:
    def __init__(self, master, vid, label_widget):
        self.master = master
        self.vid = vid
        self.label_widget = label_widget

    def open_camera(self, vid, label_widget):
        # Capture the video frame by frame
        _, frame = vid.read()
        # Convert image from one color space to other
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        # Capture the latest frame and transform to image
        captured_image = Image.fromarray(opencv_image)
        # Convert captured image to photoimage
        photo_image = ImageTk.PhotoImage(image=captured_image)
        # Displaying photoimage in the label
        label_widget.photo_image = photo_image
        # Configure image in the label
        label_widget.configure(image=photo_image)
        # Repeat the same process after every 10 seconds
        label_widget.after(10, lambda: self.open_camera(vid=vid, label_widget=label_widget))


class RawMaterial:
    def __init__(self, name, date_of_purchase, supplier, expiration_date, code, description):
        self.name = name
        self.date_of_purchase = date_of_purchase
        self.supplier = supplier
        self.expiration_date = expiration_date
        self.code = code
        self.description = description


class Products(RawMaterial):
    def __init__(self, name, date_of_production, customer, expiration_date, code, raw_material_codes, description):
        super().__init__(name, date_of_production, customer, expiration_date, code, description)
        self.date_of_production = date_of_production
        self.customer = customer
        self.raw_material_codes = raw_material_codes


raw1=RawMaterial('Şeker', '2022-02-17','HALİT CAN GÜNERİ', '2023-01-03', '3', 'Sugar: Sweet Product Raw Material' )
product1=Products('Baklava', '2023-01-10', 'HALİT CAN GÜNERİ', '2023-01-12', 12, 3,'Baklava')

raw2=RawMaterial('Susam', '2022-09-25','HALİT CAN GÜNERİ', '2023-02-12', 1, 'Sesame: Bagel Raw Material' )
product2=Products('Poğaça', '2023-01-10', 'BURAK ARDA ARİ', '2023-01-11', 15, 4,'Pastry')

raw3=RawMaterial('Un', '2022-05-15','BURAK ARDA ARİ', '2023-09-15', 2, 'Flour: Pastry Raw Material ' )
product3=Products('Simit', '2023-01-10', 'BURAK ARDA ARİ', '2023-01-11', 11, 1,'Turkish Bagel')

raw4=RawMaterial('Yağ', '2023-01-08','BURAK ARDA ARİ', '2023-07-16', 4, 'Oil: Raw Material' )
product4=Products('Tiramisu', '2023-01-09', 'HALİT CAN GÜNERİ', '2023-01-13', 14, 5,'Tiramisù')

raw5=RawMaterial('Yumurta', '2023-01-10','HALİT CAN GÜNERİ', '2023-01-17', 5, 'Egg: Raw Material' )
product5=Products('Un Kurabiyesi', '2023-01-08', 'BURAK ARDA ARİ', '2023-01-10', 13, 2,'Turkish Shortbread')

# raw1=RawMaterial("hammadde1","10","çağdaşmarket","10.10.2023","rawbarkod1","bu hammadde1 hammaddedir.")
# product1=Products("anakart1","10","müşteri1","11.12.2000","1",raw1.code,"bu bir anakart1 aöuklamasidir")

# raw2=RawMaterial("hammadde2","10","çağdaşmarket","10.10.2023","rawbarkod2","bu hammadde2 hammaddedir.")
# product2=Products("anakart2","10","müşteri1","11.12.2000","2",raw2.code,"bu bir anakart2 aöuklamasidir")

# raw3=RawMaterial("hammadde3","10","çağdaşmarket","10.10.2023","rawbarkod3","bu hammadde3 hammaddedir.")
# product3=Products("anakart3","10","müşteri1","11.12.2000","3",raw3.code,"bu bir anakart3 aöuklamasidir")

# raw4=RawMaterial("hammadde4","10","hammadde4çağdaşmarket","10.10.2023","rawbarkod4","bu hammadde4 hammaddedir.")
# product4=Products("anakart4","10","anakart4müşteri1","11.12.2000","4",raw4.code,"bu bir anakart4 aöuklamasidir")

# raw5=RawMaterial("hammadde5","10","hammadde5çağdaşmarket","10.10.2023","rawbarkod5","bu hammadde5 hammaddedir.")
# product5=Products("anakart5","10","anakart5müşteri1","11.12.2000","5",raw5.code,"bu bir anakart5 aöuklamasidir")


if __name__ == "__main__":

    ### sql bağlantıları

    

    ##add
    ##delete
    ## update
    

    ### TKINTER

    master = Tk()
    master.title("hcgbardari")
    canvas = Canvas(master, height=800, width=1800)
    canvas.pack()
    # frameler
    camerayeri = Frame(master, bg='#add8e6')
    camerayeri.place(relx=0.005, rely=0.009, relheight=0.98, relwidth=0.28)

    orta = Frame(master, bg='#add8e6')
    orta.place(relx=0.29, rely=0.009, relheight=0.98, relwidth=0.256)

    urunarama = Frame(master, bg='#add8e6')
    urunarama.place(relx=0.55, rely=0.01, relheight=0.978, relwidth=0.445)

    # butonlar
    

    
    


    # labels

    camera_yazi = Label(camerayeri, text="Camera", bg='#add8e6', font="Verdana 12 bold")
    camera_yazi.place(relx=0.38, rely=0.53, relheight=0.1, relwidth=0.17)

    urunInfo = Label(camerayeri, text="Info", bg='#add8e6', font="Verdana 12 bold")
    urunInfo.place(relx=0.4, rely=0.47, relheight=0.03, relwidth=0.1)

    urunadi = Label(urunarama, text="Product Name", bg='#add8e6', font="Verdana 8 bold")
    urunadi.place(relx=0.08, rely=0.005, relheight=0.1, relwidth=0.17)

    rawadi = Label(urunarama, text="RawMaterial Name", bg='#add8e6', font="Verdana 8 bold")
    rawadi.place(relx=0.08, rely=0.5, relheight=0.1, relwidth=0.17)

    # entries
    textboxUrunAd = Entry(urunarama, textvariable=object)
    textboxUrunAd.place(relx=0.08, rely=0.1, relheight=0.04, relwidth=0.17)

    textboxRawAd = Entry(urunarama, textvariable="RawMaterial Name")
    textboxRawAd.place(relx=0.08, rely=0.585, relheight=0.04, relwidth=0.17)

    wwww, hhhhh = 300, 300
    vid = cv2.VideoCapture(0)

    # Set the width and height
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, wwww)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, hhhhh)
    master.bind('<Escape>', lambda e: master.quit())
    label_widget = Label(camerayeri)
    label_widget.place(relx=0.05, rely=0.05, relheight=0.5, relwidth=0.9)
    visualize = Visualize(master, vid, label_widget)
    visualize.open_camera(vid, label_widget)


    


    def show_product_info():
        
        isim=textboxUrunAd.get()

        if isim=="Baklava":

            product_info = "Name: {}\nDate of production: {}\nCustomer: {}\nExpiration date: {}\nCode: {}\nRaw material codes: {}\nDescription: {}".format(product1.name, product1.date_of_production, product1.customer, product1.expiration_date, product1.code, product1.raw_material_codes, product1.description)
            label = Label(urunarama, text=product_info,bg='#add8e6')
            label.place(relx=0.005, rely=0.2)
            img=cv2.imread("baklava.png",1)
            cv2.imshow("Baklava",img)
        
        elif isim=="Pogaca":

            product_info = "Name: {}\nDate of production: {}\nCustomer: {}\nExpiration date: {}\nCode: {}\nRaw material codes: {}\nDescription: {}".format(product2.name, product2.date_of_production, product2.customer, product2.expiration_date, product2.code, product2.raw_material_codes, product2.description)
            label = Label(urunarama, text=product_info,bg='#add8e6')
            label.place(relx=0.005, rely=0.2)
            img=cv2.imread("pogaca.png",1)
            cv2.imshow("Pogaca",img)
        
        elif isim=="Simit":
    
            product_info = "Name: {}\nDate of production: {}\nCustomer: {}\nExpiration date: {}\nCode: {}\nRaw material codes: {}\nDescription: {}".format(product3.name, product3.date_of_production, product3.customer, product3.expiration_date, product3.code, product3.raw_material_codes, product3.description)
            label = Label(urunarama, text=product_info,bg='#add8e6')
            label.place(relx=0.005, rely=0.2)
            img=cv2.imread("simit.png",1)
            cv2.imshow("Simit",img)
        
        elif isim=="Tiramisu":
    
            product_info = "Name: {}\nDate of production: {}\nCustomer: {}\nExpiration date: {}\nCode: {}\nRaw material codes: {}\nDescription: {}".format(product4.name, product4.date_of_production, product4.customer, product4.expiration_date, product4.code, product4.raw_material_codes, product4.description)
            label = Label(urunarama, text=product_info,bg='#add8e6')
            label.place(relx=0.005, rely=0.2)
            img=cv2.imread("tiramisu.png",1)
            cv2.imshow("Tiramisu",img)
        
        elif isim=="Un Kurabiyesi":
    
            product_info = "Name: {}\nDate of production: {}\nCustomer: {}\nExpiration date: {}\nCode: {}\nRaw material codes: {}\nDescription: {}".format(product5.name, product5.date_of_production, product5.customer, product5.expiration_date, product5.code, product5.raw_material_codes, product5.description)
            label = Label(urunarama, text=product_info,bg='#add8e6')
            label.place(relx=0.005, rely=0.2)
            img=cv2.imread("unKurabiyesi.png",1)
            cv2.imshow("Turkish Shortbread",img)
        
        else:
            print("böyle isimde bir ürün yok")

    
    
    button = Button(urunarama, text="Show product info", command=show_product_info)
    button.place(relx=0.65, rely=0.01, relheight=0.1, relwidth=0.17)

    def show_raw_info():
        
        isim2=textboxRawAd.get()

        if isim2=="Şeker":

            product_info = "Name: {}\nDate of purchase: {}\nSupplier: {}\nExpiration date: {}\nCode: {}\nDescription: {}".format(raw1.name, raw1.date_of_purchase, raw1.supplier, raw1.expiration_date, raw1.code, raw1.description)
            label = Label(urunarama, text=product_info,bg='#add8e6')
            label.place(relx=0.005, rely=0.7)
            img=cv2.imread("seker.png",1)
            cv2.imshow("Sugar",img)
        
        elif isim2=="Susam":

            product_info = "Name: {}\nDate of purchase: {}\nSupplier: {}\nExpiration date: {}\nCode: {}\nDescription: {}".format(raw2.name, raw2.date_of_purchase, raw2.supplier, raw2.expiration_date, raw2.code, raw2.description)
            label = Label(urunarama, text=product_info,bg='#add8e6')
            label.place(relx=0.005, rely=0.7)
            img=cv2.imread("susam.png",1)
            cv2.imshow("Sesame",img)
        
        elif isim2=="Un":
    
            product_info = "Name: {}\nDate of purchase: {}\nSupplier: {}\nExpiration date: {}\nCode: {}\nDescription: {}".format(raw3.name, raw3.date_of_purchase, raw3.supplier, raw3.expiration_date, raw3.code, raw3.description)
            label = Label(urunarama, text=product_info,bg='#add8e6')
            label.place(relx=0.005, rely=0.7)
            img=cv2.imread("un.png",1)
            cv2.imshow("Flour",img)
        
        elif isim2=="Yağ":
    
            product_info = "Name: {}\nDate of purchase: {}\nSupplier: {}\nExpiration date: {}\nCode: {}\nDescription: {}".format(raw4.name, raw4.date_of_purchase, raw4.supplier, raw4.expiration_date, raw4.code, raw4.description)
            label = Label(urunarama, text=product_info,bg='#add8e6')
            label.place(relx=0.005, rely=0.7)
            img=cv2.imread("yag.png",1)
            cv2.imshow("oil",img)
        
        elif isim2=="Yumurta":
    
            product_info = "Name: {}\nDate of purchase: {}\nSupplier: {}\nExpiration date: {}\nCode: {}\nDescription: {}".format(raw5.name, raw5.date_of_purchase, raw5.supplier, raw5.expiration_date, raw5.code, raw5.description)
            label = Label(urunarama, text=product_info,bg='#add8e6')
            label.place(relx=0.005, rely=0.7)
            img=cv2.imread("yumurta.png",1)
            cv2.imshow("Egg",img)
        
        else:
            print("böyle isimde bir ürün yok")

    
    
    
    
    #entryler PRODUCTLAR
    nameEntry=Entry(orta)
    nameEntry.place(relx=0.08, rely=0.1, relheight=0.04, relwidth=0.17)

    date_of_productionEntry=Entry(orta)
    date_of_productionEntry.place(relx=0.08, rely=0.2, relheight=0.04, relwidth=0.17)

    customerEntry=Entry(orta)
    customerEntry.place(relx=0.08, rely=0.3, relheight=0.04, relwidth=0.17)

    expiration_dateEntry=Entry(orta)
    expiration_dateEntry.place(relx=0.08, rely=0.4, relheight=0.04, relwidth=0.17)

    codeEntry=Entry(orta)
    codeEntry.place(relx=0.08, rely=0.5, relheight=0.04, relwidth=0.17)

    raw_material_codesEntry=Entry(orta)
    raw_material_codesEntry.place(relx=0.08, rely=0.6, relheight=0.04, relwidth=0.17)

    descriptionEntry=Entry(orta)
    descriptionEntry.place(relx=0.08, rely=0.7, relheight=0.04, relwidth=0.17)

    #entryler RAWLAR
    RnameEntry=Entry(orta)
    RnameEntry.place(relx=0.35, rely=0.1, relheight=0.04, relwidth=0.17)

    Rdate_of_pEntry=Entry(orta)
    Rdate_of_pEntry.place(relx=0.35, rely=0.2, relheight=0.04, relwidth=0.17)

    RsuplierEntry=Entry(orta)
    RsuplierEntry.place(relx=0.35, rely=0.3, relheight=0.04, relwidth=0.17)

    Rexpiration_dateEntry=Entry(orta)
    Rexpiration_dateEntry.place(relx=0.35, rely=0.4, relheight=0.04, relwidth=0.17)

    RcodeEntry=Entry(orta)
    RcodeEntry.place(relx=0.35, rely=0.5, relheight=0.04, relwidth=0.17)

    RdecEntry=Entry(orta)
    RdecEntry.place(relx=0.35, rely=0.6, relheight=0.04, relwidth=0.17)

    con = sqlite3.connect("storage.db")
    
    cursor = con.cursor()
    def create_table_products():
        
        cursor.execute("CREATE TABLE IF NOT EXISTS Products (name TEXT, date_of_production date,customer TEXT, expiration_date date, code INT, raw_material_codes INT, description TEXT)")
        con.commit()
        # con.close()
    create_table_products()

    def addProducts():
        value = nameEntry.get()
        value2=date_of_productionEntry.get()
        value3=customerEntry.get()
        value4=expiration_dateEntry.get()
        value5=codeEntry.get()
        value6=raw_material_codesEntry.get()
        value7=descriptionEntry.get()
        cursor.execute("INSERT INTO Products (name, date_of_production, customer, expiration_date, code, raw_material_codes, description) VALUES (?,?,?,?,?,?,?)",(value,value2,value3,value4,value5,value6,value7))

        con.commit()

    addButon = Button(master, text="Add Product",command=addProducts)
    addButon.place(relx=0.47, rely=0.07, relheight=0.06, relwidth=0.07)

    def create_table_raws():
        
        cursor.execute("CREATE TABLE IF NOT EXISTS Raws (name TEXT, date_of_purchase date,supplier TEXT, expiration_date date, code INT, description TEXT)")
        con.commit()
        # con.close()
    create_table_raws()

    def addraws():
        rvalue = RnameEntry.get()
        rvalue2=Rdate_of_pEntry.get()
        rvalue3=RsuplierEntry.get()
        rvalue4=Rexpiration_dateEntry.get()
        rvalue5=RcodeEntry.get()
        rvalue6=RdecEntry.get()
        
        cursor.execute("INSERT INTO Raws (name, date_of_purchase, supplier, expiration_date, code, description) VALUES (?,?,?,?,?,?)",(rvalue,rvalue2,rvalue3,rvalue4,rvalue5,rvalue6))

        con.commit()

    addButon = Button(master, text="Add Raw",command=addraws)
    addButon.place(relx=0.47, rely=0.40, relheight=0.06, relwidth=0.07)

    # def deleteProducts():
    #     delete34 = deleteproentri.get()
        
    #     cursor.execute("DELETE FROM Products WHERE (name)=(?)",(delete34))

    #     con.commit()


    # deleteButon = Button(master, text="Delete",command=deleteProducts)
    # deleteButon.place(relx=0.47, rely=0.14, relheight=0.06, relwidth=0.07)



    # listbox =Listbox(camerayeri)
    # listbox.place()

    def serachson():
        cursor.execute("SELECT * FROM Products")
        data = cursor.fetchall()

        for row in data:
            label = Label(camerayeri, text=row)
            label.place(relx=0.01, rely=0.6, relheight=0.05, relwidth=0.8)

    
   
    btn = Button(camerayeri, text="Show last Product", command=serachson)
    btn.place(relx=0.8, rely=0.7, relheight=0.05, relwidth=0.20)

    def serachsonraw():
        cursor.execute("SELECT * FROM Raws")
        data5 = cursor.fetchall()

        for row in data5:
            label = Label(camerayeri, text=row)
            label.place(relx=0.01, rely=0.85, relheight=0.05, relwidth=0.8)

    
   
    btn2 = Button(camerayeri, text="Show last Raw", command=serachsonraw)
    btn2.place(relx=0.8, rely=0.95, relheight=0.05, relwidth=0.20)

    
    
    button2 = Button(urunarama, text="Show raw info", command=show_raw_info)
    button2.place(relx=0.65, rely=0.5, relheight=0.1, relwidth=0.17)

    

    def save_to_excelforpro():
        cursor.execute("SELECT * FROM products")
        data = cursor.fetchall()


        df = pd.DataFrame(data, columns=['name','date_of_production','customer','expiration_date','code','raw_material_codes','description'])
        df.to_excel("products.xlsx", index=False)
        df.to_excel("products.xlsx", index=False)


    

    def save_to_excelforraw():
        cursor.execute("SELECT * FROM Raws")
        data2 = cursor.fetchall()


        df = pd.DataFrame(data2, columns=['name','date_of_purchase','supplier','expiration_date','code','description'])
        df.to_excel("raws.xlsx", index=False)
        df.to_excel("raws.xlsx", index=False)
    
    saveButon = Button(master, text="Save Exel file for Pro.",command=save_to_excelforpro)
    saveButon.place(relx=0.925, rely=0.925, relheight=0.06, relwidth=0.07)

    saveButon = Button(master, text="Save Exel file for raws",command=save_to_excelforraw)
    saveButon.place(relx=0.725, rely=0.925, relheight=0.06, relwidth=0.07)


    ####makyaj
    prolabel=Label(orta, text="Product", bg='#add8e6', font="Verdana 8 bold")
    prolabel.place(relx=0.08, rely=0.05, relheight=0.04, relwidth=0.17)

    prolabel=Label(orta, text="Raw Material", bg='#add8e6', font="Verdana 8 bold")
    prolabel.place(relx=0.34, rely=0.05, relheight=0.04, relwidth=0.2)


    hcg=Label(urunarama, text="Halit Can Güneri", bg='#add8e6', font="Verdana 15 bold")
    hcg.place(relx=0.5, rely=0.65, relheight=0.04, relwidth=0.37)



    aciklama=Label(urunarama, text="Proje açıklaması: Bu proje bir\n pastane deposu için geliştirilmiştir.\n3 ana bölüme ayrılır.Bunlar depoyu\n izleyen kamera bölmesi, ürün ekleme\n bölgesi, ürün arama bölgesidir.", bg='#add8e6', font="Verdana 8 bold")
    aciklama.place(relx=0.45, rely=0.24, relheight=0.2, relwidth=0.6)






    master.mainloop()


