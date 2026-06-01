def estimate_arrival(distance_km, weather_condition):
    travel_time = distance_km * 3

    if weather_condition == "Rainy":
        travel_time += 10

    return travel_time

print(estimate_arrival(10, "Rainy"))