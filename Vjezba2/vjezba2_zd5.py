# Kristijan Kačan, 5.11.2017.
# Vježba2 zadatak 5

# unos variable sekunde
sekunde=int(input("Unesi vrijednost u sekundama: "))

# izračun
dana, ostatak_sekundi = divmod(sekunde, (60*60*24))
sati, ostatak_sekundi=divmod(ostatak_sekundi,(60*60))
minuta, ostatak_sekundi=divmod(ostatak_sekundi,60)

# ispis
print(sekunde,"sekundi je",dana,"dana", sati,"sata", minuta,"minuta","i", ostatak_sekundi,"sekunde")
