##DataStructures Sorting
##
##Merge Sort:
##
#import pdb

##b: set a breakpoint
##c: continue debugging until you hit a breakpoint
##s: step through the code
##n: to go to next line of code
##l: list source code for the current file (default: 11 lines including the line being executed)
##u: navigate up a stack frame
##d: navigate down a stack frame
##p: to print the value of an expression in the current context

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        #
        # This will convert 2 finger algorithm and individual arrays will sorted
        #
        while i < len(left) and j < len(right):
            if i < len(left) and left[i] < right[j]:
                arr[k] = left[i]
                i = i+1
            else:
                arr[k] = right[j]
                j = j+1
            k=k+1

    
        #
        # This is final individual sorted arrays will merge here 2 whiles 
        #
        while i < len(left):
            arr[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):
            arr[k] = right[j]
            j = j+1
            k = k+1

        print("Arr ",arr)

        
if __name__ == "__main__":
    print("### Merge Sort Started")
    arr = [1,6,4,5,2,3]
    #mergeSort(arr,0,len(arr)-1)
    mergeSort(arr)
