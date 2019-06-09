#! temprature c to f conversion 

# Function Conversion Temp(C) to Temp(F)
def ConversionCToF(temp):
    FormulaConst1 = 1.8
    flormulaConst2 = 32
    Farenhiet = temp * FormulaConst1 + flormulaConst2
    return Farenhiet

print("----------Start Program--------- ")
print("----------Conversion Calcius to Farenhiet------------")    

# get user input 
print("Enter temperature ( Calsius) ")
tempC = int(input())
# Function call for conversion  Temp(C) to Temp(F)
TempF = ConversionCToF(tempC)
print(tempC , "' Calsius to Farenhiet is  " , TempF )

