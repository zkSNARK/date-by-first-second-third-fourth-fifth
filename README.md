# date-by-first-second-third-fourth-fifth
A utility to return the date of the first, second, third, fourth, 
or fifth day (monday, tues, ... etc.) of a given month and year.

You can read the API as 
    get the date of (the <FIRST> <MONDAY> in <DECEMBER> <2020>)
        
By main function in this code is the 'get_date_of(...)' function.

    def get_date_of(ordinal=None, day=None, month=None, year=None, date=None) -> Optional[datetime.date]:


NOTE: 

There are 3 parameters in the header that are need to be considered
with care.

These are the date, and the year / month.  You should consider 
these to be exclusive.  Either pass a date, or pass both a month and
year.

If you pass the date field, you should pass in either a datetime.date 
object or a datetime.datetime object.  This date should be from the 
month you are interested in.  The day you set in the either of those
inputs will be ignored. 

Additionally, you should note that if you happen to pass the both the
month / year and the data parameters, the month / year will override 
the date parameter and the date parameter will be ignored. 
    
As an example, if you would like to get the second tuesday in January
of 2020, you can call the function as follows. 

    date = get_date_of(ordinal.THIRD, calendar.MONDAY, 0, 0)
    
or
    
    date = get_date_of(ordinal=ordinal.FIRST, day=calendar.MONDAY, month=month.JANUARY, year=2019)
    
or 
   
    date = get_date_of(ordinal=ordinal.FIRST, day=calendar.MONDAY, date=datetime.date(year=2019, month=month.JANUARY, day=1))

Check the tests for use.  