def get_max_value(carrot_types, capacity):
    # Convert carrot_types to a list of tuples for easier handling
    carrot_tuples = [(c['kg'], c['price']) for c in carrot_types]

    # Initialize a list for dynamic programming
    dp = [0 for _ in range(capacity + 1)]

    # Iterate through each type of carrot
    for i in range(len(carrot_tuples)):
        # Iterate through each capacity
        for j in range(carrot_tuples[i][0], capacity + 1):
            # Maximize the price at this capacity
            dp[j] = max(dp[j], dp[j - carrot_tuples[i][0]] + carrot_tuples[i][1])

    # The maximum price will be at the end of the list
    return dp[capacity]


def get_min_value(carrot_types, capacity):
    # Convert carrot_types to a list of tuples for easier handling
    carrot_tuples = [(c['kg'], c['price']) for c in carrot_types]

    # Calculate the maximum value using the original function
    max_value = get_max_value(carrot_types, capacity)

    # Initialize a list for dynamic programming
    dp = [0 for _ in range(capacity + 1)]

    # Iterate through each type of carrot
    for i in range(len(carrot_tuples)):
        # Iterate through each capacity
        for j in range(carrot_tuples[i][0], capacity + 1):
            # Maximize the price at this capacity
            dp[j] = max(dp[j], dp[j - carrot_tuples[i][0]] + carrot_tuples[i][1])

    # Calculate the minimum value
    min_value = float('inf')

    # Iterate through each type of carrot
    for i in range(len(carrot_tuples)):
        # Iterate through each capacity
        for j in range(capacity - carrot_tuples[i][0] + 1):
            # Calculate the remaining capacity
            remaining_capacity = capacity - j

            # Check if the current type of carrot can fit within the remaining capacity
            if remaining_capacity >= carrot_tuples[i][0]:
                # Calculate the minimum value
                min_value = min(min_value, max_value - (dp[remaining_capacity] - carrot_tuples[i][1]))

    return min_value

carrot_types = [{'kg': 5, 'price': 100}, {'kg': 7, 'price': 150}, {'kg': 3, 'price': 70}]
capacity = 36

print(get_max_value(carrot_types, capacity))  # Output: 840
print(get_min_value(carrot_types, capacity))  # Output: 70
