#Tools created to solve decryption assessment
# Author: Raul Rasciclal (rr355)

# Alphabet
# A  B  C  D  E  F  G  H  I  J  K    L   M  N  O   P   Q   R   S   T   U   V   W   X   Y   Z
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25


from collections import Counter
from collections import deque

# Get frequency of each character in string
def letterFreq(string):
    
    # Count of each char in string
    check = Counter(string)
    print("count = " + str(check))

    summ = len(string)
    freq = []
    check = check.most_common()
    
    # Calculate frequency
    for ele, val in check:
        freq.append((ele,round((val/summ),5)))


    # Sort alphabetically
    freq= sorted(freq)    

    print(freq)

    return freq





# Minus x from each letter and decrpyt the message
def decryptEx1(string, x):
    pt =""

    for letter in string:
        pt += chr((ord(letter) - (ord(x)-65))%26 + 65)

    print(pt)

#decryptEx1("ORROTMUTKULZNKINXUTOIGRRELKCZNGZNKVUYYKYYKJNKXKYLUXEUAXRGHUAXRGJZNOYSGJKGJOLLKXKTIKOTZNKEUATMSGTYKYZOSGZKULZNKVUYOZOUTEKYYOXPUNTZNGTQKKGTEZNOTMKRYKOIGTJULUXKKYOXPUNTZKRRKSGZNCUSKZNGZOYNUARJROQKLUXYAVVKXCKRRRGSHYLXEOLZNKEIGTMKZOZGTJOLZNKEIGTZHRGIQVUZGTJOLZNKEIGTZMKZZNGZCKRRINOZZKXROTMYCORRJUEKYYOXPUNTZNKHUEZUUQAVZNKHGYQKZGTJGYNKYKZUAZZNKTUZKYULGHXGYYHGTJCKXKNKGXJLXUSZNKJOXKIZOUTULZNKBORRGMKCNGZYZNGZYGOJJAXHKELOKRJTUZUTGIIUATZUOZOYZNKCUSKTYIRAHCGRQOTMYOXPUNTCNEEUAXJGZKXOYUTKUZNKSKSHKXYZUHKYAXKOJWAOZKLUXMUZOZOTSEZNUAMNZYULMXKGZKXZNOTMYCKRRBGSVUTZUSGXRUZZCORREKGTJUXJKXZNGZIGXXOGMKGTJSGEHKORRJXOBKXUATJGTJOTYVKIZZNKIRAHZNKRGJJKVGXZKJGTJJAXHKELOKRJRGECGOZOTMUTZNKMXGYYGTJJGOYOKYOTZNKKBKTOTMYATTUZGYUARVGYYKJZNGZCGELUXGRUTMCNORKGTJZNKLGOTZTUZKYULZNKHGTJCKXKZNKUTRENASGTYUATJYGAJOHRKCOZNOTZNKXOSULHRAKNORRYOOZNKBORRGMKULSGXRUZZRGEGSOJZNKTUXZ","K")


# Convert string to its ASCII decimal value
def convertStr(string):
    pt =[]

    for letter in string:
        pt.append(ord(letter))

    print(pt)

    return pt






# iterate over 2 lists and minus and mod each index values. - vigenere cipher
def decrpytVigenere(cipher, key):
    cipher = convertStr(cipher)
    key = convertStr(key)
    pt =""
    j=0

    for i in range(len(cipher)):
        pt+= chr(((cipher[i]-65) - (key[j]-65))%26+65)
        j+=1
        if j == len(key):
            j=0

    print(pt)


#decrpytVigenere("WTDZMDSOLHTRLHOGGWASOOGPOEYIYSVVOEWWPYOWCWASCRDCOPGRPUKTPLRFLCONLXDYZOCJZPYEJRNPWHZHYPDXPWPYQWMCOPRRSBLLXGEXPYQWMKLOSZGUSDKLBBOPNXRRMFVOWCOPIKYMYLWEJNKCYXLMIJKUMJKHRLAQSPNWMCOPGHJURYYZLABTXVMOASOFGBAPBFGJULLECHIPRLLMASOPGUSERHJJAEOUFJCTXJGWJPXWSAPPCSYBAMOHLJAEKFFNKEYWFNTZXDQCPNOVRJIWSVFVLYDWFNTTVOQCPWVZMARPNRLOVZNECRURKSCALYXLYUUPMHQBPEIWFNHMLHWQHOZHPRZSOGAALPNVZNPYQWPJUDSHLCVYOFMWATXXYUSJCHCBASOPGWPDDUYCPZXRDCOPDHKYVCKUWXBEVDQCPYQWFNTTXLQCYLDLMWVQDKCNAPBQYUASOLPFHWUKYEPYQECNUNSUADPEYXQCOPIZCALDDLJUUZDIYAMCYPRQLSYXQNHYNLLXIPILLPOTCGGALNDLMWZSORLUFSKGRXYPKFFCOPVDPPLDDRLNICSGENHNBRQBASOPYRUCSYCAHYNIMUSZGWFNYZKGDXYLPHUHHCNVUQLYCKCPVELDATLGOUWCOTXJPNTLSQCMHDCKCQHOVHDCPEDKCOPCOECRURCWGUSMEULRURCKCMPOXRRBALIGMFUDDDGAZQYUKXYPDKYWHXSQSCLMEWNAVNOHBNKEYKCAJSKPZNYHRLRQLCDKCUBRQDENOLNECNUEKNCWOPBHQQLDKWBXDYYQRQLPNJCXMERHZNKWYRIRURLOYWRWIDPX","HLKDYJ")



