class Menu:
    def get_items(self):
        print("What would you like to have?? latte ${moneymachine.latte} | espresso ${moneymachine.espresso} | cappucino ${moneymachine.cappucino")
        
    def find_drink(self,order):
        if order in ['Latte','Espresso','Cappucino']:
            return order
        return False

class Moneymachine:
    def __init__(self):
        self.money=0
        self.latte=2
        self.espresso=3
        self.cappucino=5

    def report(self):
        print("The amount ",'$',self.money)

    def money_validate(self,cost,d_price):
        if cost>d_price:
            print(' Here is your change','$',abs(cost-d_price))
            return True
        elif cost==d_price:
            return True
        else:
            print('Sorry money is not enough "Money Refund"','$',cost)

            return False

    def make_payment(self,cost,drink):
        if drink=='latte':
            if self.money_validate(cost,self.latte):
                self.money+=self.latte
                return True
            return False
        elif drink=='espresso':
            if self.money_validate(cost,self.espresso):
                self.money+=self.espresso
                return True
            return False
        elif drink=='cappucino':
            if self.money_validate(cost,self.cappucino):
                self.money+=self.cappucino
                return True
            return False
        else:
            print('Invalid drink')
            return False

class Coffee_machine:
    def __init__(self,water,milk,coffee):
        self.water=water
        self.milk=milk
        self.coffee=coffee
        self.latte={'water':200,'milk':150,'coffee':25}
        self.espresso={'water':10,'milk':10,'coffee':200}
        self.cappucino={'water':50,'milk':200,'coffee':50}

    def report(self):
        print('water:',self.water)
        print('milk:',self.milk)
        print('coffee:',self.coffee)


    def is_resource_sufficient(self,drink):
        if self.coffee>=drink['coffee']:
            if self.milk>=drink['milk']:
                if self.water>=drink['water']:
                    return True
                else:
                    print('Sorry! Not enoigh water')
                    return False
            else:
                print('Sorry! Not enough milk')
                return False
        else:
            print('Sorry! Not enough coffee')
            return False

        
class Coffeemaker:
    def make_coffee(self,order,moneymachine,drink):
        if is_resource_sufficeitn(drink):
            cost=int(input('Enter the amount :'))
            if moneymachine.make_payment(cost,order):
                self.water-=drink['water']
                self.milk-=drink['milk']
                self.coffee-=drink['coffee']
                print("Here is your {orede} Emjoy!")
            else:
                return False       
        else:
            return False


menu = Menu()
moneymachine = Moneymachine()
c_m = Coffee_machine(1000,1000,2000)

machine = 'on'
while machine !='off':
    print('------------------COFFEE MACHINE-------------------')
    print('enter menu to display menu')
    print('enter report to display machine report')
    print('enter off to switch off the machine')
    action = input('enter your choice')
    if action =='off':
        machine = 'off'
    elif action == 'report':
        c_m.report()
        moneymachine.report()
    elif action == 'menu':
        menu.get_items()
        order = input(' : ')
        if order == 'latte':
            c_m.make_coffee(order,moneymachine,c_m.latte)
        elif order ==' espresso':
            c_m.make_coffee(order,moneymachine,c_m.espresso)
        elif order == 'cappucino':
            c_m.make_coffee(order,moneymachine,c_m.cappucion)
        else:
            print('Invalid drink')
    print('-----------------------THANK YOU----------------------')
            
        
