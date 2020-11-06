from tkinter import *
import mysql.connector
from mysql.connector import Error
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from datetime import datetime

#ARUSH PART START-------------------------------------------------------------------------------------------------
try:
    flag = 0
    con = mysql.connector.connect(host='localhost', user='root', password='flightroot123',database='flight')
    cur = con.cursor(buffered=True)
    cur.execute("SHOW DATABASES")
    for x in cur.fetchall():
        for y in x:
            if y == 'flight':
                flag = 1
                break
    if flag != 1:
        cur.execute("CREATE DATABASE flight")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS price_record(From1 varchar(50),To1 varchar(50),price1 FLOAT);")
    con.commit()
#ARUSH PART END---------------------------------------------------------------------------------------------------

#SWARIT PART START---------------------------------------------------------------------------------------------------
    root = Tk()
    root.geometry('600x500')
    root.minsize(600, 500)  # min width,height
    root.maxsize(600, 500)
    root.geometry("{}x{}+{}+{}".format(600, 500, int((root.winfo_screenwidth() / 2) - (600 / 2)),
                                       int((root.winfo_screenheight() / 2) - (500 / 2))))

    root.title("Flight Price System")
    main_icon = PhotoImage(file="travelling.png")
    root.iconphoto(True, main_icon)

    root.configure(background="white")

    heading1 = Label(root, text=" AirTicket Price Predictor\n", font=("Arial Rounded MT Bold", 26), bg='white',
                     fg='black')
    heading1.pack()

    main_icon = PhotoImage(file='travelling.png')
    main_icon_label = Label(root, image=main_icon, bg='white')
    main_icon_label.pack()

    heading2 = Label(root,
                     text="\n\nProject Submitted By: \n\n➡Swarit Srivastava\n➡Mohit Pal Singh \n➡Arush Nigam\n\n\n",
                     font=("Helvetica 12 bold"), bg='white', fg='black')
    heading2.pack()


    def airline_price():
        root.destroy()
        root1 = Tk()
        root1.focus_force()  # To bring the window in focus
        root1.title("Flight Fare Predictor Portal")
        root1.geometry('600x600')
        root1.minsize(600, 600)  # min width,height
        root1.maxsize(600, 600)
        root1.geometry("{}x{}+{}+{}".format(600, 600, int((root1.winfo_screenwidth() / 2) - (600 / 2)),
                                            int((root1.winfo_screenheight() / 2) - (600 / 2))))
    
        root1.configure(background='white')

        Label(root1, text="Welcome to Airline Price Prediction System", font=("Arial 93", 17), fg="Red",
              bg="White").place(relx=0.5, y=20, anchor='center')
        Label(root1, text="Enter the Flight Details", font=("Arial 93", 17), fg="White", bg="Orange").place(relx=0.5,
                                                                                                            y=50,
                                                                                                            anchor='center')

        one_or_round = IntVar()
        r1 = Radiobutton(root1, text="One way", value=1, variable=one_or_round, bg="White", font=("Arial 93", 12))
        r1.place(relx=0.25, y=100, anchor='center')
        r2 = Radiobutton(root1, text="Round-trip", value=2, variable=one_or_round, bg="White", font=("Arial 93", 12))
        r2.place(relx=0.75, y=100, anchor='center')

        Label(root1, text="Boarding: ", font=("Arial 93", 14), fg="black", bg="White").place(relx=0.1, y=150,
                                                                                             anchor='w')
        source = StringVar(root1)
        source.set("From ")  # default value
        w = OptionMenu(root1, source, "delhi", "banglore", "mumbai", "hyderabad", "chennai", "kolkata", "surat")
        w.config(font=('calibri', (12)), bg='white', width=22, indicatoron=0, anchor=W)
        w.place(relx=0.75, y=150, anchor='center')

        Label(root1, text="Destination: ", font=("Arial 93", 14), fg="black", bg="White").place(relx=0.1, y=200,
                                                                                                anchor='w')
        destination = StringVar(root1)
        destination.set("To ")  # default value
        w = OptionMenu(root1, destination, "delhi", "banglore", "mumbai", "hyderabad", "chennai", "kolkata", "surat")
        w.config(font=('calibri', (12)), bg='white', width=22, indicatoron=0, anchor=W)
        w.place(relx=0.75, y=200, anchor='center')

        Label(root1, text="Date: ", font=("Arial 93", 14), fg="black", bg="White").place(relx=0.1, y=250, anchor='w')
        global datee
        datee = StringVar(root1)
        DateEntry(root1, width=28, height=2, bg="black", fg="white", year=2020, textvariable=datee).place(relx=0.75,
                                                                                                          y=250,
                                                                                                          anchor='center')

        Label(root1, text="Timing: ", font=("Arial 93", 14), fg="black", bg="White").place(relx=0.1, y=300, anchor='w')
        timing = IntVar()
        timing.set(2)
        r1 = Radiobutton(root1, text="8AM to 9PM", value=1, variable=timing, bg="White", font=("Arial 93", 12))
        r1.place(relx=0.60, y=300, anchor='center')
        r2 = Radiobutton(root1, text="9PM to 8AM", value=2, variable=timing, bg="White", font=("Arial 93", 12))
        r2.place(relx=0.85, y=300, anchor='center')

        Label(root1, text="Class: ", font=("Arial 93", 14), fg="black", bg="White").place(relx=0.1, y=350, anchor='w')

        passengerClass = IntVar()
        Checkbutton(root1, text='Economy', variable=passengerClass, offvalue=0, onvalue=0, bg="white").place(relx=0.50,
                                                                                                             y=350,
                                                                                                             anchor='w')
        Checkbutton(root1, text='Business', variable=passengerClass, offvalue=0, onvalue=1, bg="white").place(relx=0.65,
                                                                                                              y=350,
                                                                                                              anchor='w')
        Checkbutton(root1, text='First Class', variable=passengerClass, offvalue=0, onvalue=2, bg="white").place(
            relx=0.80, y=350, anchor='w')

        Label(root1, text="Airline: ", font=("Arial 93", 14), fg="black", bg="White").place(relx=0.1, y=400, anchor='w')

        img1 = PhotoImage(file='airindia.png')
        img2 = PhotoImage(file='spicejet.png')

        airline_brand = IntVar()
        Checkbutton(root1, text='Air India', variable=airline_brand, offvalue=0, onvalue=1, image=img1, compound=LEFT,
                    bg="white").place(relx=0.5, y=400, anchor='w')
        Checkbutton(root1, text='SpiceJet', variable=airline_brand, offvalue=0, onvalue=2, image=img2, compound=LEFT,
                    bg="white").place(relx=0.75, y=400, anchor='w')
