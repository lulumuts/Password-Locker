class User:
    """
    Class that generate new accounts using a login and password.
    """

    account_list = [] #Empty account list

    def __init__(self):

        self.username = []
        self.password = []
        self.ranpw = []

        logs = []
        pws = []
        try:
            f =open("login.csv", "r+")
            for line in f:
                line = line.strip("\n")
                line = line.strip(" ")
                x=line.split(",")
                logs.append(x[0])
                pws.append(x[1])

            f.close()

        except:
            f=open("login.csv", "w")

        if len(logs) >0:
            for i in range(len(logs)):
                self.save_account(logs[i], pws[i])

        try:
            fx =open("randpasswords.csv", "r+")
            for line in fx:
                line = line.strip("\n")
                line = line.strip(" ")
                line = line.strip()
                x=line.split(",")
                for j in x:
                    self.ranpw.append(j)

            fx.close()

        except:
            fx=open("randpasswords.csv", "w+")
            fx.close()




        #self.username = usernom
        #self.password = passnom


    def save_account(self, un, ps, arg=0):
        '''
        save_account method saves the account objects in account_list
        '''
        self.username.append(un)
        self.password.append(ps)


        if arg == 1:
            ticks=open("login.csv","w+")
            for new in range(len(self.username)):
                l = "%s,%s\n" %(self.username[new], self.password[new])
                #self.username[new],",",self.password[new],"\n"
                ticks.write(l)
            ticks.close()




    def check_exist(self, un):
        for i in range(len(self.username)):
            if self.username[i] == un:
                ret = self.password[i]
                break
            else:
                ret = ("nonefound000")
        return(ret)

    def randompw(self,un):
        import random
        import sys
        for i in range(len(self.username)):
            if self.username[i] == un:
                mynum = []
                inp = int(input("Enter your pw length: "))
                allstr = 'ABCDEFGHJKLMNOPQRSTUVWXYZ1234567890'
                for i in range(inp):
                    #print("i", i)
                    thisnum = int(random.randint(0,len(allstr)))
                    #print("thisnum", thisnum)
                    mynum.append(thisnum)
                    #print("mynum",mynum)

                #allstr[mynum]
                pasw = ''
                for x in mynum:
                    pasw = str(pasw) + str(allstr[x])
        _ = "%s---%s" %(un,pasw)
        self.ranpw.append(_)
        tacs=open("randpasswords.csv","a+")
        tacs.write("%s," %_)
        tacs.close()
        return(pasw)

    def returnpw(self,un):
        #_ = "%s---" %(un)
        print("Stored passwords for %s" %un)
        for i in self.ranpw:
            i = str(i)
            #print(i, "herenow")
            x = i.split("---")
            #print('nowwww',x)
            if x[0].strip() == un:
                print(x[1])
            else:
                pass





        #User.account_list.append(self)

    def get_details(self):
        print(self.username)
        print(self.password)

    def find_account_by_login(self):
        '''
        Method that takes in the password in the form of a number and returns account
        details

        Args:
         login: name to search before
        Returns:
         Account of person that matches the name.
        '''
        for user in cls.account_list:
            if contact.login == login:
                return login
