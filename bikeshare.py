import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
            
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to view: {}, or {} and {} from the list of cities?".format('chicago', 'new york city', 'washington')).lower()
        if city in CITY_DATA:
            break
            print("Sorry! invalid input")
        else:
            print("Provide a valid input")
            

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would you want to view: {}, {}, {}, {}, {}, or {} and {} in the list of months?".format('all', 'january', 'february', 'march', 'april', 'may', 'june')).lower()
        if month in months_list:
            break
            print("input not correct")
        else:
            print("Provide a valid input")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want to see {}, {}, {}, {}, {}, {}, {}, {} movements in the city?".format('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')).lower()
        if day in days_list:
            break
            print("Wrong date input!")
        else:
            ("Provide a valid input")
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):          
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
        
    """
    
    df = pd.read_csv(CITY_DATA[city])
    
    # converting the start time column to datetime
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
#     df['city'] = df['Start Time'].dt.city
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # Filtering the specified city by month and day
#     city = ['chicago', 'new york city', 'washington']
#     if city != 'all':
#         city = city.index(month)
#         df = df[df['city'] == city]
        
        
    if month != 'all':
        months_list = ['january', 'february', 'march', 'april', 'may', 'june']    #.index(months_list[0]) 
    #if month != 'all':
        month = months_list.index(month)+ 1
        df = df[df['month'] == month]       # creating a new DataFrame for the month and day: Hints from Udacity classroom
   # else: 
       # print('month is all')
        
      
    
    if day != 'all':
#         days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']   #.index(days_list[0]) 
#         day = days_list.index(day)+ 1
        # creating a new DataFrame for the month and day: Hints from Udacity classroom
        df = df[df['day_of_week'] == day.title()]         
        
        
        
    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #frequent_month = df['month'].mode()[0]
    print('frequent_month would be: {}'.format(df['month'].mode()))       #removed [0]


    # TO DO: display the most common day of week
    #frequent_day = df['day'].mode()[0]
    #day != True
    #while True:               #adding a while loop
    city = ['chicago', 'new york city', 'washington']
    for key in CITY_DATA:
        if (CITY_DATA[key] == 'day'):
            #while key == CITY_DATA:
            day = False       #changed to False
            break
            print("These {} of the month wasn\'t captured: " + str(day).mode())
        else:
            print('check for the right information')            
   
    # TO DO: display the most common start hour
    #df['hour'] = df['Start Time'].dt.hour
    #frequent_hour = df['hour'].mode()[0]
    print('frequent_hour would be: {}'.format(df['hour'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station: Hints from Udacity classroom
    #frequent_start_station = df['Start Station'].mode()[0]
    print('frequently used start station would be: {} '.format(df['Start Station'].mode())) 


    # TO DO: display most commonly used end station
    #frequent_end_station = df['End Station'].mode()[0]
    print('frequently end station would be: {} '.format(df['End Station'].mode())) 
    


    # TO DO: display most frequent combination of start station and end station trip
    df['f_comb_of_start_end_station'] = df['Start Station'] + '-' + df['End Station'].mode()
    print('frequently combined stations are: {}'.format(df['f_comb_of_start_end_station']))
                                  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel
    total_travel_time = df['Trip Duration'].sum().round()
    print('total_travel_time is: ', (df['Trip Duration'].sum()))
                                  


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ', (df['Trip Duration'].mean()))
                                                              
                                                              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #df['User Type'] = df['User Type'].value_counts()
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender 
#     city = ['chicago' 'new york city', 'washington']
if 'Gender' in CITY_DATA:
    if city != 'washington':
        print('The count for gender is:', df['Gender'].value_counts().to_frame())
    else:
        print("Gender information can\'t be accessed because it is not available")
        
    # TO DO: Display earliest, most recent, and most common year of birth 
    if 'Birth Year' in CITY_DATA:
        print('The youngest is:', int(df['Birth Year'].min()))  
        print('The most recent viewers are:', int(df['Birth Year'].max()))
        print('The most common year is:', int(df['Birth Year'].mode()))
    
                                                       
                                                          


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
       
       
        
                                                                              
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
                   #changed from break statement


if __name__ == "__main__":
	main()
   
    
    
