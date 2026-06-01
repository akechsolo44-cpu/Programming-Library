def convert_minutes(numberofepisodes, durationperepisode):
    total_minutes = numberofepisodes * durationperepisode
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes

print(convert_minutes(5, 45))