#SWARIT PART END----------------------------------------------------------------------------------------------------------

#ARUSH PART START--------------------------------------------------------------------------------------------------------------        
        def onClickShowAllF2():
            showAll = Tk()
            showAll.title("Records")
            showAll.configure(bg='grey')
            showAll.geometry('600x800')

            p1 = Label(showAll, text='S.No.', font='time 16 bold', fg='black', bg='grey')
            p1.grid(row=1, column=0, padx=10, pady=10)
            p2 = Label(showAll, text='From', font='time 16 bold', fg='black', bg='grey')
            p2.grid(row=1, column=1, padx=10, pady=10)
            p3 = Label(showAll, text='To', font='time 16 bold', fg='black', bg='grey')
            p3.grid(row=1, column=2, padx=10, pady=10)
            p4 = Label(showAll, text='Price', font='time 16 bold', fg='black', bg='grey')
            p4.grid(row=1, column=3, padx=10, pady=10)

            def clear_data():
                 option = messagebox.askyesno("Caution!", "Pressing Yes Will Delete All Your Records")
                 if option:
                        cur = con.cursor()
                        Delete_all_rows = "TRUNCATE TABLE price_record"
                        cur.execute(Delete_all_rows)
                        con.commit()
                        messagebox.showinfo("Deleted!", "All Records Deleted successfully ")
                        showAll.destroy()
                        onClickShowAllF2()
                        
                 else:
                        pass  


            
            Button(showAll, text="Clear Data", font=("Arial", 16), fg="white", bg="red", width=10,
            height=1, cursor="hand2", command=clear_data).grid(row=1, column=5)
            

            # Selecting query form database
            query = 'SELECT * FROM flight.price_record'
            cur.execute(query)

            result = cur.fetchall()
            num = 2
            for x in result:  # print all the records................................
                sno = Label(showAll, text=num-1, font="time 12 bold", fg="orange", bg='black')
                sno.grid(row=num, column=0, pady=10, padx=10)

                city = Label(showAll, text=x[0], font="time 12 bold", fg="orange", bg='black')
                city.grid(row=num, column=1, padx=10, pady=10)

                nigam = Label(showAll, text=x[1], font="time 12 bold", fg="orange", bg='black')
                nigam.grid(row=num, column=2, padx=10, pady=10)

                arush = Label(showAll, text=x[2], font="time 12 bold", fg="orange", bg='black')
                arush.grid(row=num, column=3, padx=10, pady=10)

                num += 1
#ARUSH PART END------------------------------------------------------------------------------------------------------------                


