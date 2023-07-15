# cook your dish here
T = int(input())
for i in range(T):
    total_items, min_freshness = map(int, input().split())
    freshness_values = list(map(int, input().split()))
    cost_values = list(map(int, input().split()))
    filtered_cost_values = [cost_values[item] 
                            for item in range(total_items) 
                            if freshness_values[item]>= min_freshness]
    # filtered_cost_values = []
    # for item in range(total_items):
    #     if freshness_values[item] >=min_freshness:
    #         filtered_cost_values.append(cost_values[item])
    print(sum(filtered_cost_values))