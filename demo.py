def raft(goat_weights, capacity, K_trips):
    trips = 0
    remaining_goat_weights = goat_weights[:]

    while remaining_goat_weights:
        current_weight = 0
        i = 0
        while i < len(remaining_goat_weights):
            if current_weight + remaining_goat_weights[i] <= capacity:
                current_weight += remaining_goat_weights[i]
                remaining_goat_weights.pop(i)
            else:
                 i+=1
        trips += 1

        if trips > K_trips:
            return False
    return True



def min_capacity(n, k, goat_weights):
    goat_weights.sort(reverse=True)
    left = max(goat_weights)
    right = sum(goat_weights)

    while left < right:
        mid = (left + right) // 2
        if raft(goat_weights, mid, k):
            right = mid
        else:
            left = mid + 1
    return left

n, k = map(int, input().split())
goat_weights = list(map(int, input().split()))

print(min_capacity(n,k,goat_weights))