#MOHIT PART START----------------------------------------------------------------------------------------------------------
        def show_result():

            def one_or_round_trip():
                global basePrice, result
                if (one_or_round.get() == 2):
                    basePrice = basePrice * 1.8

            def calculateBasePrice():
                global journey, distance, basePrice

                journey = source.get() + destination.get()
                distance = faresDictionary[journey]
                distance = int(distance)
                if distance < 1200:
                    basePrice = distance * 2.5
                elif distance < 1700:
                    basePrice = distance * 1.9
                elif distance < 2500:
                    basePrice = distance * 1.6

            def checkDate():
                global basePrice

                date = datee.get()
                date = datetime.strptime(date, '%m/%d/%y')

                today = datetime.now()
                daysDifference = (date - today).days

                if daysDifference < 7:
                    basePrice = basePrice * 1.6
                elif daysDifference < 18:
                    basePrice = basePrice * 1.4
                elif daysDifference < 30:
                    basePrice = basePrice * 1.2

            def checktime():
                global basePrice
                if (timing.get() == 1):
                    basePrice = basePrice * 1.13
                else:
                    basePrice = basePrice * 1.09

            def checkPassengerClass():
                global basePrice
                if passengerClass.get() == 2:
                    basePrice = basePrice * 2
                elif passengerClass.get() == 1:
                    basePrice = basePrice * 1.5
                else:
                    basePrice = basePrice * 1

            def airline():
                global basePrice
                if (airline_brand.get() == 2):
                    basePrice = basePrice + 800

            faresDictionary = {"mumbaidelhi": "1413", "mumbaibanglore": "0981", "mumbaihyderabad": "0709",
                               "mumbaichennai": "1331", "mumbaikolkata": "2048", "mumbaisurat": "0283",
                               "delhimumbai": "1413", "delhibanglore": "2177", "delhihyderabad": "1586",
                               "delhichennai": "2210", "delhikolkata": "1491", "delhisurat": "1157",
                               "bangloremumbai": "0981", "bangloredelhi": "2177", "banglorehyderabad": "0569",
                               "banglorechennai": "0346", "banglorekolkata": "1878", "bangloresurat": "1252",
                               "hyderabadmumbai": "0709", "hyderabaddelhi": "1586", "hyderabadbanglore": "0569",
                               "hyderabadchennai": "0626", "hyderabadkolkata": "1492", "hyderabadsurat": "0987",
                               "chennaimumbai": "1331", "chennaidelhi": "2210", "chennaibanglore": "0346",
                               "chennaihyderabad": "0626", "chennaikolkata": "1672", "chennaisurat": "1605",
                               "kolkatamumbai": "2048", "kolkatadelhi": "1491", "kolkatabanglore": "1878",
                               "kolkatahyderabad": "1492", "kolkatachennai": "1672", "kolkatasurat": "2010",
                               "suratmumbai": "0283", "suratdelhi": "1157", "suratbanglore": "1252",
                               "surathyderabad": "0987", "suratchennai": "1605", "suratkolkata": "2010"}

            try:
                global basePrice

                calculateBasePrice()

                one_or_round_trip()
                checkDate()
                checktime()
                checkPassengerClass()
                airline()

                basePrice = round(basePrice, 2)
                result = "Price Predicted: Rs. " + str(basePrice)
                l = Label(root1, text=result, font=("Arial 93", 14), fg="black", bg="White").place(relx=0.5, y=550,
                                                                                                   anchor='center')
            except:
                messagebox.showerror("Error", "Choose correct source and destination!")
            finally:
                query = 'INSERT INTO flight.price_record(From1,To1,price1) values(%s, %s, %s);'
                values = (source.get(), destination.get(), basePrice)
                cur.execute(query, values)
                con.commit()
                print('sucessfully inserted')
                # print(source.get(), destination.get(), basePrice)
#MOHIT PART END----------------------------------------------------------------------------------------------------------                

        Button(root1, text="Flight Price", font=("Arial", 16), fg="white", bg="black", compound="center", width=15,
               height=1, cursor="hand2", command=show_result).place(relx=0.50, y=480, anchor='center')

        show_data = PhotoImage(file='showdata.png')        
        Button(root1, text="Show Data", font=("Arial", 12), image=show_data, fg="red", bg="white", compound="left",
               cursor="hand2", command=onClickShowAllF2).place(relx=0.85, y=550, anchor='center')

        root1.mainloop()


    button1 = Button(root, text="Proceed to Project", command=airline_price, compound="center", bg="black",
                     font=("Calibri", 20), fg="white", cursor="hand2")
    button1.pack()
    root.mainloop()

except Error as err:
    print(err)
# Finally block for connection giving message for connection close..................................
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print('connection is closed')
