
# 📝 Homework Project: Robot Simulator with Abstraction

## 🎯 Goal
Build a simple **robot simulator** in Python using **abstraction with classes**.  
The robot will:  
1. **Sense** the environment (sensors).  
2. **Decide** what to do (controller).  
3. **Act** on the environment (actuators).  
4. **Report** what it’s doing (notifications).  

Each part is handled by a different team, but in the end, everything integrates into one simulation loop.  

---

## 🔹 Team 1 – Sensors (Abstraction of Inputs)
- Create classes `LidarSensor` and `UltrasonicSensor`.  
- Each has a method `.read_distance()` that returns a distance in meters (simulated with random values).  
- The main program should be able to call `.read_distance()` without caring which sensor is used.  

👉 **Abstraction:** The robot only knows it can “read distance,” not how the sensor works.  

---

## 🔹 Team 2 – Controllers (Abstraction of Decision-Making)
- Create classes `BangBangController` and `ProportionalController`.  
- Each has a method `.decide(setpoint, measurement)` that returns an effort value between -1 and 1.  
- Example: If the setpoint is 2.0 m and the sensor reads 1.0 m, the controller decides whether to move forward or stop.  

👉 **Abstraction:** The robot only knows it can “decide effort,” not how the decision is made.  

---

## 🔹 Team 3 – Actuators (Abstraction of Outputs)
- Create classes `Motor` and `Heater` (or `Gripper`).  
- Each has a method `.apply(effort)` that prints what the actuator is doing.  
  - `Motor.apply(0.5)` → `"Motor running at 50% speed"`.  
  - `Heater.apply(0.5)` → `"Heater at 50% power"`.  

👉 **Abstraction:** The robot only knows it can “apply effort,” not how the actuator works.  

---

## 🔹 Team 4 – Notifications (Abstraction of Communication)
- Create classes `EmailNotification` and `ConsoleNotification`.  
- Each has a method `.send(message)` that reports what the robot is doing.  
  - `ConsoleNotification.send("Robot stopped")` → prints to screen.  
  - `EmailNotification.send("Robot stopped")` → simulates sending an email.  

👉 **Abstraction:** The robot only knows it can “send a message,” not how it’s delivered.  

---

## 🔹 Integration (All Teams Together)
Now combine everything into a **robot loop**:

```python
import time
import random

# Example integration (students will expand this)
sensor = LidarSensor()
controller = ProportionalController(kp=0.5)
actuator = Motor()
notifier = ConsoleNotification()

setpoint = 2.0  # target distance in meters

for step in range(5):
    distance = sensor.read_distance()
    effort = controller.decide(setpoint, distance)
    actuator.apply(effort)
    notifier.send(f"Step {step}: distance={distance:.2f}, effort={effort:.2f}")
    time.sleep(1)
```

---

## ✅ Learning Outcomes
- **Team 1 (Sensors):** Abstraction hides how data is measured.  
- **Team 2 (Controllers):** Abstraction hides how decisions are made.  
- **Team 3 (Actuators):** Abstraction hides how actions are executed.  
- **Team 4 (Notifications):** Abstraction hides how information is communicated.  
- **All together:** The robot loop works with any combination of sensor, controller, actuator, and notifier — thanks to abstraction.  

---

## 🔧 Homework Deliverables
- A Python file with all 4 parts implemented.  
- A main simulation loop that integrates them.  
- At least **one extension** per team (e.g., add a new sensor, a new controller, a new actuator, or a new notification type).  
- A short reflection: *“How did abstraction make it easier to swap components?”*  

---

👉 This way, the **whole class builds one logical system** (a robot simulator), but each team focuses on a different abstraction pillar.  

