# Kirjoita ratkaisu tähän
vuosi = int(input("Anna vuosi:"))

if (vuosi % 4) == 0:
   if (vuosi % 100) == 0:
       if (vuosi % 400) == 0:
           print("{0} on karkausvuosi".format(vuosi))
       else:
           print("{0} ei ole karkausvuosi".format(vuosi))
   else:
       print("{0} on karkausvuosi".format(vuosi))
else:
   print("{0} ei ole karkausvuosi".format(vuosi))
