a = input("Введите ticket:")
s = a.replace('  ', '')
m = s.encode("utf-8").hex()
c = "000000740a2435353537333038632d643430312d343334312d613364652d336231386662333030376239121648616e647368616b6552656d6f7465536572766963651a0e70726f746f48616e647368616b6522241a220a20" + m
print(c)
