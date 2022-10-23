print("what do you want to smoke")
print(" 1 for Stay awake")
options = int(input(" 2 for deep sleep \n - "))
if(options != 1 or 2 ):
    options = int(input("Choose from the given options from \n 1 or 2 : "))
    if(options == 2):
        print("Smoke Indica") 
    elif(options == 1):
        print("Smoke Sativa")
    
    if(options == 1):
        print(" * Acapulco Gold\n * Bedrocan \n * Blue Dream")
    elif(options == 2):
        print(" * Charlotte's Web\n * Skunk Sour\n * Diesel.")