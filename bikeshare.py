import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

    city = input('Which city would you like to explore today? \nChicago or New York City or Washington \n').lower()
    while city not in CITY_DATA:
        print('Please enter the correct city name .\n')
        city = input('Which city would you like to explore today? \nChicago or New York City or Washington \n').lower()
    print( "Looks like you want to explore '{}' today, if not, please restart. \n" .format(city))
        #,if not, please reenter your choice {}
        #break
    #city = input().lower()
        #while city in CITY_DATA:
           # print( "Looks like you want to explore '{}' today, if not, please restart. " .format(city))
            #break

    # get user input for month (all, january, february, ... , june)
    Month_Data = [ 'january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('Please select from the following months -  january, february, march, april, may, june or all. \n').lower()
    while month not in Month_Data:
        print('Please pick the correct month')
        month = input('Please select from the following months - january, february, march, april, may, june or all. \n').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    Day_Data = [ 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = input("Please select the day from -  sunday, monday, tuesday, wednesday, thursday, friday, saturday or all . \n").lower()
    while day not in Day_Data:
        print('Incorrect Day')
        day = input("Please select the correct day from -  sunday, monday, tuesday, wednesday, thursday, friday, saturday or all . \n").lower()



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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]


     # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    """
    data = 0

    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            print(df[data : data+5])
            data += 5

        else:
            break



def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    while month != 'all':
        print('You have already chosen a particular month: {} .' .format(month))
        break
    else:
        Common_Month = df['month'].mode()[0]
        print('The most common month is {}.' .format(Common_Month))

    # display the most common day of week
    if day == 'all':
        Common_Day = df['day_of_week'].mode()[0]
        print('The most common day is {}.' .format(Common_Day))
    else:
        print("You have already chosen '{}' as particular day of week." .format(day))

    # display the most common start hour
    print ('The most commom start hour is {}.' .format(df['hour'].mode()[0]) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Common_start_station = df['Start Station'].mode()[0]
    print('The Most Common Start Station is {}.' .format(Common_start_station))

    # display most commonly used end station
    Common_end_station = df['End Station'].mode()[0]
    print('The Most Common End Station is {}.' .format(Common_end_station))

    # display most frequent combination of start station and end station trip
    Freqcombo_start_end_station = df.groupby(['Start Station','End Station']).count().idxmax()[0]
    print('The most frequent combination of Start station and End station trip is {}.' .format(Freqcombo_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {}.' .format(Total_travel_time))
    # display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {}.' .format(Mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    Count_user_type = df['User Type'].value_counts()
    print('Here are the User Type counts: \n{}.' .format(Count_user_type))

    # Display counts of gender
    while city != 'washington':
        Count_gender = df['Gender'].value_counts()
        print('\nHere are the Gender counts: \n{}.' .format(Count_gender))
        break
    else:
        print('\nSorry! We don\'t have the Gender/ Birth Year Dataset for Washington.')


    # Display earliest, most recent, and most common year of birth
    while city != 'washington':
        Earliest_birth_year = df['Birth Year'].min()
        print('\nThe Earlist birth year is {}.' .format(Earliest_birth_year))

        Mostrecent_birth_year = df['Birth Year'].max()
        print('The Most recent birth year is {}.' .format(Mostrecent_birth_year))

        Mostcommon_birth_year = df['Birth Year'].mode()[0]
        print('The Most common birth year is {}.\n' .format(Mostcommon_birth_year))
        break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
