
#Exercise1
words = ['this' , 'is', 'a', 'sentence', '.']

def swap(words,a,b,c,d):
    words[a],words[b],words[c], words[d] = words[b], words[a], words[d], words[c]
    return words



swap(words,2,0,1,3)

print(f"Yoda: {words}")


#Exercise2


#Exercise3
bubble_sort = [10,23,45,70,11,15]
target = 70
#helper function
def swap(alist, a, b):
    alist[a], alist[b]= alist[b], alist[a]
    
def bubble_sort(alist):
    is_sorted= False
    while not is_sorted:
        is_sorted= True
        
        for idx in range(len(alist)-1):
            print([idx], [idx + 1])
            if alist[idx] > alist[idx + 1]:
                swap(alist,idx, idx+1)
                is_sorted = False
    return alist
    #For this exercise i tried to use the skeleton of the example we did in class...