def count_subsequence_AG(string):
    count=0
    for i in range(len(A)):
        if string[i]=='A':
            for j in range(i+1, len(string)):
                if string[j]=='G':
                    count+=1
    return count

string=input()
result=count_subsequence_AG(string)
print(result)
