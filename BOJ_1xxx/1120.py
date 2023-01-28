A,B=input().split()
def sub(A:str, B:str):
    return sum([A[i]!=B[i] for i in range(len(A))])

def result(A:str, B:str):
    min=50
    if len(A)==len(B):
        return sub(A, B)
    else:
        for i in range(len(B)-len(A)+1):
            new_B = B[i:i+len(A)]
            res=sub(A, new_B)
            if res<min:
                min=res
        return min
print(result(A,B))