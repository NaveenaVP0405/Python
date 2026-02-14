def get_details():
  name = input("Name: ")
  emp_id = input("ID: ")
  dept = input("Department: ")
  basic = float(input("Basic Salary: "))
  return name, emp_id, dept, basic
def calculate_salary(basic):
  hra = basic * 0.20
  da = basic * 0.10
  pf = basic * 0.12
  gross = basic + hra + da
  net = gross - pf
  return hra, da, pf, gross, net
def print_slip(name, emp_id, dept, basic, gross, net):
  print("\n--- Salary Slip ---")
  print("Name:", name)
  print("ID:", emp_id)
  print("Department:", dept)
  print("Basic:", basic)
  print("Gross:", gross)
  print("Net:", net)
name, emp_id, dept, basic = get_details()
hra, da, pf, gross, net = calculate_salary(basic)
print_slip(name, emp_id, dept, basic, gross, net)
