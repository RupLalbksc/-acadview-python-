#12a
a=3
if a<4:
    try:
        b=a/(a-3)
        print(b)
        
    except ZeroDivisionError:
        print("Exception ======",ZeroDivisionError)

#12b

try: 
    a = [1,2,3,4,5] 
    print(a[5]) 
except LookupError: 
    print("Index out of bound error.")
else: 
    print("Success")