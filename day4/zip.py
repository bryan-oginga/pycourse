
# list r practise

# list litera

salaries = [1000, 2000, 3000, 4000, 5000]
tax_rates = 16.0

def salary_after_tax(salaries, tax_rate):
    # return a list of salaries after tax
    return [salary - (salary * tax_rate / 100) for salary in salaries]

after_tax_salaries = salary_after_tax(salaries, tax_rates)
print(after_tax_salaries)

print(f"{'BEFORE TAX ':<8} {'AFTER TAX ':<8}:")
print("--"*15)

for before, after in zip(salaries, after_tax_salaries):
    print(f"{before:<8} {after:>8}")