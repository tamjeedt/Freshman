#Coursework - task 4, Tamjeed
#Started - 18/11/23
#Completed - 13/12/23

#Imported libraries
import numpy as np
import matplotlib.pyplot as plt

#Part i
#Defining a function that's representing the given differential equation
def velocity_equation(t):
    #Each part of the equation has been broken down to allow smooth calculation and easy editing
    sin = np.sin(2 * np.pi * t)
    exp = np.exp(-0.618 * t)
    v = 0.4 * sin * exp
    #Returns the value for velocity after making the calculation
    return v

#Application of Euler's method
def euler_method(function, t0, tn, h):
    num_steps = int((tn - t0) / h) + 1
    t_values = np.linspace(t0, tn, num_steps)
    v_values = np.zeros(num_steps)
    #Initial condition
    v_values[0] = function(t0)
    #Iterate using Euler's method
    for i in range(1, num_steps):
        v_values[i] = v_values[i - 1] + (function(t_values[i - 1]) * h)
    return t_values, v_values

#Parameters for the function
t0 = 0   #Initial time
tn = 1   #Final time
h = 0.1  #Time step size

#Using Euler's method to predict horizontal displacement at t = 1 s
t_values, v_values = euler_method(velocity_equation, t0, tn, h)

#Index corresponding to t = 1 s
index_t1 = int((1 - t0) / h)

#Predicted horizontal displacement at t = 1 s
displacement_at_t1 = v_values[index_t1]

#Results shown
print("Predicted horizontal displacement [t = 1s]:", displacement_at_t1,"m")

#Part ii
#Exact solution
t_exact = np.linspace(0, 1, 1000)
v_exact = velocity_equation(t_exact)

#Different time step sizes (taking different time steps sizes to expain the accuracy using the a graph)
h_values = [0.1, 0.05, 0.01]

#Plotting exact solution graph
def exact_solution():
    plt.figure(figsize=(10, 6))
    plt.plot(t_exact, v_exact, label='Exact Solution', linestyle='--')
    #Plotting Euler's method for different time step sizes
    for h in h_values:
        t_values, v_values = euler_method(velocity_equation, 0, 1, h)
        plt.plot(t_values, v_values, label=f'Euler (h={h})')

#Graph plotting carried out within a function
def graph_for_evidence():
    plt.title("Effect of Time Step Size on Euler's Method Accuracy")
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity')
    plt.legend()
    plt.show()

#Euler's method is a first order method where the error of this method is proportional the time step sizes used. Therefore, when the step size is higher the method's accuracy
#decreases and correspondingtly the the accuracy increases when the step sizes reduce accordingly smaller step sizes results to more precise numerical intergration.
#in order to assess the accuracy of the prediction the outcome obtained could be compared with different step sizes against the actual solution of the differential equation.
#hence the above plotted graph assess the accuracy.


#Part iii
#Function to find the derivative of the velocity to find the time at the maximum displacement
def velocity_derivative(t):
    #The function has been split into the two products that are added together when function V is differentiated using the product rule
    product_1 = -0.2472 * (np.sin(2 * np.pi * t)) * (np.exp(-0.618 * t))
    product_2 = 0.8 * (np.pi) * (np.cos(2 * np.pi * t)) * (np.exp(-0.618 * t))
    #dV is the derivative of V - the displacement (dV/dt)
    dV = product_1 + product_2
    #Returns dV/dt
    return dV

#Implement the bisection method to find the time of maximum displacement
def calculate_time_at_max_displacement(function, a, b, tol):
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if function(midpoint) == 0:
            return midpoint
        elif function(midpoint) > 0:
            a = midpoint
        else:
            b = midpoint
    return (a + b) / 2

#Function to print time corresponding to the maximum displacement
def return_corresponding_time():
    #Set initial interval boundaries and threshold
    time_a = 0
    time_b = 1
    threshold = 0.01
    #Find the time corresponding to the maximum displacement
    max_time = calculate_time_at_max_displacement(velocity_derivative, time_a, time_b, threshold)
    print("Time corresponding to maximum displacement:", max_time,"s")

#Calls the function to print the time corresponding to the maximum displacement
return_corresponding_time()

#Function is called to display the exact solution and graph
exact_solution()
graph_for_evidence()