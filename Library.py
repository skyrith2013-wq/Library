import json , time , random , os
from datetime import datetime

def Mains():
    try:
        class library():

            # GREETING

            @staticmethod
            def greeting():
                ct =  datetime.now().hour
                if ct < 12:
                    print("\n            Good Morning")
                elif ct < 17:
                    print("\n            Good Afternoon")
                else:
                    print("\n            Good Evening")
                print("""
    ====================================
           WELCOME TO SKY LIBRARY     
    ====================================\n""")

            def __init__(self, filename = "Library_store.json"):
                self.filename = filename

            # SET CURRENT USER

            def set_current_user(self, mo_no, User_code):
                with open(self.filename, "r") as j:
                    readers = json.load(j)

                    self.value = False
                    for idx, i in enumerate(readers):
                        if i["Mobile Number"] == mo_no and i["User_code"] == User_code:
                            self.current_user = i
                            self.current_index = idx  
                            self.value = True
                            break
                        else:
                            self.value = False
                            break
                    
            # EXPIRING

            def expiring(self):
                print("Checking Your Membership.....")
                time.sleep(3)
                if len(str(self.current_user['User_code'])) == 7:
                    if (self.current_user['Time'] - time.time())/86400 > 1:
                        print("Your Subscribtion Has Been Expired!")
                        exit()

                elif len(str(self.current_user['User_code'])) == 10:
                    if (self.current_user['Time'] - time.time())/86400 > 7:
                        print("Your Subscribtion Has Been Expired!")
                        exit()

                elif len(str(self.current_user['User_code'])) == 12:
                    if (self.current_user['Time'] - time.time())/86400 > 30:
                        print("Your Subscribtion Has Been Expired!")
                        exit()

                elif len(str(self.current_user['User_code'])) == 15:
                    if (self.current_user['Time'] - time.time())/86400 > 365:
                        print("Your Subscribtion Has Been Expired!")
                        exit()

                elif len(str(self.current_user['User_code'])) == 17:
                    print(f"ooh, {self.current_user['Name']} You Are VIP\nYou Can Read Books For Infinite Time's In Sky Library!")
                    
            # WORKING

            def working(self):
                self.greeting()
                NO = input("Are You New To Our Library (Yes/No) --> ").lower()
                if NO == "yes":
                    self.New()

                elif NO == "no":
                    name = str(input("Enter Your Name --> "))
                    MO_number = int(input("Enter Your Mobile Number --> "))
                    User_Code = int(input("Enter Your User Code --> "))
                    if name.isdigit():
                        print("Enter A Valid Name!")
                        exit()

                    if len(str(User_Code)) != 10:
                        print("Length of Mobile Number Is 10-digits !")
                        exit()

                    if MO_number < 0:
                        print("Enter A Positive Number!")
                        exit()

                    if MO_number < 0:
                        print("Enter A Positive Number!")
                        exit()

                    self.set_current_user(MO_number, User_Code)

                    if self.value == True:
                        self.expiring()

                        self.start = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
                        print("Now You Can Read Books ")
                        time.sleep(4)
                        self.out = input("Do You Want To Come Out ? ").lower()
                        print(self.out)
                        if self.out == "yes":
                            time.sleep(1)
                            print("Thank's For Vising!")
                        else:
                            print("Enter Something Valid!")
                        self.current_user['Visiting'].append({"From": self.start,
                                                            "To": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")})
                        self.storing()
                    else:
                        print("You Don't Have A Membership In Our Library!")
                        make = str(input("Do You Want To Make One --> "))

                        if make == "yes":
                            print("Let's Create An Account\nProcessing.....")
                            time.sleep(3)
                            self.New()

                        elif make == "no":
                            print("Thank's For Visiting!")
                            exit()

                        else:
                            print("Enter Something Valid!")
                
                else:
                    print("Enter Something Valid!")
                    exit()

            # STORING

            def storing(self):
                try:
                    with open(self.filename, "r") as J:
                        readers = json.load(J)
                        if not isinstance(readers, list):
                            readers = [readers]
                except (FileNotFoundError, json.JSONDecodeError):
                    readers = []

                if hasattr(self, "current_index"):
                    readers[self.current_index] = self.current_user
                else:
                    print("Error: current user index not found, cannot update safely.")
                    return

                with open(self.filename ,"w") as f:
                    json.dump(readers , f , indent=4)

            # PAYMENT

            def Payment(self, amt):
                Bank_file = "D:\Code\Python\Suraj of python\Old_Bank\CBSE_Store.json"
                print("""How do You Wanna Pay ?
1 : CBSE Bank\n""")
                pay_M = int(input("--> "))

                if pay_M == 1:
                    
                    account_no = int(input("Enter Your Account Number --> "))

                    if len(str(account_no)) != 12:
                        print("Length Of Account Number Is 12 digit !")
                        exit()
                    if account_no < 0:
                        print("Account Number Should be Positive !")
                        exit()

                    PIN = int(input("Enter Your PIN --> "))

                    if PIN < 0:
                        print("PIN Should be Positive !")
                        exit()
                    if len(str(PIN)) != 4:
                        print("Length Of PIN Is 4 digit !")
                        exit()

                    with open(Bank_file ,"r") as J:
                        accounts = json.load(J)

                    for k ,account in enumerate(accounts):
                        if account.get('Account Number') == str(account_no) and account.get('PIN') == PIN:

                            print(f"Processing your Payment of ₹{amt}")
                            time.sleep(4)

                            current_balance = account.get('Bank Balance', account)
                            if current_balance >= amt:

                                accounts[k]['Bank Balance'] = current_balance - amt

                                with open(Bank_file ,"w") as f:
                                    json.dump(accounts , f , indent=4)
                                print(f"The Payment Of ₹{amt} Has Been Done")
                                break
                            
                            else:
                                print("You Don't Have Enough Money !")
                                exit()
                else:       
                    print("please Enter Something Valid!")
                    exit()

        # ------------------------
        #        NEW USER
        # ------------------------

            def New(self):

                nameing = str(input("Enter Your Name --> "))
                if nameing.isdigit():
                    print("Enter Something Valid!")
                    exit()

                MO_No = int(input("Enter Your Mobile Number --> "))
                if len(str(MO_No)) != 10:
                    print("Length Of Mobile Number Is 10 digit !")
                    exit()
                if MO_No < 0:
                    print("Mobile Number Should be Positive")
                    exit()

                print("""
        Daily : Amount - ₹50
        Weekly : Amount - ₹150
        Monthly : Amount - ₹500
        Yearly : Amount - ₹5000
        VIP : Amount - ₹7000
                                                            """)
                                        
                subscribtion = str(input("Which subscribtion Do you Want ? ")).lower()

                # SUBSCIBTIONS

                if subscribtion == "daily":

                    self.Payment(50)
                    time.sleep(2)
                    User_code = random.randint(10**7, 10**8-1)
                    self.Data(nameing, MO_No, User_code)
                    print(f"Your User Code is {User_code} (not this and do not share)")
                    time.sleep(1)
                    print("You are Now Registered To Our Library!")

                elif subscribtion == "weekly":

                    self.Payment(150)
                    time.sleep(2)
                    User_code = random.randint(10**10, 10**11-1)
                    self.Data(nameing, MO_No, User_code)
                    print(f"Your User Code is {User_code} (not this and do not share)")
                    time.sleep(1)
                    print("You are Now Registered To Our Library!")


                elif subscribtion == "monthly":
                        
                    self.Payment(500)
                    time.sleep(2)
                    User_code = random.randint(10**12, 10**13-1)
                    self.Data(nameing, MO_No, User_code)
                    print(f"Your User Code is {User_code} (do not this and do not share)")
                    time.sleep(1)
                    print("You are Now Registered To Our Library")
                
                elif subscribtion == "yearly":

                    self.Payment(5000)
                    time.sleep(2)
                    User_code = random.randint(10**15, 10**16-1)
                    self.Data(nameing, MO_No, User_code)
                    print(f"Your User Code is {User_code} (do not this and do not share)")
                    time.sleep(1)
                    print("You are Now Registered To Our Library!")


                elif subscribtion == "vip":

                    self.Payment(7000)
                    time.sleep(2)
                    User_code = random.randint(10**17, 10**18-1)
                    self.Data(nameing, MO_No, User_code)
                    print(f"Your User Code is {User_code} (do not this and do not share)")
                    time.sleep(1)
                    print("You are Now Registered To Our Library!")

                else:
                    print("Enter Something Valid !")

            # STORING DATA
                
            def Data(self, nameing, MO_No, User_code):
                data = {
                    "Name": nameing,
                    "Mobile Number": MO_No,
                    "User_code": User_code,
                    "Time": time.time(),
                    "Visiting": []
                }

                filename = "Library_store.json"
                if os.path.exists(filename):
                    with open(filename, "r") as J:
                        try:
                            readers = json.load(J)
                            if not isinstance(readers, list):
                                readers = [readers]
                        except json.JSONDecodeError:
                            readers = []
                else:
                    readers = []
                readers.append(data)
                with open(filename, "w") as f:
                    json.dump(readers, f, indent=4)

        l = library()
        l.working()

    except Exception as e:
        print(f"Something Went Wrong!")

if __name__ == "__main__":
    Mains()

                