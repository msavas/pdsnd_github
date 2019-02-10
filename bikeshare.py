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
    print('Hello! Let\'s get ready to explore some AMAZING!!! US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            #asks for user input and converts it to all lowercase
            test_city = input('Enter New York City, Chicago, or Washington: ').lower()
            #tests if user input is in the CITY_DATA dictionary
            CITY_DATA[test_city]
            #if in the dictionary, assigns user input to city variable
            city = test_city
            break
        except:
            print('That is an invalid entry. Please enter New York City, Chicago, or Washington.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month_dict = {'all': 0, 'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6 }
            test_month = input('Enter a month between January and June or type ALL: ').lower()
            month_dict[test_month]
            month = test_month
            break
        except:
            print('Invalid entry. Don\'t give up! Try again! Choose a month between January and June OR type ALL ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            #method is the same as for months just above
            day_dict = {'all': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6,'sunday': 7 }
            test_day = input('Enter or a day of the week or ALL: ').lower()
            day_dict[test_day]
            day = test_day
            break
        except:
            print('Invalid entry. Enter a day of the week or type ALL: ')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time into datetime so we can extract month and day
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #create new columns for month and day
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #filter by dayofweek if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    datetime = pd.to_datetime(df['Start Time'])
    df['month'] = datetime.dt.month
    popular_month = df['month'].mode()[0]
    print('The most popular month is:', popular_month)

    # TO DO: display the most common day of week
    df['day'] = datetime.dt.dayofweek
    popular_day = df['day'].mode()[0]
    print('The most popular day is:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = datetime.dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most common start station is:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most common start station is:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combo = df.groupby(['Start Station', 'End Station']).size().sort_values(axis=0, ascending=False).head(1)
    print('The most populat start and end station journey is: ', combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total time traveled is: ', total_travel)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time is: ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User type totals are: ', user_type)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Gender figures are: ', gender)
    except:
        print('This city does not have gender data.')

    # TO DO: Display earliest, most recent, and most common year of birth
    #earliest year of birth
    try:
        earliest_year = df['Birth Year'].sort_values(axis=0).head(1).sum()
        print('The earliest year of birth is: ', earliest_year)
    except:
        print('This city does not have birth year data')

    #most recent year of birth
    try:
        latest_year = df['Birth Year'].sort_values(axis=0, ascending=False).head(1).sum()
        print('The most recent year of birth is: ', latest_year)
    except:
        print('This city does not have birth year data')
    #most common year of birth
    try:
        most_common_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is: ', most_common_year)
    except:
        print('This city does not have birth year data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def indiv_data(df):
    counter = 5
    more_data = input('Would you like to see individual ride data? yes or no: ')
    if more_data.lower() == 'yes':
        print(df.head(counter))
        while input('Five more? yes or no: ') == 'yes':
            counter += 5
            print(df.head(counter))
    else: print('No problem.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        indiv_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
