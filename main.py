import csv
import os
# Student basic information holder
class student:
    def __init__(self,reg,name,branch,room,feestat):
        self.reg=reg
        self.name=name
        self.branch=branch
        self.room=room
        self.feestat=feestat

    def aslist(self):
        return[self.reg,self.name,self.branch,self.room,self.feestat]
        #main hostel manager
class hostelmanager:
    def __init__(self, file_path="students.csv"):
        self.file_path = file_path
        self.students=[]
        self.setup()
        self.load()
            #make sure folder and file exists
    def setup(self):
        if not os.path.isdir("data"):
            os.makedirs("data")
        if not os.path.isfile(self.file_path):
            with open(self.file_path,"w",newline="")as f:
                wr=csv.writer(f)
                wr.writerow(["regno","name","branch","room","feestatus"])
                                     
                #load csv data into list
    def load(self):
        self.students=[]
        try:
            with open(self.file_path,"r")as f:
                rd=csv.reader(f)
                next(rd,None)
                for row in rd:
                    if row:
                        stu = student(row[0],row[1],row[2],row[3],row[4])
                        self.students.append(stu)

        except Exception as e:
            print("error reading file, staring new.",e)
                                
                                #save to csv
    def save (self):
        with open(self.file_path,"w",newline="")as f: 
            wr=csv.writer(f)
            wr.writerow(["regno","name","branch","room","feestatus"])
            for s in self.students:
                wr.writerow(s.aslist())
        print("data updated.")
                                            # add a frsh student entry
    def addstudent (self):
        print("\n add student")
        reg=input("registration no:")

                    #avoid duplicates
        for s in self.students:
            if s.reg==reg:
                print("A student with this reg no already exists.")
                return
        name =input("name:")
        branch=input("branch:")
        room=input("room no:")
        fee=input("fee status(paid/pending):")

        new_stu=student(reg,name,branch,room,fee)
        self.students.append(new_stu)
        self.save()
        print(f"{name} added to room {room}.")

                #show everything
    def viewall(self):
        print("\n student list")
        if not self.students:
            print("no records found.")
            return
        print(f"{'regno':<12}{'name':<20}{'room':<10}{'fees'}")
        print("-"*50)
        for s in self.students:
             print(f"{s.reg:<12}{s.name:<20}{s.room:<10}{s.feestat}")
        print("-"*50)
                 #delete student

    def removestudent(self):
        reg=input("enter reg no to remove:")
        for s in self.students:
            if (s.reg==reg):    
                self.students.remove(s)
                self.save()
                print("record removed.") 
                return
        print("student with that reg no not found.")        
                 #stats
    def stats(self):
        total=len(self.students)
        paid=sum(1 for s in self.students if s.feestat.lower()=='paid')
        print("\n stats")
        print("total students:",total)
        print("paid fees:",paid)
        print("pening fees:",total-paid)
def main():
    hm=hostelmanager()
    while True:
        print("\n hostel management menu ")
        print("enter 1 to add student")
        print("enter 2 to view students")
        print("enter 3 to remove student")
        print("enter 4 to view stats")
        print("enter 5 to quit")
        ch=input("select an option:")
        if (ch=="1"):
            hm.addstudent()
        elif(ch=="2"):
            hm.viewall()
        elif(ch=="3"):
            hm.removestudent()
        elif(ch=="4"):
            hm.stats()
        elif(ch=="5"):
            print("Thank you, have a nice day!")
            break
        else:
            print("invalid choice, try again.")

if(__name__=="__main__"):
    main()
