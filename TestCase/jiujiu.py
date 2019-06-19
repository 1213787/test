
def jiujiu():
    for i in range(1,10):
        x=i +1
        for j in range(1,i+1):
            print('%s * %s = %2s' %(i,j,i*j),end="  ")

        print("  ")

if __name__ == '__main__':
    jiujiu()



