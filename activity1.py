def total_calc(total_amount, tip_perc):
    total = total_amount*(1 + 0.01 * tip_perc)
    total = round(total,2)
    print(f"please pay ${total}")
total_calc(150,20)