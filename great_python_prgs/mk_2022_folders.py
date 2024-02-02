from pathlib import Path
import calendar

month_names = list(calendar.month_name[1:])
days = ['Day 1', 'Day 8', 'Day 15', 'Day 22', 'Day 28']

for i, month in enumerate(month_names):
    for day in days:
        Path(f'2023/{i+1}.{month}/{day}').mkdir(parents=True, exist_ok=True)