daily_visitores=[1200,1300,500,300,1100,1400,1537]
highest_traffic=max(daily_visitores)
lowest_traffic=min(daily_visitores)
highest_day=daily_visitores.index(highest_traffic)+1
lowest_day=daily_visitores.index(lowest_traffic)+1
print("highest_traffic_day",highest_traffic)
print("lowest_traffic_day",lowest_traffic)
