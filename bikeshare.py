import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv','washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    print('~'*60)
    while True:
        city = str(input('Which city do you want to see its data? \nPlease choose one (chicago , new york or washington)\n')).lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('Error!!. PLease Enter a valid City \n')
    print('*'*60)       
               
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while True:
        month=str(input('Which month do you want data to be filterd?\nPlease choose one (january, february, march, april, may, june or all) \n')).lower()
        if month in months:
            break
        else:
            print('Error!!. Please Enter a Valid month \n')
    print('*'*60)                  
    days =['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    while True:
        day = str(input('Which day do you want data to be filtered?\nPlease choose one (saturday, sunday, monday, tuesday, wednesday, thursday, friday or all) \n')).lower()
        if day in days:
            break
        else:
            print('Error!!. Please Enter a Valid Day \n')
       
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour
                                  
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
    if month != 'all':
        month = months.index(month) + 1
        df =df[df['month'] == month]
    elif month == 'all':
        df = df
     
                                  
    if day != 'all':
        df = df[df['day'] == day.title()]
    elif day == 'all':
        df = df
  
    return df
counter = 0
def view_data (df):
    global counter
    while True:
        ask_user = input('Would you like to view more raw data for the city selected? \n Print yes or no.\n\n').lower()
        if ask_user == 'yes':
            print(df[counter: counter + 5])
            counter += 5
        else:
            break
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(' The most common month is: ', df['month'].mode()[0])
    print(' The most common day is: ', df['day'].mode()[0])
    print(' The most common hour is: ', df['hour'].mode()[0])
    #Plotting a histogram of trip durations
    plt.hist(df['Trip Duration'], bins=20) 
    plt.xlabel('Trip Duration')
    plt.ylabel('Frequency')
    plt.title('Histogram of Trip Durations')
    plt.show()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def frequent_combination(df):
    combination = df['Start Station'] + 'to' +df['End Station']
    frequent_combination = combination.value_counts().idxmax()
    return frequent_combination

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print(' The most commonly used Start station is: ',df['Start Station'].mode()[0])
    print(' The most commonly used End station is: ',df['End Station'].mode()[0])
    most_frequent_station = frequent_combination(df)
    print(' The most frequent combination start station and end station :\n\n', most_frequent_station)
    #Plotting a bar chart of the most popular start stations
    start_station_counts = data['start_station'].value_counts().head(10)  # Get the top 10 most popular start stations
    plt.bar(start_station_counts.index, start_station_counts.values)
    plt.xlabel('Start Station')
    plt.ylabel('Count')
    plt.title('Top 10 Most Popular Start Stations')
    plt.xticks(rotation=90)  # Rotate x-axis labels if needed
    plt.show()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print(' Total travel time is: ', df['Trip Duration'].sum())
    print(' Average travel time is:', df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print(' Count of User Types :\n', df['User Type'].value_counts())
    if city != 'washington':
        print(' \nCount of Gender :\n', df['Gender'].value_counts()) 
        print(' \nMost common Year of birth is:', int(df['Birth Year'].mode()[0]))  
        print('Most recent Year of birth is:', int(df['Birth Year'].max()))
        print('Most earlist Year of birth is:', int(df['Birth Year'].min())) 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    pass


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        view_data(df)
        time_stats(df)
        frequent_combination(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
