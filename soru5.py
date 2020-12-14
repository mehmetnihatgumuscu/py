ifade = input("İfadeyi giriniz: \n")
ifadeler = ifade.split("\\n")[:-1] # birden fazla ifade girilmişse \n ile bölüyoruz. 

# örnek ifade: receive-23-1-0\n

for ifade in ifadeler: 
    parts = ifade.split('-')
    if parts[0] not in ['receive', 'send']: 
        print ("Error: send ya da receive icermiyor ")
        print ("--------")
        continue
    if int(parts[1]) not in range(0, 256): 
        print ("Error: birinci bolum hatali ")
        print ("--------")
        continue
    if int(parts[2]) not in [1,2,3,4]: 
        print ("Error: ikinci bolum hatali ")
        print ("--------")
        continue
    if int(parts[3]) not in [0,1]: 
        print ("Error: ucuncu bolum hatali ")
        print ("--------")
        continue
    if parts[0] == 'send' and int(parts[4]) not in [0,1]: 
        print ("Error: dorduncu bolum hatali ")
        print ("--------")
        continue
    
    if parts[0] == 'receive': 
        print ("Kod Tipi : receive - Gelen")
    elif parts[0] == 'send': 
        print ("Kod Tipi : send - Giden")
    
    if int(parts[1]) >= 0 and int(parts[1]) <= 50: 
        print ("Sinyal Gucu :", parts[1], "- Cok Zayif Sinyal")
    elif int(parts[1]) > 50 and int(parts[1]) <= 100: 
        print ("Sinyal Gucu :", parts[1], "- Zayif Sinyal")
    elif int(parts[1]) > 100 and int(parts[1]) <= 150: 
        print ("Sinyal Gucu :", parts[1], "- Orta Sinyal")
    elif int(parts[1]) > 150 and int(parts[1]) <= 200: 
        print ("Sinyal Gucu :", parts[1], "- Guclu Sinyal")
    elif int(parts[1]) > 200 and int(parts[1]) <= 255: 
        print ("Sinyal Gucu :", parts[1], "- Cok Guclu Sinyal")
        
    if int(parts[2]) == 1: 
        print ("Cihaz :", parts[2], "- Televizyon")
    elif int(parts[2]) == 2: 
        print ("Cihaz :", parts[2], "- Camasir Makinesi")
    elif int(parts[2]) == 3: 
        print ("Cihaz :", parts[2], "- Buzdolabi")
    elif int(parts[2]) == 4: 
        print ("Cihaz :", parts[2], "- Firin")
        
    if int(parts[3]) == 0: 
        print ("Durumu :", parts[3], "- Off")
    elif int(parts[3]) == 1: 
        print ("Durumu :", parts[3], "- On")
    
    if parts[0] == 'send': 
        if int(parts[4]) == 0: 
            print ("Cevap :", parts[4], "- Istenmiyor")
        elif int(parts[4]) == 1: 
            print ("Cevap :", parts[4], "- Isteniyor")
        
        
    print ("--------")