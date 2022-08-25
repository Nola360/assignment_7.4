#Akinola Daramola Jr
#Programming Exercise 7.3
#Due Date: 07/31/2022

"""
Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a list.
The program should calculate and display the total rainfall for the year,
the average monthly rainfall, the months with the highest and lowest amounts.
"""


def main():
    weatherApp()


def weatherApp():

    months = ["Jan","Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec" ]

    total_rainfall = 0
    avg_monthly_rainfall = 0
    new_month = 0
    rainfall_each_month = []
    max_rainfall = 0
    index = months.index("Jan")
    
    
    for index, rainfall in enumerate(months):
        print(index, rainfall)
        #print("Before ", rainfall)
        #print(months[:])
        rainfall = float(input(f"What is the total rainfall in {rainfall}? "))
        #print("After ", rainfall)
        rainfall_each_month.append(rainfall)
        print("CHECKEDDDDDDD", rainfall_each_month.index(rainfall))
        if rainfall_each_month.index(rainfall) == rainfall_each_month[:].index(rainfall):
            print("DOUBLE CHECKED!!!!!!!!!")
            print(rainfall_each_month[:])
            print(months[index])
        total_rainfall += rainfall
        new_month += 1
        
        if max_rainfall < rainfall:
            max_rainfall = rainfall
            #months[index] = max_rainfall[index]
            index = rainfall_each_month.index(rainfall)
            
    print(rainfall_each_month[index])
    print(f"Total rainfall for year: {total_rainfall:,.2f}")
    print(f"Max rainfall: {max_rainfall:,.2f}")
    print("New Month:", months[index])    
    avg_monthly_rainfall = total_rainfall / new_month
    print(f"Average Monthly Rainfall: {avg_monthly_rainfall:,.2f}")

   
    


main()
