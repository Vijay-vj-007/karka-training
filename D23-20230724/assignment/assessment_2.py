monthly_gold_rate=[{"month":"january","gold_rate":3000},
                   {"month":"february","gold_rate":3500},
                   {"month":"march","gold_rate":2500},
                   {"month":"april","gold_rate":2600}]

max=0
max_month=""
min=monthly_gold_rate[0]["gold_rate"]
min_month=""

for gold in monthly_gold_rate:
    if gold["gold_rate"]>max:
        max=gold["gold_rate"]
        max_month=gold["month"]

    if gold["gold_rate"]<min:
        min=gold["gold_rate"]
        min_month=gold["month"]

print(f"Month: {max_month}\tGold rate: {max}")
print(f"Month: {min_month}\tGold rate: {min}")

