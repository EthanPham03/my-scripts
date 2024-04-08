#!/usr/bin/env python3


# Declaration of variables


# Declaration of function
import psutil

print(f"CPU Time: {psutil.cpu_times().user}")
print(f"CPU Processes: {psutil.cpu_times().system}")
print(f"System Idle:{psutil.cpu_times().idle}")
print(f"Priority Processes:{psutil.cpu_times().nice}")
print(f"I/O Wait Time:{psutil.cpu_times().iowait}")
print(f"Servicing Hardware Interrupts:{psutil.cpu_times().irq}")
print(f"Servicing Software interrupts:{psutil.cpu_times().softirq}")
print(f"Other operating systems:{psutil.cpu_times().steal}")
print(f"Virtual CPU For Guests:{psutil.cpu_times().guest}")

# Main


# End