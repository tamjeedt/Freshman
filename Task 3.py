#Coursework - task 3, Tamjeed
#Started - 18/11/23
#Completed - 13/12/23

#Imported libraries
import numpy as np # import the numpy library for data analysis
import matplotlib.pyplot as plt # import matplot for data visualisation

#Part i
#Function to define V(z)
def calculate_wind_speed(z):
    #Constants have been defined to allow changes and separated to make the function easy to read
    H = 10
    v_at_H = 12.5
    v_at_z = v_at_H * ((z / H) ** 0.12)
    #Returns the calculated wind speed
    return v_at_z



#Part ii
def graph_for_wind_speeds():
    points = np.linspace(0, 150, 7)
    #Wind speeds calculated and assigned to an array
    wind_speeds = [calculate_wind_speed(z) for z in points]
    plt.plot(points, wind_speeds, marker = "o", linestyle = "-", color = "b")
    #Title of the graph
    plt.title("Wind Speed Profile Along the Tower")
    #x-axis label
    plt.xlabel("Altitude (meter)")
    #y-axis label
    plt.ylabel("Wind Speed (m/s)")
    plt.grid(True)
    #Displays the graph
    plt.show()



#Part iii
#Function to define V^2
def v_squared(z):
    v = calculate_wind_speed(z)
    v_sqr = v ** 2
    return v_sqr

#Lower limit for the integral
a = 0
#Upper limit for the integral
b = 150

#Function for carrying out repeated trapezium rule
def repeated_trapezium_rule(nstrip):
    #x value of each strip
    x_strip = np.linspace(a, b, nstrip + 1)
    #Initialises the result variable
    trapezium_result = 0.0
    #Calculates the step size
    h = (b - a) / nstrip
    #For loop to calculate the sum of all the strips
    for i in range(0, len(x_strip) - 1):
        #Adds the values at each endpoint and doubles every value in between them
        trapezium_result += v_squared(x_strip[i]) + v_squared(x_strip[i + 1])
    #Returns the final result after multiplying by the step size and dividing by 2 to satisfy the trapezium rule formula
    return trapezium_result * h / 2

#Function for carrying out repeated simpson's rule
def repeated_simpsons_rule(nstrip):
    #x value of each strip
    x_strip = np.linspace(a, b, 2 * nstrip + 1)
    #Initialises the result variable
    simpsons_result = 0.0
    #Calculates the step size
    h = (b - a) / (2 * nstrip)
    #For loop to calculate the sum of all the strips
    for i in range(0, len(x_strip) - 1):
        if i == 0 or i == len(x_strip) - 1:
            #Endpoints contribute with weight 1
            simpsons_result += v_squared(x_strip[i])
        elif i % 2 == 1:
            #Odd numbers have a weight of 4
            simpsons_result += 4 * v_squared(x_strip[i])
        else:
            #Even numbers have a weight of 2
            simpsons_result += 2 * v_squared(x_strip[i])
    #Returns the final result after multiplying by the step size and dividing by 3 to complete the Simpson's rule formula
    return simpsons_result * h / 3

#Formula to calculate F drag using repeated trapezium rule for the integral
def formula_using_trapezium(z):
    integrate_trapezium = repeated_trapezium_rule(z)
    C = 0.6  #Drag coefficient
    P = 1.29 #Air density
    D = 10   #Circular cross-section diameter of the tower
    #For F drag - the wind drag
    using_trapezium = 0.5 * C * P * D * integrate_trapezium
    #Returns the value
    return using_trapezium

#Formula to calculate F drag using repeated Simpson's rule for the integral
def formula_using_simpson(z):
    integrate_simpson = repeated_simpsons_rule(z)
    C = 0.6  #Drag coefficient
    P = 1.29 #Air density
    D = 10   #Circular cross-section diameter of the tower
    #For F drag - the wind drag
    using_simpson = 0.5 * C * P * D * integrate_simpson
    #Returns the value
    return using_simpson

#Function to calculate and return both values obtained for F drag using the respective integration rules
def calculate_wind_drags(z):
    with_trapezium = formula_using_trapezium(z)
    with_simpson = formula_using_simpson(z)
    #Both values are returned as a tuple
    return with_trapezium, with_simpson

#Both values are assigned as a tuple
wind_drag_result_trapezium, wind_drag_result_simpson = calculate_wind_drags(6)
print("Initial Wind drag [Trapezium rule]:", wind_drag_result_trapezium,"Ns^2/m") #Values printed with their unit
print("Initial Wind drag [Simpson's rule]:", wind_drag_result_simpson,"Ns^2/m")



#Part iv
#Carries out the repeated Simpson's rule until a satisfactory result has been reached
def calculate_satisfactory_wind_drag(threshold = 0.01): #Threshold can be altered to be as precise as possible
    #Starts with 6 strips initially - can be altered
    nstrip = 6
    #Initial result from the integration is assigned as the previous result
    previous = formula_using_simpson(nstrip)
    print("Wind drag [Simpson's rule]:", previous,"Ns^2/m")
    #While loop used to repeat the process until the threshold has been satisfied
    while True:
        #Number of strips doubles in each iteration
        nstrip *= 2
        #Current result assigned to a variable
        current = formula_using_simpson(nstrip)
        #Difference is calculated
        difference = abs(current - previous)
        print("Wind drag [Simpson's rule]:", current,"Ns^2/m")
        #Breaks the loop only if the threshold is met
        if difference < threshold:
            break
        previous = current

#Calls the function
calculate_satisfactory_wind_drag()

#Function for part ii is called
graph_for_wind_speeds()