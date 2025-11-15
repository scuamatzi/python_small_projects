import psutil

print(f"{'PID':<10} {'Name':<25} {'Status':<15} {'Username':<20}")
print("-" * 70)

for proc in psutil.process_iter(["pid", "name", "status", "username"]):
    try:
        pid = proc.info["pid"]
        name = proc.info["name"] or "N/A"
        status = proc.info["status"] or "N/A"
        username = proc.info["username"] or "N/A"

        print(f"{pid:<10} {name:<25} {status:<15} {username:<20}")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
