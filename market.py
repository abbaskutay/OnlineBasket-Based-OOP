import datetime

class InventoryProduct:
    def __init__(self,name,price,stock_amount):
        self.name = name
        self.price = price
        self.stock_amount = stock_amount




class BasketProduct():
   def __init__(self,name,price,stock_amount,basket_amount):
       pass




class Basket:
    def __init__(self):
        self.contents = {}
        self.basket_cont = []
        self.total_value = 0.0

    def display_contents(self,INV):
        self.basket_cont = []
        self.total_value = 0.0
        totallist = []
        count1 = 1
        print "Your basket contains:"
        # amount_selected=basket[user][adding_to_basket1] = amount
        for i in self.contents.keys():
            price = INV[i].price
            amount = self.contents[i]
            total_price = price * int(amount)
            self.total_value += total_price
            # totallist.append(total_price)
            self.basket_cont.append(i)
            print str(count1), i, "price=", price, "amount=", amount, "total=", total_price
            count1 += 1



    def show_basket_submenu(self,INV):
        print "Please choose an option:"
        print "1.Update amount"
        print "2.Remove an item"
        print "3.Check out"
        print "4.Go back to main menu"
        selection_sub = input("Your selection:")
        if selection_sub == 1:
            self.update_item(INV)
        elif selection_sub == 2:
            self.remove_item()
        elif selection_sub == 3:
            return 1

        elif selection_sub == 4:
            pass


    def add_item(self,u,user):
        adding_to_basket = int(raw_input("Please select which item you want to add to your basket (Enter 0 for main menu):"))
        adding_to_basket1 = str(u[adding_to_basket - 1])
        amount = int(raw_input("adding " + adding_to_basket1 + " Enter Amount:"))
        if amount == market().inventory[adding_to_basket1].stock_amount or amount <= market().inventory[adding_to_basket1].stock_amount:
            self.contents[adding_to_basket1] = int(amount)

            print"Going back to main menu..."

    def remove_item(self):
        c = 1
        for i in self.basket_cont:
            print c, i
            c += 1
        select_item = int(raw_input("Please select which item to remove:"))
        sel = self.basket_cont[select_item - 1]
        del self.contents[sel]

    def update_item(self,INV):
        c=1
        print self.basket_cont
        for i in self.basket_cont:
            print c, i
            c+=1

        select_item = int(raw_input("Please select which item to change its amount:"))
        new_amount = int(raw_input("Please enter new amount: "))
        while select_item > len(self.basket_cont):
            select_item = int(raw_input("Please select which item to change its amount:"))
            new_amount = int(raw_input("Please enter new amount: "))
        self.contents[self.basket_cont[int(select_item) - 1]] = int(new_amount)



class User :
    def __init__(self,username,password,basket):
        self.username = username
        self.password = password
        self.basket = basket


class market:
    def __init__(self):
        inventory = {'asparagus': [10, 5], 'broccoli': [15, 6], 'carrots': [18, 7],
                     'apples': [20, 5], 'banana': [10, 8], 'berries': [30, 3],
                     'eggs': [50, 2], 'mixed fruit juice': [0, 8], 'fish sticks': [25, 12],
                     'ice cream': [32, 6], 'apple juice': [40, 7], 'orange juice': [30, 8], 'grape juice': [10, 9], }
        self.inventory = {}
        for i in inventory.keys():
            self.inventory[i]= InventoryProduct(i,inventory[i][1],inventory[i][0])

        self.users = {"ahmet":User("ahmet","sehir123",Basket()), "meryem":User("meryem","4444",Basket())}
        self.u = []


    def show_market(self,user):
        print "Please choose one of the following services:"
        print "1. Search for a product"
        print "2. See Basket"
        print "3. Check Out"
        print "4. Logout"
        print "5. Exit"
        selection = int(raw_input("Your choice:"))
        while selection > 5:
            self.show_market(user)
        if selection == 1:
            self.search(user)
            self.show_market(user)
        elif selection == 2:
            self.users[user].basket.display_contents(self.inventory)
            s = self.users[user].basket.show_basket_submenu(self.inventory)
            if s == 1:
                self.check_out(user)
            else:
                self.show_market(user)
        elif selection == 3:
            self.check_out(user)
            self.show_market(user)
        elif selection == 4:
            self.login()
        elif selection == 5:
            exit()

    def search(self,user):
        count = 1
        choosing = raw_input("What are you searching for?").lower()
        while True:
            for selected in self.inventory.keys():
                if choosing in selected:
                    self.u.append(selected)
            # we wrote this code when we search items we will put them into the lsit to use it after.
            if len(self.u) == 0:
                choosing = raw_input(
                    "Your search did not match any items. Please try something else (Enter 0 for main menu):")
            # when we search sth has not in the inventory the program will ask again.
            else:
                break
        print 'found ' + str(len(self.u)) + " similar items"
        for selected in self.u:
            print str(count) + ".", selected, str(self.inventory[selected].price) + "" + "$"
            count += 1
        self.users[user].basket.add_item(self.u,user)

    def update_stock(self,user):
        for i in self.users[user].basket.contents.keys():
            self.inventory[i].stock_amount -= self.users[user].basket.contents[i]

    def check_out(self,user):
        self.print_reeipt(user)
        self.update_stock(user)
        self.users[user].basket.contents = {}

    def print_reeipt(self,user):
        print "Processing your receipt..."
        print "******* Sehir Online Market ********"
        print  "************************************ "
        print       "44 44 0 34"
        print      "sehir.edu.tr"
        print " ------------------------------------"
        totallist = []
        for i in self.users[user].basket.contents.keys():
            price = self.inventory[i].price
            amount = self.users[user].basket.contents[i]
            total_price = price * int(amount)
            totallist.append(total_price)
            print  i, "price=", price, "amount=", amount, "total=", total_price

        print "------------------------------------"
        print "TOTAL", self.users[user].basket.total_value, "$"
        # we created the totallist list to put the all prices and we used "sum" code to sum the all prices.
        print "------------------------------------"
        now = datetime.datetime.now()
        print  now.strftime("%Y-%m-%d %H:%M")
        print "Thank You for using our Market!"
    def login(self):
        print  ("Please log in by providing your user credentials:")
        while (1):
            self.username = raw_input("username")
            password = raw_input("password")
            if self.username in self.users.keys():
                if password == self.users[self.username].password:
                    print "Successfully logged in!"
                    self.show_market(self.username)
                    break
            # we wrote this code to get username and passsword from the dict that we created above.

            print 'Your user name and/or password is not correct. Please try again!'


m = market().login()
