if __name__=="__main__":
    print("welcome to the tip calculator!")
    bill = float(input("What was the total bill? €"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    bill_with_tip = tip / 100 * bill + bill # or (1) bill * (1 + tip / 100)
    # or (2) tip_as_percent = tip / 100
    # total_tip_amount = bill * tip_as_percent
    # total_bill = bill * total_tip_amount
    print("{:.2f}".format(bill_with_tip)) 
    bill_per_person = bill_with_tip / people
    final_amount = round(bill_per_person, 2)
    print(f"Each person should pay €{final_amount}")

