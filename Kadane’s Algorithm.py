def maximumSubarraySum(arr):
    n = len(arr)
    maximumSum = -1e8

    for i in range(0, n):
        currentSum = 0
        for j in range(i, n):
            currentSum = currentSum + arr[j]
            if(currentSum > maximumSum):
                maximumSum = currentSum

    return maximumSum

if __name__ == "__main__":
    # Your code goes here
    a = [1, 3, 8, -2, 6, -8, 5];
    print(maximumSubarraySum(a));