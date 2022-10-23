from statistics import correlation


print(" Namaskar deviyoo aur sajanoo \n Kaun benaga crorepati me swagat hai aapka.. \n dil tham ke baitiye kyuki shuru karen jaa rahe aaj ka show \n")
money = 0
x = 1

while(x <= 1):

    first_question =  int(input("Aaj ka pehla sawal hai, Pakistan ke Prime minister kaun hai? \n \n 1) Nawaz Sharif\n 2) Shehbaz Sharif \n 3) Imran Khan \n 4) Inzamam ul-haq \n Ans : "))

    if(first_question == 2):

        money = money + 1 
        print(" Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ", money, "Rupee.")
        x = x + 1
    
    else:
        print(" Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break
    
    second_question = int(input("\n Pesh hai dusra sawal, Pakistan ke Capital ka naam kya hai? \n \n 1)Lahore \n 2)Islamabad \n 3)Karachi \n 4)Faisalabad \n Ans : "))
    
    if(second_question == 3):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

    third_question = int(input("\n Pesh hai teesra sawal, In which Italian city can you find the Colosseum? \n \n 1)Venice \n 2)Rome \n 3)Naples \n 4)Milan \n Ans : "))
    
    if(third_question == 2):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

        
    fourth_question = int(input("\n Pesh hai choutha sawal, What is the largest canyon in the world? \n \n 1)Verdon Gorge, France \n 2)King’s Canyon, Australia \n 3)Grand Canyon, USA \n 4)Fjaðrárgljúfur Canyon, Iceland \n Ans : "))
    
    if(fourth_question == 3):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

    fifth_question = int(input("\n Pesh hai panchva sawal, In which museum can you find Leonardo Da Vinci’s Mona Lisa? \n \n 1)Le Louvre \n 2)Uffizi Museum \n 3)British Museum \n 4)Metropolitan Museum of Art \n Ans : "))
    
    if(fifth_question == 1):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

    sixth_question = int(input("\n Pesh hai chatta sawal, In the Big Bang Theory, what is the name of Sheldon and Leonard’s neighbour? \n \n 1)Raj \n 2)Penny \n 3)Howard \n 4)Stuart \n Ans : "))
    
    if(sixth_question == 2):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

    seventh_question = int(input("\n Pesh hai saathva sawal, When did Hitler invade Poland? \n \n 1)1st September 1939 \n 2)11th November 1939 \n 3)8th May 1940 \n 4)1st December 1940 \n Ans : "))
    
    if(seventh_question == 1):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

    eighth_question = int(input("\n Pesh hai aanthva sawal, What is the largest continent in size? \n \n 1)Asia \n 2)Africa \n 3)Europe \n 4)North America \n Ans : "))
    
    if(eighth_question == 1):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

    ninth_question = int(input("\n Pesh hai nauva sawal, In which city is the Juventus Football Club based?? \n \n 1)Manchester \n 2)Barcelona \n 3)Turin \n 4)Marseille \n Ans : "))
    
    if(ninth_question == 3):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

    tenth_question = int(input("\n Pesh hai dasva sawal, Which country does not share a border with Romania? \n \n 1)Ukraine \n 2)Bulgaria \n 3)Hungary \n 4)Poland \n Ans : "))
    
    if(tenth_question == 4):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

    eleventh_question = int(input("\n Pesh hai gyaravah sawal, When was the first Harry Potter book published? \n \n 1)1999 \n 2)1997 \n 3)2001 \n 4)2003 \n Ans : "))
    
    if(eleventh_question == 2):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

    twelfth_question = int(input("\n Pesh hai baaraha sawal, What is the capital of Iraq? \n \n 1)Tehran \n 2)Islamabad \n 3)Baghdad \n 4)Amman \n Ans : "))
    
    if(twelfth_question == 3):
        money = money + 1
        print("Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore ",money , "Rupee.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break

    thirteenth_question = int(input("\n Pesh hai akhri aur sabse ahem sawal, Which country won the first Football World Cup in 1930? \n \n 1)Brazil \n 2)Portugal \n 3)Italy \n 4)Uruguay \n Ans : "))
    
    if(thirteenth_question == 4):
        money = money + 1
        print(" Dhudhudhun \n Dhudhudhun \n Dhudhudhun \n Bilkul sahi jawab \n Aap jeet chuke hai, poore Ek Crore Rupaye.")

    else:
        print("Dhudhudhun \n Dhudhudhun\n Dhudhudhun \n Afsos Galat Jawab \n Kaun banega crorepati me aapka safar yahi khatam hota hai")
        break



