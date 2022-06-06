for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [int(i) for i in input().split()]
    sorted_arr = [i for i in range(1, n + 1)]
    ans_flag = 0
    ans = []
    i = 0 #starting position
    while(1):
        if ((arr[n - 1] == (n)) and (i == n)):
            ans_flag = 1
            break
        if arr[i] == sorted_arr[i]:
            i += 1
            continue
        #therefore our first index will be the ith position
        #rest two indexes will obviously will lie after ith position
        #let's find the second position, which is gonna be where the arr[i]th element will go for getting sorted
        id1 = i
        tempid2 = arr[i] - 1
        if arr[tempid2] - 1 != i:
            #then clearly no exception occuring
            #start the required cyclic shifts
            id3 = arr[tempid2] - 1 #basically where the element arr[tempid2] will go to get sorted
            if id3 < tempid2:
                id2 = id3
                id3 = tempid2
                #perform a single left shift
                #which is nothing but a single reverse right shift
                val1 = arr[id1]
                val2 = arr[id2]
                val3 = arr[id3]
                ans.append([id3, id2, id1])
                arr[id1] = val2
                arr[id2] = val3
                arr[id3] = val1
            else:
                id2 = tempid2
                #perform a single right shift
                val1 = arr[id1]
                val2 = arr[id2]
                val3 = arr[id3]
                ans.append([id1, id2, id3])
                arr[id1] = val3
                arr[id2] = val1
                arr[id3] = val2
        else:
            #two conditions gonna be here now, as if no such third index exist
            #then clearly exit the programg by printing -1 as sorting wont be possible
            #else choose the closest unsorted index to id1
            got_the_index = False
            temp_id = -10000
            for x in range(id1 + 1, n - 1):
                if x != tempid2:
                    if arr[x] != sorted_arr[x]:
                        temp_id = x
                        got_the_index = True
                        break
            if not got_the_index:
                print(-1)
                break
            #now checking whether the found index is greater than id2 or smaller than id2;
            #if smaller perform a single right shift
            #else perform a single left shift
            if(temp_id < tempid2):
                id3 = tempid2
                id2 = temp_id
                val1 = arr[id1]
                val2 = arr[id2]
                val3 = arr[id3]
                ans.append([id1, id2, id3])
                arr[id1] = val3
                arr[id2] = val1
                arr[id3] = val2
            else:
                id2 = tempid2
                id3 = temp_id
                val1 = arr[id1]
                val2 = arr[id2]
                val3 = arr[id3]
                ans.append([id3, id2, id1])
                arr[id1] = val2
                arr[id2] = val3
                arr[id3] = val1
        #print(arr)
    if(ans_flag == 1):
        print(len(ans))
        for i in ans:
            for j in i:
                print(j + 1, end=" ")
            print()