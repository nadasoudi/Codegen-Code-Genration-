import collections

def main():
    words = input("Enter the words separated by a comma: ").split(",")
    print(sorted(set(words)))

if __name__ == "__main__":
    main()

# OUTPUT:
# Enter the words separated by a comma: a,b,c,d,e,f,g,h,i,j,k,l,m,n,o