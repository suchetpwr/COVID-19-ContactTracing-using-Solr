from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import csv
import requests

master = Tk()

master.geometry("700x700")

firstname = StringVar()
surname = StringVar()
cNumber = StringVar()
token = StringVar()
StoreInfo = StringVar()
Date = StringVar()

searchFName = StringVar()
searchLName = StringVar()
searchCNumber = StringVar()
searchStoreVisited = StringVar()
searchCounter1 = StringVar()
searchCounter2 = StringVar()
tokenVal = StringVar()

def search_person():
    resultWindow = Toplevel(master)
    resultWindow.title("Search Result")
    resultWindow.geometry("500x500")
    #tempSearchFName = searchFName.get()
    #tempSearchLName = searchLName.get()
    tempSearchCNumber = searchCNumber.get()
    if(tempSearchCNumber == ""):
        print('Error')
        messagebox.showerror("error", "Please enter contact number")
    else: 
        params = (
        ('q', 'ContactNumber:%s'%tempSearchCNumber),
        )
        response = requests.get('http://localhost:8983/solr/NewCore/select', params=params)

    lblResult = Label(resultWindow, text = response.text, font = ('Arial',14)).grid(row = 5, column = 3)
    #messagebox.showinfo("result", response.text)

def search_related():
    searchWindowNew = Toplevel(master)
    searchWindowNew.title("People to contact")
    searchWindowNew.geometry("1000x1000")

    lblHeadingSearch = Label(searchWindowNew, text = "Please enter the details from previous window here", font = ('Arial',24,"bold")).grid(row = 0, column =0, columnspan = 4, padx =50, pady =10)

    lblSearchStoreVisited = Label(searchWindowNew, text = "Enter the Store Visited information from pervious window", font = ('Arial',14,"bold")).grid(row = 1, column =1)
    entrySearchStoreVisited = Entry(searchWindowNew, textvariable = searchStoreVisited, width = 10).grid(row=1, column = 2)

    lblSearchCounter = Label(searchWindowNew, text = "Enter the Counter Range based on counter value from previous window", font = ('Arial',14,"bold")).grid(row = 2, column =1)
    entrySearchCounter1 = Entry(searchWindowNew, textvariable = searchCounter1, width = 10).grid(row=2, column = 2)
    lblTO = Label(searchWindowNew, text = "TO", font = ('Arial',14,"bold")).grid(row = 2, column =3)
    entrySearchCounter2 = Entry(searchWindowNew, textvariable = searchCounter2, width = 10).grid(row=2, column = 4)

    searchRelatedContactbtn = Button(searchWindowNew, text = "Search People to Contact", command = search_related_results).grid(row = 4, column = 2, sticky = E, padx = 50, pady = 10)

def search_related_results():
    finalResultWindow = Toplevel(master)
    finalResultWindow.title("People to Contact")
    finalResultWindow.geometry("1000x1000")
    tempSV = searchStoreVisited.get()
    tempR1 = searchCounter1.get()
    tempR2 = searchCounter2.get()
    params = (
    ('q', 'StoreVisited:%s AND counter:[%s TO %s]'%(tempSV, tempR1, tempR2)),
    )

    response2 = requests.get('http://localhost:8983/solr/NewCore/select', params=params)
    lblResult = Label(finalResultWindow, text = response2.text, font = ('Arial',14)).grid(row = 5, column = 3)
    
def searchThrough():
    searchWindow = Toplevel(master)
    searchWindow.title("Search")
    searchWindow.geometry("500x500")
    lblHeadingSearch = Label(searchWindow, text = "Search through data", font = ('Arial',24,"bold")).grid(row = 0, column =0, columnspan = 4, padx =50, pady =10)

    #lblSearchFirstName = Label(searchWindow, text = "Enter First Name", font = ('Arial',14,"bold")).grid(row = 1, column =1)
    #entrySearchFirstName = Entry(searchWindow, textvariable = searchFName, width = 10).grid(row=1, column = 2)


    #lblSearchLastName = Label(searchWindow, text = "Enter Last Name", font = ('Arial',14,"bold")).grid(row = 2, column =1)
    #entrySearchLastName = Entry(searchWindow, textvariable = searchLName, width = 10).grid(row=2, column = 2)

    lblSearchContactNumber = Label(searchWindow, text = "Enter Contact Number", font = ('Arial',14,"bold")).grid(row = 3, column =1)
    entrySearchContactNumber = Entry(searchWindow, textvariable = searchCNumber, width = 10).grid(row=3, column = 2)

    searchContactbtn = Button(searchWindow, text = "Search Contact", command = search_person).grid(row = 4, column = 0, sticky = E, padx = 50, pady = 10)
    #print(searchFName)
    
    

