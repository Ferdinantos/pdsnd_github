import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city with any caps (chicago, new york city, washington)
    print('Which city do you want to explore from chicago, new york city and washington?\n')
    city = input()
    city = city.lower()
    while city != "chicago" and city != "new york city" and city != "washington":
        print("Invalid Entry")
        city = input()


    # TO DO: get user input for month (all, january, february, ... , june)
    print('Which month do you want?  you can pick: all, january, february, ... and june\n')
    month = input()
    month = month.lower()
    while month != "all" and month != "january" and month != "february" and month != "march" and month != "april" and month != "may" and month != "june":
        print("Invalid Entry")
        month = input()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Which day do you want?  you can pick: all, monday, tuesday, ... sunday\n')
    day = input()
    day = day.lower()
    while day != "all" and day != "monday" and day != "tuesday" and day != "wednesday" and day != "thursday" and day != "friday" and day != "saturday" and day != "sunday":
        print("Invalid Entry")
        day = input()

    #we assign value to month (in numbers)
    if month == "january":
        month = 1
    elif month == "february":
        month = 2
    elif month == "march":
        month = 3
    elif month == "april":
        month = 4
    elif month == "may":
        month = 5
    elif month == "june":
        month = 6

    #we assign value to day (in numbers)
    if day == "monday":
        day = 1
    elif day == "tuesday":
        day = 2
    elif day == "wednesday":
        day = 3
    elif day == "thursday":
        day = 4
    elif day == "friday":
        day = 5
    elif day == "saturday":
        day = 6
    elif day == "sunday":
        day = 7

    print('-' * 40)
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
    df['hour'] = df['Start Time'].dt.hour
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int and give us with number the month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Popular month:\n', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Popular Start day of week:\n', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:\n', popular_hour, 'o\'clock')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_ss = df['Start Station'].mode()[0]

    print('Most Popular Start Station:\n', popular_ss)

    # TO DO: display most commonly used end station
    popular_es = df['End Station'].mode()[0]

    print('Most Popular End Station:\n', popular_es)

    # TO DO: display most frequent combination of start station and end station trip
    s1 = df['Start Station'].astype(str) + "->" + df['End Station'].astype(str)

    popular_ses = s1.mode()[0]

    print('Most Popular End Station:\n', popular_ses)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tt = df['Trip Duration'].sum()
    print("total travel time:\n", tt)
    # TO DO: display mean travel time
    att = df['Trip Duration'].mean()
    print("average travel time:\n", att)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()

        print('\nCounts of gender...\n', user_types)

        # TO DO: Display counts of gender
        user_types1 = df['Gender'].value_counts()

        print('\nCounts of gender...\n', user_types1)

        # TO DO: Display earliest, most recent, and most common year of birth
        df['Birth Year'] = pd.to_datetime(df['Birth Year'])
        df['year'] = df['Birth Year'].dt.year
        popular_year = df['year'].mode()[0]
        min_year = df['year'].min()
        max_year = df['year'].max()
        print('Most common Birth Year:\n', int(popular_year))
        print('recent Year:\n', int(max_year))
        print('Earliest Year:\n', int(min_year))
    except:
        print('no statistics')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def show_data(df):
    count = 0
    while True:
        print('Do you want the next five lines of the data? yes or no')
        pick = input()
        pick = pick.lower()
        count = count + 5
        if pick == 'yes':
            print(df.iloc[:count])
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
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
