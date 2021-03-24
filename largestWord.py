
def largestWord(s):
  
  
    s = sorted(s, key = len)

    print(s[-1])
  

if __name__ == "__main__":
  

    s = "be confident and be yourself"
  
   
    l = list(s.split(" "))
  
    largestWord(l)
