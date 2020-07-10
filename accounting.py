

def customer_payments(file):

  """ Given file, produce report """

  payment_log = open(file)

  melon_cost = 1.00


  for line in payment_log:
    line = line.rstrip()
    words = line.split('|')

    customer_number = words[0]
    customer_name = words[1]
    customer_melons = words[2]
    customer_paid = float(words[3])

    customer_expected = melon_cost * float(customer_melons)

    print()
    print("Customer{}_name = {}".format(customer_number, customer_name))
    print("Customer{}_melons = {}".format(customer_number, customer_melons))
    print("Customer{}_paid = {}".format(customer_number, customer_paid))

    if customer_expected < customer_paid:
      print(f"Customer{customer_number} {customer_name} overpaid for their melons. Expected payment was ${customer_expected}. Customer paid ${customer_paid}.")
    elif customer_expected > customer_paid:
      print(f"Customer{customer_number} {customer_name} underpaid for their melons. Expected payment was ${customer_expected}. Customer paid ${customer_paid}.")

customer_payments("customer-orders.txt")


#     customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
