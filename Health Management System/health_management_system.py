import datetime  # To save the log data with time
import json  # To save the given usernames as json format and reused.
import os  # To create the log files with the user name and type


class Healthmanager():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    saved_dir = "Cached_Data"
    filename = f"{saved_dir}/names.json"
    topics_json_filename = f"{saved_dir}/topics.json"
    logged_dir = "Log files"
    def __init__(self, dictionary):
        '''
        Init the Health Manager Function and create the class instances. Such as : ]
        1."clientDict" - The dictionary of all user names with a unique number key
        2."values" - The blank list to use it as a list of names on the class
        3."i" - The name counter of the clientDict dictionary- use as key of clientDict.
        '''
        self.i = 1
        self.clientDict = dictionary
        self.savePoints = {"1":"Food", "2": "Exercise"}
        self.values = []
        self.readNames()
        self.getSaveTopics()
        self.ensureDir(self.saved_dir)
        if len(self.clientDict) == 0:
            self.assignNames()
    
    def initial(self):
        '''
        Take the necessary input from the user and decide the filename as {username}-food
        or {username}-exercise for logging data & also decide which data to retrive
        and show the data to user. 
        '''
        try:
            print("------------------------")
            self.showNames()
            print("------------------------")
            name = input("Your option : ")
            name = self.clientDict.get(name)
            print("------------------------")
            print(f"*** Initializing for \"{name}\" ***")
            print(f"1 for log")
            print(f"2 for retrieve")
            print("------------------------")
            option = input("Enter your option : ")
            print("------------------------")

            if option == "1":
                option = "log"
            elif option == "2":
                option = "retrive"
            else:
                main()
                
            print(f"What you want to {option}.")
            for key, value in self.savePoints.items():
                print(f"{key}. {value}")
            print("------------------------")
            a = input(" * Choose your option : ")
            print("------------------------")
            fileEx = self.savePoints.get(a)
                

            if option == "log":
                storevalue = input("Type Here :\n")
                self.log(name, storevalue, fileEx)
            else:
                self.retrieve(name, fileEx)

        except ValueError:
            print(f"{self.FAIL}Invalid Value!{self.ENDC}")

    def updateValuesOfDict(self):
        '''Append the names of clientDict to self.values list'''
        for value in self.clientDict.values():
            self.values.append(value.lower())

    def log(self, name, storevalue, fileEx):
        self.ensureDir(self.logged_dir)
        '''
        Save the data to a .log file as given parameters: (name, fileEx, storvalue)
        name - The name of the log file
        fileEx - The extra part of filename to name a meaningful file
        storvalue - The data to save the file
        '''
        for value in self.clientDict.values():
            if name == value:
                with open(f"{self.logged_dir}/{name.lower()}-{fileEx.lower()}.log", "a") as f:
                    f.write(f"[{self.getDate()}] {storevalue}\n")
        print(f"Successfully saved data of {name}")

    def retrieve(self, name, fileEx):
        '''
        Retrieve the data of the .log file which was created by the log() function
        and then show the data to user. 
        '''
        with open(f"{self.logged_dir}/{name.lower()}-{fileEx}.log") as f:
            content = f.read()
            print(content)

    def addLogTypes(self):
        print("Adding Log Topics : ")
        print(f"{self.HEADER}Enter q to quit{self.ENDC}")
        topicLi = []
        keys = []
        while True:
            for key in self.savePoints.keys():
                keys.append(key)
            topic = input(" * Enter the Topic of log types : ")
            if topic == "q":
                break
            self.savePoints[str(int(max(keys))+1)] = topic 
            topicLi.append(topic)
        self.saveTopics()
        
    def saveTopics(self):
        with open(self.topics_json_filename, "w") as f:
            json.dump(self.savePoints, f, indent=3)
    
    def getSaveTopics(self):
        if os.path.exists(self.topics_json_filename):
            with open(self.topics_json_filename) as f:
                self.savePoints = json.load(f)
    
    def readNames(self):
        '''
        Read the JSON (if exists the json file) file and retrieve the names from
        from the JSON data and assign them. This function also give the value 
        of self.i to a unique number value
        '''
        if os.path.exists(self.filename):
            with open(self.filename) as f:
                jsonData = f.read()
                nameDict = json.loads(jsonData)
                self.clientDict = nameDict
                # print(self.clientDict)
                for value in self.clientDict.values():
                    self.values.append(value.lower())

                keys = []
                if len(self.clientDict) != 0:
                    for key in self.clientDict.keys():
                        keys.append(int(key))
                    i1 = max(keys)
                    i1 += 1
                else:
                    i1 = 1
                # print(i)
                self.i = i1
                print(self.i)

    def assignNames(self):
        '''
        Take the names from the user on a while loop to assign the JSON file 
        and use this for log and retrieve.
        '''
        print("---Assigning names---")
        print("Enter \"q\" to exit")
        while True:
            name = input("Enter the name : ")
            if name.lower() == "q":
                break

            if name.lower() not in self.values:
                self.clientDict[self.i] = name
                self.i += 1
                self.values.append(name.lower())
                print(f"Successfully assigned the name : {name}")
            else:
                print(
                    f"\"{name}\" is already present in the names data .Please choose a unique name.")
        # print(self.clientDict)
        self.saveNames()

    def saveNames(self):
        '''
        Save the names as a JSON file to use the data anytime.
        '''
        try:
            names = json.dumps(self.clientDict, indent=3)
            with open(self.filename, "w") as f:
                f.write(names)
        except Exception as e:
            print(e)

    def showNames(self):
        '''
        Show the name of user which is saved to clientDict
        '''
        for key, value in self.clientDict.items():
            print(f"{key}. {value}")

    def updateDict(self):
        '''
        To Update or Insert a name to a position
        '''
        self.showNames()
        updateDict = {}
        print("Update the name in srl no. ")
        print("Enter \"q\" to stop.")
        while True:
            keyinput = input("Enter the key / srl no. : ")
            if keyinput == "q":
                break
            valueinput = input("Enter the new name : ")
            if valueinput == "q":
                break
            if valueinput.lower() not in self.values:
                updateDict[int(keyinput)] = valueinput
                print("Successfully updated!")
                self.updateValuesOfDict()
                self.clientDict.update(updateDict)
                self.saveNames()
            else:
                print(
                    f"\"{valueinput}\" is already present in the names data. Please Enter a unique name.")

    def searchName(self):
        '''
        Give the user access to search by name to the data
        '''
        user = input("Enter the name to search : ")
        search_result = []
        for key in self.clientDict.keys():
            value = self.clientDict.get(key)
            if user.lower() == value.lower():
                print("\t\t\t***Search Results***")
                print(f"{key}. {value}")
                search_result.append(value)
        if len(search_result) == 0:
            print(f"There are no name like \"{user}\"")

    def sortNames(self):
        '''
        Sorted the names as alphabetical order.
        '''
        confirm = input("Do you really want to sort the names (y/n) : ")
        if confirm == "y":
            self.clientDict = {k: v for k, v in sorted(
                self.clientDict.items(), key=lambda item: item[1])}
            self.saveNames()
            print("Successfully sorted the names according to alphabetical order!")

    def removeName(self):
        '''
        Remove a name from the dictionary
        '''
        self.showNames()
        res = input("\n Enter the no. of name you want to delete : ")
        try:
            if res.isdigit():
                self.clientDict.pop(res)
                print(
                    f"The {self.clientDict.get(res)} of srl. {res} is successfully deleted.")
            else:
                self.clientDict.remove(res)
                print(f"{res} is successfully deleted.")
            self.saveNames()
        except ValueError:
            print("Invalid Value! Please Enter the srl no.")

    def deleteAllNames(self):
        '''
        Delete all names from the dictionary
        '''
        confirm = input("Do you really want to delete all names data (y/n) : ")
        if confirm == "y":
            print("All names data has been deleted!")
            self.clientDict = {}
            self.saveNames()
            print("Please insert some names to run the program.")
            self.assignNames()
        else:
            print("Thank you for your confirmation. Your data is saved!")

    @staticmethod
    def getDate():
        '''
        Retrun the current date and time
        '''
        return datetime.datetime.now()
    
    @staticmethod
    def ensureDir(dirname):
        if not os.path.exists(dirname):
            os.makedirs(dirname)

