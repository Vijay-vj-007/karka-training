consumer_name=input("Enter consumer name: ")
consumer_reading=[]
for i in range(5):
    reading=int(input(f"Enter the reading for month {i+1}: "))
    consumer_reading.append(reading)

consumer_data = {"consumer_name": consumer_name,
                "eb_reading": consumer_reading}


def calculate_electricity_bill(consumer_data):
    eb_reading=consumer_data["eb_reading"]

    output=[]
    Total_amount=0
    for i in range(len(eb_reading)-1):
        unit_consumed=eb_reading[i+1] - eb_reading[i]
        month=i+1
        bill=0
        if unit_consumed <100:
            bill=bill + 0
            Total_amount+=0
        elif unit_consumed >=100 and unit_consumed <200:
            bill=bill+(2 * unit_consumed)
            Total_amount+=(2* unit_consumed)
        elif unit_consumed >= 200 and unit_consumed <500:
            bill=bill+(5 * unit_consumed)
            Total_amount+=(5*unit_consumed)
        elif unit_consumed >= 500 and unit_consumed <=1000:
            bill=bill+(10 * unit_consumed)
            Total_amount+=(10*unit_consumed)
        elif unit_consumed > 1000:
            bill=bill+(14 * unit_consumed)
            Total_amount+=(14*unit_consumed)

        result={"Month":month,
                "Unit_consumed":unit_consumed,
                "Bill_amount":bill,}
        output.append(result)
        
    return output,Total_amount
print(calculate_electricity_bill(consumer_data))
    
# datas,total=calculate_electricity_bill(consumer_data)
# output_text=""
# for data in datas:

#     output_text=output_text+ f"Month:{data['Month']}\nUnit consumed:{data['Unit_consumed']}\nBill amount:{data['Bill_amount']}\n\n"
#     file_name="/home/vijay/txt/vijay.txt"
#     with open(file_name,"w") as file:
#         file.write(output_text)

# tot=""
# tot=tot+ f"Total amount:{str(total)}"
# file_name="/home/vijay/txt/vijay.txt"
# with open(file_name,"a") as file:
#     file.write(tot)






