
players = ['Amad Diallo', 'Anthony Elanga', 'Shola Shoretire', 'Hannibal Mejbri', 'Facundo Pellistri']

youth_academy = players.copy()

if (id(players) == id(youth_academy)):
    # print("Both lists refer to the same memory location")
    pass
else:
    # print("Both lists do not refer to the same memory location")
    pass
    
print(youth_academy[0:2])

