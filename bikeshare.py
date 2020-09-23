import time
import pandas as pd
import numpy as np
import json

CITY_DATA = { 'chicago': 'chicago.csv',
'new york city': 'new_york_city.csv',
'washington': 'washington.csv' }


def get_City():
    """
    asking user to specify a city to Explore.
    Args:
       none
    Returns:
         city - name of the city to Explore - str
    """
    print('*'*40)
    print('Hello! Let\'s explore some US bikeshare data !')
    print('Informed that data selected only for the first six months in 2017')
    print('*'*40)
    while True:
          city = input("Which city would you like to filter by? \n (N) new york city \n (C) chicago \n (W) washington? ").lower()
          
          
          if city not in ("n", "c", "w"):
              QToCheck=input("Sorry, I didn't catch that. Do you want Try again? or restart? \n (1) Try again \n {2) restart").lower()
              if QToCheck=="1":
                  continue
              else:
                  restart = input('\nWould you like to restart? Enter yes or no.\n')
                  if restart.lower() != 'yes':
                      break
          else:
              if city=="c":
                  city="chicago"
              elif city=="n":
                  city="new york city"
              else:
                  city="washington"
                  
              month = input("Do you want to filter by month Yes or No? \n ").lower()
              if month not in ("yes", "no"):
                    print("Sorry, I didn't catch that. Try again.")
                    continue;
              if month=="yes":
                    print('*'*40)
                    month=get_Month(city)
              else:
                    month="all"
              day=input("Do you want to filter by day Yes or No? \n ").lower()
              if day not in ("yes", "no"):
                    print("Sorry, I didn't catch that. Try again.")
                    continue;
              if day=="yes":
                    print('*'*40)
                    day=get_day(city,month)
              else:
                    day="all"     
                    return city,month,day
            





def get_Month(city):
    """
    asking user to specify a month to Explore.
    Args:
       city - name of the city to Explore - str
    Returns:
         month - name of the month to Explore - str
    """
    while True:
        month = input(" kindly enter the day as follows:  January, February, March, April, May, June ?\n").lower()
        print("Which month would you like to filter by for ",city, "city ? /n",month)
        if month not in ("january", "february", "march", "april", "may", "june"):
            QToCheck=input("Sorry, I didn't catch that. Do you want Try again? or restart? \n (1) Try again \n {2) Restart").lower()
            if QToCheck=="1":
                continue
            else:
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break
        else:
            break;
    return month       




def get_day(city,month):
    """
    asking user to specify a day of week to Explore.
    Args:
       city - name of the city to Explore - str
       month- name of the month to explore- str
    Returns:
       day - name of the month to Explore - str
    """
    while True:
        day = input("kindly enter the day as follows: Saturday,Sunday, Monday, Tuesday, Wednesday, Thursday, Friday.\n").lower()
        print("Which day of week would you like to filter by for ",city, "city and ",month ," month ? /n",day)
        if day not in ("saturday","sunday", "monday", "tuesday", "wednesday", "thursday", "friday"):
            QToCheck=input("Sorry, I didn't catch that. Do you want Try again? or restart? \n (1) Try again \n {2) Restart").lower()
            if QToCheck=="1":
                continue
            else:
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break
        else:
            break;   
    return day;        





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

    # extract month and day of week and hour from Start Time and create new columns(months,day of week and hour)
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
    
    # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        print(day)
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df





def time_stats(df):
    """Displays statistics on the most frequent times of travel.
     Input:
        the dataframe with all the bikeshare data
    Returns: 
       none
    """
    # Popular times of travel
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #1 display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)

    # display the most common start hour

    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)





def station_stats(df):
    """Displays statistics on the most popular stations and trip.
     Input:
        the dataframe with all the bikeshare data
    Returns: 
       none
    """
    #2 Popular stations and trip
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #1 display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)

    #2 display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)

    #3 display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)





def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
     Input:
        the dataframe with all the bikeshare data
    Returns: 
       none
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    # display mean travel time
    max_travel = df['Trip Duration'].max()
    print("Max travel time :", max_travel)

    print("Travel time for each user type:\n")
    # display the total trip duration for each user type
    group_by_user_trip = df.groupby(['User Type']).sum()['Trip Duration']
    for index, user_trip in enumerate(group_by_user_trip):
        print("  {}: {}".format(group_by_user_trip.index[index], user_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)





def user_stats(df):
    """Displays statistics on bikeshare users.
     Input:
        the dataframe with all the bikeshare data
    Returns: 
       none
    """

    print('\n Calculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    # iteratively print out the total numbers of user types 
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)





def user_stats_gender(df):
    """Displays statistics of analysis based on the gender of bikeshare users.
     Input:
        the dataframe with all the bikeshare data
    Returns: 
       none
    """
    try:
    # Display counts by gender
        print("Counts by  gender is:\n")
        gender_counts = df['Gender'].value_counts()
    #  print out the total numbers of genders 
        for index,gender_count   in enumerate(gender_counts):
            print("  {}: {}".format(gender_counts.index[index], gender_count))
    except:
        print('\nThis city does not have Gender data')
    print('*'*40)





def user_stats_birth(df):
    """Displays statistics of analysis based on the birth years of bikeshare users.
     Input:
        the dataframe with all the bikeshare data
    Returns: 
       none
    """
    try:
    # Display earliest, most recent, and most common year of birth
        print("Counts by  earliest, most recent, and most common year of birth is:\n")
        birth_year = df['Birth Year']
    # the most common birth year
        most_common_year = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_year)
    # the most recent birth year
        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)
    # the most earliest birth year
        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)
    except:
        print('This city does not have Birth Year Data')
    print('*'*40)    





def display_data_in_JSON(df):
    """Displays raw bikeshare data in json format.
     Input:
        the dataframe with all the bikeshare data
    Returns: 
       none
    """
    row_length = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_length, 5):
        
        yes = input('\nWould you like to see the particular user trip data in json formt? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break
        
        # retrieve and convert data to json format
        # split each json row data 
        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            # pretty print each user data
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)





def display_raw_data(df):
    """
    Displays the raw data
    Input:
        the dataframe with all the bikeshare data
    Returns: 
       none
    """
    rowIndex = 0

    showdata = input("\n Would you like to see the particular user trip data? Please write 'yes' or 'no' \n").lower()

    while True:

        if showdata == 'no':
            return

        if showdata == 'yes':
            print(df[rowIndex: rowIndex + 5])
            rowIndex = rowIndex + 5

        
        showdata = input("\n Would you like to see five more rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()





def main():
    city = ""
    month = ""
    day = ""
    try:
        while True:
            #Get filters data
            city, month, day = get_City()
            print('*'*40)
            print("You selected city :" ,city," month :", month," day: ", day)
            print('*'*40)
            #load data
            df=load_data(city, month, day)
            #1 Popular times of travel
            time_stats(df)
            #2 Popular stations and trip
            station_stats(df)
            #3 Trip duration
            trip_duration_stats(df)
            #4 User info
            #4#1 counts of each user type
            user_stats(df)
            #4#2 counts of each gender (only available for NYC and Chicago)
            user_stats_gender(df)
            #4#3 earliest, most recent, most common year of birth (only available for NYC and Chicago)
            user_stats_birth(df)
            #5 Display raw data
            #5#1 Display raw data in json format
            display_data_in_JSON(df)
            #5#2 Display raw data in table format
            display_raw_data(df)
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
    except:     
            restart = input('\n Kindly run proram again \n')


if __name__ == "__main__":
	main()




