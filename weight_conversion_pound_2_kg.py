# Weight Conversion Calculator

## Input weight in pounds
pounds = float(input("Enter weight in pounds: "))

## Conversion factor from pounds to kilograms
conversion_factor = 0.453592

## Convert pounds to kilograms
kilograms = pounds * conversion_factor

## Display the result
print(f"{pounds} pounds is equal to {kilograms:.2f} kilograms.")
