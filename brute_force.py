def bitAtGivenPosSetOrUnset(n, k):
    new_num = n >> (k - 1)

    # if it results to '1' then bit is set,
    # else it results to '0' bit is unset
    return (new_num & 1)


# Driver code
n = 10
k = 1
if (bitAtGivenPosSetOrUnset(n, k)):
    print("Set")
else:
    print("Unset")