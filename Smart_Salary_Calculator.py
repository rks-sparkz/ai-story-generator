# 1. Taking Inputs
name = input("Name: ")
age = int(input("Age: "))                 
salary = float(input("Salary: "))         
experience = int(input("Experience: "))   

# 2. Calculating Yearly Salary
yearly_salary = salary * 12

# 3. Calculating Bonus 
# Experience >= 5 → 20% bonus | Otherwise → 10% bonus
if experience >= 5:
    bonus = salary * 0.20
else:
    bonus = salary * 0.10

# 4. Calculating Tax
# Salary > 50000 → 15% tax | Otherwise → 5% tax
if salary > 50000:
    tax = salary * 0.15
else:
    tax = salary * 0.05

# 5. Checking Senior Benefit
# Age >= 40 → Eligible | Otherwise → Not Eligible
if age >= 40:
    senior_benefit = "Eligible"
else:
    senior_benefit = "Not Eligible"

# Salary > 80000 → "High Earner" | Otherwise → "Regular Earner"
status = "High Earner" if salary > 80000 else "Regular Earner"

# 7. Displaying the Sample Output
print("\n--- Sample Output ---")
print(f"Yearly Salary: {int(yearly_salary)}")
print(f"Tax: {int(tax)}")
print(f"Bonus: {int(bonus)}")
print(f"Senior Benefit: {senior_benefit}")
print(f"Status: {status}")