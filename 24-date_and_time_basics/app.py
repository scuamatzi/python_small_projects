from datetime import datetime, timedelta, timezone

now = datetime.now()

print("Formatted: ", now.strftime("%Y-%m-%d %H:%M:%S"))

print("-" * 60)

date_str = "2025-10-08 17:25:05"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f"Parsed: {dt}")

print("-" * 60)

future = now + timedelta(days=5)
past = now - timedelta(days=5)

print(f"Future: {future}")
print(f"Past: {past}")

print("-" * 60)

print(f"Date only: {now.date()}")
print(f"Time only: {now.time()}")

print("-" * 60)

print(f"Day: {now.day}, Month: {now.month}, Year: {now.year}")

print("-" * 60)

print("Weekday (0=Monday): ", now.weekday())
print("ISO Weekday (1=Monday): ", now.isoweekday())

print("-" * 60)

d1 = datetime(2025, 9, 20)
d2 = datetime(2025, 9, 26)

diff = d2 - d1
print("Difference in days: ", diff.days)

print("-" * 60)

utc_now = datetime.now(timezone.utc)
print("UTC Time: ", utc_now)

print("-" * 60)
