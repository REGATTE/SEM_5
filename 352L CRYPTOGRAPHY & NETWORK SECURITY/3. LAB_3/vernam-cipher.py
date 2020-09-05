
plain = list(map(int,input("Enter plaintext: ").split()))
key = list(map(int,input("Enter key: ").split()))
def encrypt():
  if(len(plain)!=len(key)):
    print("Invalid Input")
  else:
    result = []
    for i in range(len(plain)):
      result.append(plain[i] ^ key[i])
  return result

encrypt()
