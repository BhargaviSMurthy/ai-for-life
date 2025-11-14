import csv

def save_to_csv(filepath, records):
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "rate", "holiday", "workday_count"])
        
        for r in records:
            writer.writerow([r.date, r.rate, r.is_holiday, r.workday_count])
