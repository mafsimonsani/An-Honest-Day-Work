# WC '18 Contest 3 J1 - An Honest Day's Work
REMAINING_PAINT_PRICE = 1

leftover_paint = int(input())
bottlecap_paint = int(input())
sold_price = int(input())

# Calculate the amount of money which James will make.

total_badges = leftover_paint // bottlecap_paint
extra_paint_left_over = leftover_paint - (bottlecap_paint * total_badges)

total_money = (sold_price * total_badges) + (REMAINING_PAINT_PRICE * extra_paint_left_over) 

print(total_money)