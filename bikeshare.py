import time
import pandas as pd

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
    print('Hello! Let\'s explore some US bike share data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose a city from: (chicago, new york city, washington)\n").lower()
        if city.lower() in ("chicago", "new york city", "washington"):
            break
        else:
            print("Either there's a typo or the input is not there, please try again")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose a month from: (all,january,february,march,april,may,june)\n").lower()
        if month.lower() in ("all", "january", "february", "march", "april", "may", "june"):
            break
        else:
            print("Either there's a typo or the input is not there, please try again")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "Choose a day from: (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)\n").lower()
        if day.lower() in ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"):
            break
        else:
            print("Either there's a typo or the input is not there, please try again")
            continue

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_mode = df["month"].mode()[0]
    print("Most common month is: ", month_mode)

    # TO DO: display the most common day of week
    day_mode = df["month"].mode()[0]
    print("Most common month is: ", day_mode)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour_mode = df["hour"].mode()[0]
    print("Most common start hour is: ", hour_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_start_station = df["Start Station"].mode()[0]
    print("Most common start station is: ", mode_start_station)

    # TO DO: display most commonly used end station
    mode_end_station = df["End Station"].mode()[0]
    print("Most common end station is: ", mode_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["rout"] = df["Start Station"] + "-" + df["End Station"]
    mode_frequency = df["rout"].mode()[0]
    print("Most frequent combination of start station and end station is: ", mode_frequency)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_duration = df["Trip Duration"].count()
    print("Total travel time is: ", travel_duration)

    # TO DO: display mean travel time
    travel_duration_mean = df["Trip Duration"].mean()
    print("Mean travel time is: ", travel_duration_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("The count of user types is: ", user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print("the count of gender is: ", gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_dob = df["Birth Year"].max()
    print("The earliest year of birth is ", earliest_dob)

    recent_dob = df["Birth Year"].min()
    print("The most recent year of birth is ", recent_dob)

    dob_mode = df["Birth Year"].mode()[0]
    print("The most common year of birth is ", dob_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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


if __name__ == "__main__":
    main()
