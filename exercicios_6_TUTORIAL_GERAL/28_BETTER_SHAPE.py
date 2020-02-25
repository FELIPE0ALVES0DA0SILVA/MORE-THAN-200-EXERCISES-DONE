import datetime

current_weight = 130
goal_weight = 160
avg_lbs_week = 1

start_date = datetime.date.today()
end_date = start_date

while current_weight < goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight += avg_lbs_week

print(end_date)
print(f"Reached  goal in {(end_date - start_date).days // 7} weeks ")

