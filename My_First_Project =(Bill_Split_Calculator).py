print("Bill Split Calculator")
bill_amount = float(input())
tip_percentage = float(input())
Split = int(input())
tip_amount = (tip_percentage / 100) * bill_amount
total = (bill_amount + tip_amount)
print (f"Total (including tip): R{total}")
split_total = (total / Split)
print(f"Each person pays: R{split_total}")
