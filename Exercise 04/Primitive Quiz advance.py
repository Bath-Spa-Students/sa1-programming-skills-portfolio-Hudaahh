#Exercise no 04, Primitive Quiz advance
#listing 10 Europe Country And Capital
Country_Cap = "Latvia,Riga,Lithuania,Vilnius,Luxbourg,Luxembourg,Malta,Valletta,Moldova,Chișinău,Monaco,Monaco,Montenegro,Podgorica,Netherlands,Amsterdam,Norway,Oslo,France,Paris"
Id = Country_Cap.split(',')
#useing for i in range
for i in range (0,len(Id), 2):
    Country = Id[i]
#Assigning Country and Capital Together
    Capital = Id[i+1]
#Asking the user to give the country's Capital
    Ans = input(f"What is the capital of {Country} ? ").lower()
#Check wether the given output is correct or incorrect 
    if Ans==Capital.lower():
        print("The Answer is correct ")
    else:
        print("The Answer is incorrect ")


