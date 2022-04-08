
vraag_leeftijd = input("wat is u leeftijd : ? ")
vraag_gebroortejaar = input("wat is u geboorte jaar : ? ")

try:
    vraag_leeftijd = int(vraag_leeftijd)
    vraag_gebroortejaar = int(vraag_gebroortejaar)


except:
    print("u kunt alleen getallen invoeren !! ")

    
else:
    print("u leeftijd = " + str(vraag_leeftijd))
    print("u geboorte jaar = " + str(vraag_gebroortejaar))





