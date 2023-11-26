# BEST PRACTICES MOVIE SCHEDULER

## ABOUT

The Best Practices Movie-Scheduler uses a two-tier approach to schedule movies in a multiplex mall of capacity ‘N’ screens and 6 slots per screen. 

In the first tier, the priority score for each movie is generated from the information we collected through user survey. 

Using the calculated priority score,the number of showings per movie is computed, wherein the movie with the maximum score is allotted maximum screening.

The second tier deals with the main scheduling problem. 
The forthcoming week’s scheduling plan is visualized as a two-dimensional (screen-by- slot) matrix, then that matrix contains only “empty cells”.
After the first tier has been successfully executed, some of those empty cells are ‘filled’ given the day of the week.
The movies with a higher priority score to prime showings and the rest to the remaining showings. 

This way we satisfy the demand of the audience, ensure success of the movies, and maximize the theatre’s revenue/ profit.

# SLOTS AVAILABLE PER SCREEN
The total number of slots per screen per day is 6, the timings of the slots are given below.
The slots are of 3 hours each with a 30-minute interval in between slots.

Slot 1 :  5:00am - 8:00am
Slot 2 :  8:30am - 11:30am
Slot 3 :  12:00pm - 3:00pm
Slot 4 : 3:30pm - 6:30pm
Slot 5 : 7:00pm - 10:00pm
Slot 6: 10:30pm - 1:30am

# CONSTRAINTS
- Demand-based calculation of the number of showings per movie based on cast weightage, demand score and success rate.
- Prime-Showtimes are first 'filled' with movies of high priority score and the remaining showings with the remaning movies.
- For a new movie, the runtime and success rate are predefined as 0 and 5 respectively.
- The number of slots varies for weekdays, weekends and festival days, as 4,5 and 6 slots respectively, in order to maximize profit
- If the language of the movie is not the same as the local language, then the priority of the movie will be decreased by 20 percent.
- If the movie has some special features like 3D or Dolby Atmos, then its priority will be increased.
- If the movie has either 3D or Dolby feature then its priority will be increased by a score of 0.5. 
- If the movie has both the features then its priority will be increased by a score of 0.75. 
- If the runtime of the movie is equal to 0 0r 1 weeks, its priority will remain the same.
- If the runtime of the movie is equal to 2 week, its priority will reduce by 25%
- If the runtime of the movie is equal to 3 weeks, its priority will reduce by 50%.
- If the runtime of the movie is equal to 4 weeks, its priority will reduce by 75%.
- If the runtime of the movie is greater than 4 weeks:
- If its demand score is greater than 5, its priority will be reduced by 80% else its priority will be assigned value 0.


# OPERATING INSTRUCTIONS
- In the command prompt, mount on the directory mysite2 present in the Django directory using cd command.
- Run ```python manage.py runserver```
- The development server is hosted and its url appears on the terminal.Copy the url and paste it on the browser.

- The page visible to the user is the About Page, details and working of the algorithm used is expressed here in an aesthetic manner.
- On clicking the 'LET'S BEGIN SCHEDULING' button, the website is redirected to the first survey form of the application.
	- Fill in the number of screens and local language sections. To select multiple special days, CTRL +  click on the day.
	- Click the 'SUBMIT' button.

- After filling the necessary details, the user is redirected to the second form/ survey page on clicking the ‘SUBMIT’ button.

- In the second form, fill the details i.e., Movie name, demand score, cast wieghtage, success rate, runtime, features and language of the movie.
- After filling the necessary details, the user is redirected to the same page on clicking the ‘ADD’ button to go on adding details about the next movie. 
- The page redirects to the third form by clicking the ‘SUBMIT’ button, after filling the details for the last movie. 

- In the third form, fill the details i.e., Movie name, demand score, cast wieghtage,features and language of the movie.
- After filling the necessary details, the user is redirected to the same page on clicking the ‘ADD’ button to go on adding details about the next movie. 
- The page redirects to the result by clicking the ‘SUBMIT’ button, after filling the details for the last movie. 

- The result page displays the generated schedule.

- To quit the server, open the terminal and operate CTRL + C or CTRL + BREAK.

For more details, look into Report.pdf 




