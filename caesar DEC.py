  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
  " "
]
def checkcode (str1):
    for x in str1:
        if x not in alpha:
            raise Exception("Code is not valid")
            return False
    return True
    
def decrpytcode (str1,key):
    strarray = str1.split()
    final = []
    for x in str1:
        if x in alpha:
            xin = 0
            xin = (alpha.index(x) - key) 
            final.append(alpha[xin])
    finaltxt = "".join(final)
    print("decrypted code :"+finaltxt)
    
    
    
Boop = input("please enter code:")
entstr =  Boop.upper()
keytxt = input("Enter Key:")
key = int(keytxt)
if checkcode(entstr) is True:
    decrpytcode(entstr,key)
