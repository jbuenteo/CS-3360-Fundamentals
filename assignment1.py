import random
import math

NUM_PROCESSES = 1000
LAMBDA = 2.0
TS = 1.0

processes = []

arrival_time = 0

for pid in range(1, NUM_PROCESSES + 1):

    if pid == 1:
        inter_arrival = 0
    else:
        u = random.random()

        while u == 0:
            u = random.random()

        inter_arrival = round((-math.log(u)) / LAMBDA) 

    arrival_time += inter_arrival

    u2 = random.random()

    while u2 == 0:
        u2 = random.random()

    service_time = round(-TS * math.log(u2))

    if service_time < 1:
        service_time = 1

    processes.append({    
       "pid": pid,
        "arrival_time": arrival_time,
        "service_time": service_time
   })

print("\nPROCESS LIST")
print ("PID Arrival Service")

for p in processes[:20]:
    print(
        p["pid"],
        p["arrival_time"],
        p["service_time"]
    )

timeline = []

cpu_time = 0

for p in processes:

    arrival_time = p["arrival_time"]
    service_time = p["service_time"]
    pid = p["pid"]

    if arrival_time > cpu_time:

        timeline.append(
            (
                cpu_time, 
                arrival_time, 
                "IDLE", 
                None
            )       
        )
    
        cpu_time = arrival_time

        start_time = cpu_time
        finish_time = start_time + service_time

        p["start_time"] = start_time
        p["finish_time"] = finish_time

        timeline.append(
            (
                start_time, 
                finish_time, 
                "BUSY", 
                pid
            )       
        )

        cpu_time = finish_time

    print("\nCPU TIMELINE")

    for segment in timeline[:20]:

        start, finish, status, pid = segment

        if status == "IDLE":
            print(f"{start} - {finish}: CPU is idle")
        else:
            print(f"{start} - {finish}: Process {pid} is running")

total_time = cpu_time

average_service_time = (
        sum(p["service_time"] for p in processes) / NUM_PROCESSES
    )

average_waiting_time = (
        sum(p.get("start_time", 0) - p["arrival_time"] for p in processes) / NUM_PROCESSES
    )

average_turnaround_time = (
        sum(p.get("finish_time", 0) - p["arrival_time"] for p in processes) / NUM_PROCESSES
    )    

busy_time = sum(
        p["service_time"] for p in processes
    )

cpu_utilization = (
        busy_time / total_time
    ) * 100

throughput = (
    NUM_PROCESSES / total_time       
)

arrival_rate = (
    NUM_PROCESSES / processes[-1]["arrival_time"]
)

print("\nSTATISTICS")
print("--------------------")
print(f"Total time: {total_time}")
print(f"Average service time: {average_service_time:.2f}")
print(f"Average waiting time: {average_waiting_time}")
print(f"Average Turnaround Time: {average_turnaround_time:.2f}")
print(f"CPU Utilization: {cpu_utilization:.2f}%")
print(f"Throughput: {throughput:.4f}")
print(f"Arrival Rate: {arrival_rate:.3f}")

print("\nGenerated Averages")
print("--------------------")
print(f"Expected Lambda: 2.0")
print(f"Actual Lambda: {arrival_rate:.4f}")
print(f"Expected Service Time: 1.0")
print(f"Actual Average Service Time: {average_service_time:.4f}")
