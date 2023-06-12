#format inside format
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter.format(1,{2},'',[]), formatter, formatter, formatter))
print(formatter.format("Johny johny,","Yes papa,","Eating sugar,","No papa"))
