profit = {
    "cost_price" :12,
    "sell_price" :34,
    "inventory" :30
}
total_CP= profit["cost_price"] * profit["inventory"]
total_SP= profit["sell_price"] * profit["inventory"]
total_profit = total_SP - total_CP
print(total_profit)
total_profit = total_profit * 159
print("total profit in rupees: ",total_profit)
if total_profit >= 200000:
    tax = (0.2 *total_profit) - total_profit
    print("He has to pay 20% tax from his profit ! ")