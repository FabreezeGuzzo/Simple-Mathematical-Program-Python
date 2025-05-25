bath_amount = int(input("How much water does the tub hold?"))
water_already_in_tub = int(input("How many gallons are already in the tub?"))
needed_water = bath_amount - water_already_in_tub
gallons_per_min = float(input("How many gallons per min?"))
time_need_to_fill_tub = needed_water / gallons_per_min
print("Amount of time it would take to fill up the tub", time_need_to_fill_tub)
