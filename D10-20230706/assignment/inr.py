prods=[100,200,300,400,500]
currency_code="INR"
a=[]
for prod in prods:
    str_prods=str(prod)
    concatenate_string=currency_code +" "+str_prods
    a.append(concatenate_string)
print(a)    