if __name__ == "__main__":
    # Change the directory to this folder
    path = os.path.join(os.getcwd(), "Health Management System")
    if os.getcwd() != path:
        os.chdir(path)

    clientDict = {}
    newHm = Healthmanager(clientDict)
    commands = ''' ************************ Health Management System ************************
                Commands: (Type the words or "srl"[such. 1 , 2, 3] for a command)
                srl|---- commands ---------| ---------------work-------------------
                1. | get all names        :| Get the saved names
                2. | assign Names         :| Assign names in the dictionary
                3. | update names         :| To update names or insert names data
                4. | log & retrieve       :| To log or retrieve the data of a person
                5. | search name          :| To search the key of any name
                6. | sort names           :| To sort the names
                7. | remove name          :| To remove any name
                8. | del all data         :| To delete all names
                9. | exit or quit or q    :| To exit the software
                10.| help or show commands:| To show the command interface again
        '''
    print(commands)
    '''Take the commands from the user'''
    while True:
        userinput = input(f"> {newHm.WARNING}Enter the command :{newHm.ENDC} ")
        if userinput.lower() == "get all names" or userinput == "1":
            newHm.showNames()
        elif userinput.lower() == "assign names" or userinput == "2":
            newHm.assignNames()
        elif userinput.lower() == "update names" or userinput == "3":
            newHm.updateDict()
        elif userinput.lower() == "log & retrive" or userinput == "4":
            newHm.initial()
        elif userinput.lower() == "search name" or userinput == "5":
            newHm.searchName()
        elif userinput.lower() == "sort names" or userinput == "6":
            newHm.sortNames()
        elif userinput.lower() == "remove name" or userinput == "7":
            newHm.removeName()
        elif userinput.lower() == "del data" or userinput == "8":
            newHm.deleteAllNames()
        elif userinput.lower() == "add log topics" or userinput == "9":
            newHm.addLogTypes()
        elif userinput.lower() == "exit" or userinput.lower() == "quit" or userinput.lower() == "q" or userinput == "10":
            print("Thanks for using these software!")
            input("Press Enter to exit ")
            exit()
        elif userinput.lower() == "help" or userinput.lower() == "show command" or userinput == "11":
            print(commands)
        else:
            print("***Invalid Keyword!***")
            print(commands)
