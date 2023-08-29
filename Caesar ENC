alpha = [
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
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
]
Text = input("Enter Text ")
final = []
key = input("Enter Key ")
key = int(key)

for x in Text.upper():
    xin=0
    
    if x == " ":
        final.append(" ")
    if x in alpha:
        xin = alpha.index(x) + key
        if xin > 25:
            xin = xin - 25
        final.append(alpha[xin])
    else:
        raise Exception("please use plain text")
        
final = "".join(final)         
print ("Encrpted code:"+final)
