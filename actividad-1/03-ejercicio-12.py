hours_per_week = 48
price_per_hour = 5_000
tax_percent = 0.125

gross = hours_per_week*price_per_hour
tax = gross*tax_percent

print('SALARIO DE UN EMPLEADO')
print(f'Salario bruto: ${gross:,.0f}')
print(f'Rte. Fte.: ${(tax):,.0f}')
print(f'Salario neto: ${(gross-tax):,.0f}')