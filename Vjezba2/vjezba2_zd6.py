# Kristijan Kačan, 5.11.2017.
# Vježba2 zadatak 6

# unos variabli a, b
a,b=float(input("Unesi prvi decimalni broj: ")), float(input("Unesi drugi decimalni broj: "))

# izračun i ispis
print('Količnik brojeva {} i {} na 5 decimala je {:.5f}'.format(a, b, a/b))
print('Količnik brojeva {} i {} na 2 decimale je {:.2f}'.format(a, b, a/b))
print('Količnik brojeva {} i {} zaokružen na cijeli broj je {:.0f}'.format(a, b, a/b))


