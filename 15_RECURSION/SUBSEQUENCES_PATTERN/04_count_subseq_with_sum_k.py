## A subsequence is formed by choosing some elements while keeping their original order
# We'll use the power set logic to find the ans
def count_subseq_sum_k(arr,k):
    def count(i,curr_sum):
        if i==len(arr):
            if curr_sum ==k :
                return 1 
            return 0 
        take = count(i+1, curr_sum+arr[i])
        not_Take = count(i+1,curr_sum)
        return take+not_Take
    return count(0,0)
arr = [1,2,3]
print(count_subseq_sum_k(arr,2))
