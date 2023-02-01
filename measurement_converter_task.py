#cm to m /100
#m to feet *3.28084

# Making the cm to m function
def cm_converter(cm:float) -> float:
    return cm / 100

# Making the m to feet function
def m_converter(m:float) -> float:
    return m * 3.28084

# Asking the user which converter they would like to use and the number to be converted
calculator = int(input("Please choose your preferred calculator by typing the associated key, : 1 = cm to m, 2 = m to feet :"))
target_number = float(input("Please type in the number you would like to convert :"))

# Running the calculators
if calculator == 1:
    print(f" Your {target_number} cm has been converted into {cm_converter(target_number)} m")
elif calculator == 2:
    print(f" Your {target_number} meters have been converted into {m_converter(target_number)} feet")
