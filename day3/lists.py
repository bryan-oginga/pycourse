
color = ['black', 'white', 'red', 'blue', 'green']

variable_list = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30},(1, 2, 3),[12.3,156,11.6]]

# List comprehension

tests = [number ** 3 for number in range(1, 11)]

# 1. Populating List Items
names = ['John', 'Jane', 'Doe', 'Alice', 'Bob']

candidates = []

for name in names:
    candidates.append(name)
    if len(candidates) == len(names):
        # print(candidates)
        pass


# 2. Popilating lists using map function (Taxrate example)

tax_rates = [0.1, 0.2, 0.3, 0.4, 0.5]

salaries = [1000, 2000, 3000, 4000, 5000]
tax_rate = 16.0

def get_salary_after_tax(salary):
    return salary - (tax_rate/100)

salary_after_tax = list(map(get_salary_after_tax, salaries))

#Tabular printing
print(f"{'Before tax ':<15} {'After tax ':>15}")
print("_"*30)
for before, after in zip(salaries, salary_after_tax):
    # print(f"{before:<15} {after:>15}")
    pass
    
# Acessing lists

employee_list = [
    ('John Doe',20, 'Software Engineer'),
    ('Jane Smith', 25, 'Product Manager'),
    ('Bob Johnson', 30, 'Data Scientist')
]
print(employee_list[1][0])