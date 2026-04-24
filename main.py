from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt

attendance = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0
}

def add_data(event):
    day = document.getElementById("day").value
    absences = document.getElementById("absences").value

    if absences == "":
        return

    attendance[day] = int(absences)
    draw_graph()

def reset_data(event):
    for day in attendance:
        attendance[day] = 0
    document.getElementById("absences").value = ""
    draw_graph()

def draw_graph():
    days = list(attendance.keys())
    values = np.array(list(attendance.values()))

    plt.clf()
    plt.figure(figsize=(6,4))
    plt.plot(days, values, marker='o', linewidth=3)
    plt.fill_between(days, values, alpha=0.2)
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Absences")
    plt.grid(True)

    display(plt, target="plot", append=False)

draw_graph()