def openEntryWindow():
    newWindow = Toplevel(master)
    newWindow.title("Add an Entry")
    newWindow.geometry("800x800")
    lblHeading = Label(newWindow, text = "Add a new Entry", font = ('Arial',24,"bold")).grid(row = 0, column =0, columnspan = 4, padx =50, pady =10)

    lblFirstName = Label(newWindow, text = "First Name", font = ('Arial',14,"bold")).grid(row = 1, column =1)
    entryFirstName = Entry(newWindow, textvariable = firstname, width = 10).grid(row=1, column = 2)
    
    lblLastName = Label(newWindow, text = "Last Name", font = ('Arial',14,"bold")).grid(row = 2, column =1)
    entryLastName = Entry(newWindow, textvariable = surname, width = 10).grid(row=2, column = 2)

    lblContact = Label(newWindow, text = "Contact Number", font = ('Arial',14,"bold")).grid(row = 3, column =1)
    entryContact = Entry(newWindow, textvariable = cNumber, width = 10).grid(row=3, column = 2)

    lblStoreVisited = Label(newWindow, text = "Store Visited", font = ('Arial',14,"bold")).grid(row = 4, column =1)
    entrySV = Entry(newWindow, textvariable = StoreInfo, width = 10).grid(row=4, column = 2)

    lblDate = Label(newWindow, text = "Date", font = ('Arial',14,"bold")).grid(row = 5, column =1)
    entryDate = Entry(newWindow, textvariable = Date, width = 10).grid(row=5, column = 2)

    f = open('newDataFile.csv', 'r')
    csv_f = csv.reader(f)

    token_list = []
    for row in csv_f:
        #print(row)
        token_list.append(row[5])

    length = len(token_list)
    for i in range(length):
        if(i == length -1):
            tokenVal = token_list[i]

    lblTokenDisplay1 = Label(newWindow, text = "Please enter a token value for this entry.", font = ('Arial',14,"bold")).grid(row = 6, column =1)
    lblTokenDisplay1 = Label(newWindow, text = "Note the current token value and enter current token + 1 in the box below", font = ('Arial',14,"bold")).grid(row = 7, column =1)
    lblTokenDisplay = Label(newWindow, text = "Current Token Number = %s"%tokenVal, font = ('Arial',14,"bold")).grid(row = 8, column =1)

    lblToken = Label(newWindow, text = "Token Number", font = ('Arial',14,"bold")).grid(row = 9, column =1)
    entryToken = Entry(newWindow, textvariable = token, width = 10).grid(row=9, column = 2)
    

    subbtn = Button(newWindow, text = "Submit", command = store_info).grid(row = 10, column = 2, sticky = E, padx = 50, pady = 10)
    

def store_info():
    tempFirstName = firstname.get()
    tempLastName = surname.get()
    tempContactNumber = cNumber.get()
    tempToken = token.get()
    tempStore = StoreInfo.get()
    tempDate = Date.get()
    if(tempFirstName == "" or tempLastName == "" or tempContactNumber == "" or tempToken == "" or tempStore == "" or tempDate == ""):
        print('Error')
        messagebox.showerror("error", "You have not entered all the information")
        firstname.set("")
        surname.set("")
        cNumber.set("")
        token.set("")
        StoreInfor.set("")
        Date.set("")
    with open('newDataFile.csv', 'a', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerow([tempFirstName, tempLastName, tempContactNumber, tempStore, tempDate, tempToken])
    csvfile.close()
    

label = Label(master, text="This is the main window")

label.pack(pady = 10)

btnNewEntry = Button(master, text = "New Entry", command = openEntryWindow)
btnNewEntry.pack(pady = 10)

btnSearch = Button(master, text = "Search Person", command = searchThrough)
btnSearch.pack(pady = 50)

btnSearchRelated = Button(master, text = "Search people to Contact", command = search_related)
btnSearchRelated.pack(pady = 50)

mainloop()
