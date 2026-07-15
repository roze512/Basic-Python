distance = float(input("\nDistance (km) enter karein: "))
if distance < 5:
    fare = 100
elif distance <= 15:
    fare = 250
else:
    fare = 500
print("Aapka fare hai:", fare, "PKR")
