
def generate(numRows: int) -> list[list[int]]:
    out = []
    arr = [1]
    out.append(arr)
    if numRows > 1:
        for k in range(1, numRows):
            temp = []
            print('new row', k)
            for j in range(-1, k):
                print(j, k)
                if(j>=0 and j<k-1):
                    print('if')
                    print(arr)
                    s = arr[j] + arr[j+1]
                else:
                    print('else')
                    print(arr)
                    s = arr[j]
                temp.append(s)
            out.append(temp)
            print('out', out)
            arr = temp
    return out

generate(5)