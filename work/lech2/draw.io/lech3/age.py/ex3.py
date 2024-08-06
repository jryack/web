w = int(input("Enter te number of hours workd :"))
r = int(input("Enterr thehourly pay rate :" ))
tot = w*r
if w > 40 :
   ot = (w - 40)
   print("The gross pay is ", (ot*1.5*r) + (40*r))
else :
    print("The gross pay is ", tot) 