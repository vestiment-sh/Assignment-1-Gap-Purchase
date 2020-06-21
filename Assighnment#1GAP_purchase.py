### Steven Smith (23658589)
## 6/12/2020
# Assignment 1 GAP Purchase

# Declaration of variables
jeans = 0.0
t_shirt = 0.0
purchase_amount = 0.0
total_sale = 0.0
total_state_sales_tax = 0.0
total_county_sales_tax = 0.0
total_sales_tax = 0.0
state_sales_tax = 0.04
county_sales_tax = 0.04875

#Insert values
jeans = float(input('Enter the charge for the jeans: '))
t_shirt = float(input('Enter the charge for the t-shirt: '))

total_state_sales_tax = (jeans*state_sales_tax) + (t_shirt*state_sales_tax)

total_county_sales_tax = (jeans*county_sales_tax)+(t_shirt*county_sales_tax)

total_sales_tax = total_state_sales_tax + total_county_sales_tax

purchase_amount = jeans + t_shirt

total_sale = purchase_amount + total_sales_tax

print('Amount of Purchase: $', format(purchase_amount, ' .2f'))
print('State Sales Tax: $', format(total_state_sales_tax, ' .2f'))
print('County Sales Tax: $', format(total_county_sales_tax, ' .2f'))
print('Total Sales Tax: $', format(total_sales_tax, ' .2f'))
print('Total Sale: $', format(total_sale, ' .2f'))