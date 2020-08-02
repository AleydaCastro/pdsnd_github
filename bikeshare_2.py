import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': "./chicago.csv",
              'New York City': "./new_york_city.csv",
              'Washington': "./washington.csv" }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = ""
        city = input("Enter city (Chicago, New York City or Washington): ").title()
        if city not in ("Chicago", "New York City", "Washington"):
            print("Invalid city")
            #input("Enter city (Chicago, New York City or Washington): ").title()
            continue
        else:
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        month = ""
        month = input("Enter month (all, january, february, ... , june): ").title()
        if month not in ("All", "January", "February", "March", "April", "May", "June"):
            print("Invalid month")
            #input("Enter month (all, january, february, ... , june): ").title()
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = ""
        day = input("Enter day of week (all, monday, tuesday, ... sunday): ").title() 
        if day not in ("All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
            print("Invalid day")
            #input("Enter day of week (all, monday, tuesday, ... sunday): ").title()
            continue
        else:
            break

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
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'All':
        # months = ['January', 'February', 'March', 'Apr)il', 'May', 'June']
        # month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month: ', common_month)


    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day: ', common_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station: ', common_end_station)

    # display most frequent combination of start station and end station trip
    freq_comb = (df['Start Station'] + " and " + df['End Station']).mode()[0]
    print('Most Frequent Combination of Start and End Station: ', freq_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby('User Type')['User Type'].count()
    print('Counts of User Types: ', user_types)

    try:
        # Display counts of gender
        gender = df.groupby('Gender')['Gender'].count()
        print('Counts of Gender: ', gender)

        # Display earliest, most recent, and most common year of birth
        earlieast_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('The earliest year of birth is {}\n \
            The most recent year of birth is {}\n \
            The most common year of birth is {}'.format(earlieast_year, most_recent_year, most_common_year))

    except:
        print("\nGender and Birth year not available for Washington")
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
def display_data(df):
    raw_data = input("\nWould you like to see raw data? Enter yes or no\n")
    lines = 0
    if raw_data == 'yes':
        print(df.iloc[lines:lines + 5])
        lines += 5
        
        while True:
            five_more = input("\nWould you like to see 5 more lines? Enter yes or no\n")
            if five_more == 'yes':
                print(df.iloc[lines:lines + 5])
                lines += 5
                continue
            else:
                break

        
    
    
    
    


def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