# decrypt Vigenere cipher
def findVigenereKey(string, englishPercent,keyLength):
    kLength = keyLength
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ|"

    for i in range(kLength):
        #get every 6th value
        iterateOver = string[::kLength]

        #get letter frequency
        freq = letterFreq(iterateOver)
       

        #give value to all letters in alpha  
        compList= []
        letters_dict = dict(freq)
        compList = [(letter, letters_dict.get(letter, 0)) for letter in alpha]

        total = 0.0
        prevTotal = 0.0
        counter = 0
        shiftNo = 0
        compList = deque(compList)

        # compare with English text freq and get the highest percentage
        for i in range(25):

            for j in range(len(englishPercent)):
                total+= (englishPercent[j][1]*compList[j][1])

            if total > prevTotal:
                shiftNo = counter
                prevTotal = total

            compList.rotate(-1)
            counter+=1
            total=0

        print(prevTotal)
        print(shiftNo)
        string = string[1:]




# decrypt using the transposition method
def decryptTransposition(cipher, column):
    # find out how many rows each column has/ how many characters belong in each column
    rows = int(len(cipher)/ column)
    
    tmpCipher = cipher
    table = []

    # add the characters into each column
    for i in range(column):
        x = tmpCipher[:rows]
        table.append([letter for letter in x])
        tmpCipher = tmpCipher[rows:]

    # print each character from all columns row wise.
    for row in range(rows):

        for colmn in range(column):

            print(table[colmn][row], end= "")
            #if colmn == 0:
            #    print(table[2][row], end= "")
            #if colmn == 1:
            #    print(table[5][row], end= "")
            #if colmn == 2:
            #    print(table[0][row], end= "")
            #if colmn == 3:
            #    print(table[4][row], end= "")
            #if colmn == 4:
            #    print(table[1][row], end= "")
            #if colmn == 5:    
            #    print(table[3][row], end= "")
        #print()



# find each character from the cipher in the mapping (dictionary) and print the character it is mapped to.
def decrpytEx7(cipher,mapping):
    pt= []
    for letter in cipher:
        try:
            pt.append(mapping[letter])
        except:
            pt.append(letter)

    print(''.join(str(x) for x in pt))



#decrpytEx7("VZONTOVPMKQNGO|VINGO|VOJHAVXAHAJQASV|OAVP|MFFQAVPTXJ|TOAPVMERKVOAXVZXNP|PVJKSV|OAVZAJXNKAPPVRBVOAXVAYAPVOAXVONGOVAK|OMPNJPIVOJHNKGVJV|XJKPBNGMXNKGVABBAT|VMERKV|OAVBJTAVZONTOVOJSVFAAKVOAXVMKSRNKGVPORZNKGVN|VJPVJV|ONKGVRBVNIIJTMQJ|AVFAJM|YVZN|OVJV|RMTOVRBVSNGKN|YVZONTOVZJPVJQIRP|VXAGJQV|OAVQN||QAVRKAPVWKAAQNKGVXRMKSV|OANXVPQAAEYVAYAPVFQNKWNKGVJKSVXASVJZJN|ASVOAXVEXAEJXJ|NRKPVBMQQVRBVJVPMPEAKSASVZRKSAXVZONTOV|OANXVEOYPNTJQVOAJHNKAPPVJ|V|OJ|VORMXVZRMQSVKR|VJQQRZV|RVFATRIAVJT|NHAV|OAVIRP|VNIEXAPPASVRBV|OAIVPJNSVFAVYRMVXAJQQYVGRNKGV|RVTOXNP|AKVONIV|APPV|OAVGNXQVIR|OAXVXAEQNASVNKVJVGXJHAVJBBNXIJ|NHAVZOJ|PVONPVKJIAVGRNKGV|RVFAVPOAVOJSVKR|V|ORMGO|VRBV|OJ|VFM|VJVKJIAVPMGGAP|ASVFYVJVEOXJPAVNKV|OAVFRRWVRBVGAKAPNPVTJIAVNK|RVOAXVOAJSVJPVPOAVEXRTAASASVZN|OV|OAVFJE|NPIJQVPAXHNTAVJKSVKRZVPOAVEXRKRMKTASVN|VPRXXRZVNVFJE|NCAV|OAAVNKV|OAVKJIAVRBV|OA",
#{'A': 'E', 
#'B': 'F',
#'E': 'P',
#'F': 'B',
#'G': 'G',
#'H': 'V',
#'I': 'M',
#'J': 'A',
#'K': 'N', 
#'M': 'U',
#'N': 'I',
#'O': 'H',
#'P': 'S',
#'Q': 'L',
#'R': 'O',
#'S': 'D',
#'T': 'C',
#'V': '|',
#'X': 'R',
#'Y': 'Y',
#'Z': 'W',
#'|': 'T'})
