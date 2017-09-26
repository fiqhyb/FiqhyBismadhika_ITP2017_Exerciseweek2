def main():
    print("Refrigerator Simulator\nmade by Fiqhy and Fariz\nRESPOND WITH 'yes' OR 'no' WITHOUT QUOTATION\nOR THE PROGRAM WILL END")
    print("#############################################")
    supply_list=[]
    def check():
        search=input("Do you want to check the refrigerator?")
        while search=="yes":
            if supply_list ==[]:
                print("The refrigerator is empty")
                check()
            spec_item=input("What item you're searching for?")
            if spec_item in supply_list:
                print(spec_item,"is available")
                check()
            else:
                print(spec_item,"is not available")
                check()
        if search=="no":
            insert()
    def insert():
        def new():
            new_supply=input("Enter the name of the object to put into the refrigerator:")
            supply_list.append(new_supply)
            print(new_supply)
            check()
        input_new=input("Do you want to input new item to  the refrigerator?")
        if input_new=="yes":
            new()
        elif input_new=="no":
            print("You closed the refrigerator...")
            exit()
    check()
main()