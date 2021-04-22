# Enuerate with enumerator() instead of range
  
month = ["jan", "frb", "march", "april"]

for m in month:
    print(m)
for i, m in enumerate(month):
    print(i, m)