from pprint import pprint,pp
monthly_gold_rate=[{"month":"january","gold_rate":3000,"Jewel":[{"name":"chain","making_cost":12},{"name":"ring","making_cost":14}]},
                   {"month":"february","gold_rate":3500,"Jewel":[{"name":"chain","making_cost":12},{"name":"ring","making_cost":14}]},
                   {"month":"march","gold_rate":2500,"Jewel":[{"name":"chain","making_cost":12},{"name":"ring","making_cost":14}]},
                   {"month":"april","gold_rate":2600,"Jewel":[{"name":"chain","making_cost":12},{"name":"ring","making_cost":14}]}]


monthly_cost={}
for gold in monthly_gold_rate:
    month=gold["month"]
    gold_rate=gold["gold_rate"]
    Jewels=gold["Jewel"]
    jewel_costs={}
    for Jewel in Jewels:
            jewel_name=Jewel["name"]
            percentage=gold["gold_rate"]* Jewel["making_cost"] /100
            total_cost=gold["gold_rate"]+percentage
            jewel_costs[jewel_name] = total_cost

    monthly_cost[month] = {
        "gold_rate": gold_rate,
        "jewels": jewel_costs
    }
pp(monthly_cost)

