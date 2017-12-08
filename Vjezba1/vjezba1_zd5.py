# Kristijan Kačan Vježba1 zadatak5 31.10.2017.

# definiranje variable sekunde
sekunde=184713

# izračun
dana= int(sekunde//(60*60*24))
ostatak_sekundi=(sekunde%(60*60*24))
sati=int(ostatak_sekundi//(60*60))
ostatak_sekundi=(ostatak_sekundi%(60*60))
minuta=int(ostatak_sekundi//60)
ostatak_sekundi=(ostatak_sekundi%60)

# ispis
print(sekunde,"sekundi je",dana,"dana", sati,"sata", minuta,"minuta","i", ostatak_sekundi,"sekunde")
