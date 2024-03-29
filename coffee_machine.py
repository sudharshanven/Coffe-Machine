class CoffeMachine:
    water_supply = 400
    milk_supply = 540
    bean_supply = 120
    cups = 9
    money = 550

    def fill_up(self):
        print("Write how many ml of water you want to add:")
        self.water_supply += int(input())
        print("Write how many ml of milk you want to add: ")
        self.milk_supply += int(input())
        print("Write how many grams of coffee beans you want to add:")
        self.bean_supply += int(input())
        print("Write how many disposable cups you want to add:")
        self.cups += int(input())

    def print_info(self):
        print(f"""The coffee machine has:
{self.water_supply} ml of water
{self.milk_supply} ml of milk
{self.bean_supply} g of coffee beans
{self.cups} disposable cups
${self.money} of money""")


def buy_coffee():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffe_type = input()

    if coffe_type == "1":
        if machine1.water_supply >= 250 and machine1.bean_supply >= 16 and machine1.cups >= 1:
            machine1.water_supply -= 250
            machine1.bean_supply -= 16
            machine1.cups -= 1
            machine1.money += 4
            print("I have enough resources, making you a coffee!")
        elif machine1.water_supply < 250:
            print("Sorry, not enough water!")
        elif machine1.bean_supply < 16:
            print("Sorry, not enough coffee beans!")
        elif machine1.cups < 1:
            print("Sorry, not enough disposable cups")

    elif coffe_type == "2":
        if machine1.water_supply >= 350 and machine1.milk_supply >= 75 and machine1.bean_supply >= 20 and machine1.cups >= 1:
            machine1.water_supply -= 350
            machine1.milk_supply -= 75
            machine1.bean_supply -= 20
            machine1.cups -= 1
            machine1.money += 7
            print("I have enough resources, making you a coffee!")
        elif machine1.water_supply < 350:
            print("Sorry, not enough water!")
        elif machine1.milk_supply < 75:
            print("Sorry, not enough milk!")
        elif machine1.bean_supply < 20:
            print("Sorry, not enough coffee beans!")
        elif machine1.cups >= 1:
            print("Sorry, not enough disposable cups")
    elif coffe_type == "3":
        if machine1.water_supply >= 200 and machine1.milk_supply >= 100 and machine1.bean_supply >= 12 and machine1.cups >= 1:
            machine1.water_supply -= 200
            machine1.milk_supply -= 100
            machine1.bean_supply -= 12
            machine1.cups -= 1
            machine1.money += 6
            print("I have enough resources, making you a coffee!")
        elif machine1.water_supply < 200:
            print("Sorry, not enough water!")
        elif machine1.milk_supply < 200:
            print("Sorry, not enough milk!")
        elif machine1.bean_supply < 12:
            print("Sorry, not enough coffee beans!")
        elif machine1.cups >= 1:
            print("Sorry, not enough disposable cups")

machine1 = CoffeMachine()
print()
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    chosen_option = input()
    if chosen_option == "buy":
        buy_coffee()
    elif chosen_option == "fill":
        machine1.fill_up()
    elif chosen_option == "take":
        print(f"I gave you ${machine1.money}")
        machine1.money = 0
        print("")
    elif chosen_option == "remaining":
        machine1.print_info()
    elif chosen_option == "exit":
        break
