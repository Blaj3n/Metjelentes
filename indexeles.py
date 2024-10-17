ido = "0123"

print(ido[0:2])     # a 0. karaktertől indul a végkarakter -1 -ig. Lásd: 0 ---> (2-1)
print(ido[:2])      # a 0. karaktertől indul a végkarakter -1 -ig. Lásd: 0 ---> (2-1)
print(ido[2:4])      # a 2. karaktertől indul a végkarakter -1 -ig. Lásd: 2 ---> (4-1)
print(ido[2:])      # a 2. karaktertől indul a végkarakter -1 -ig. Lásd: 2 ---> (4-1)

datum = "02271234"

# hónap
print(f"Hónap: {datum[:2]}")
# nap
print(f"Nap: {datum[2:4]}")
# perc
print(f"Perc: {datum[6:]}")
