![title_picture](/images/movies.jpg)

# Movies Profitability Analysis Based on Genres' Criteria. 

**By Yevgeniy Kostrov**
***
# Overview
The purpose of this project is to analyze a large data set of movies that includes many different types of information about each movie, such as genres, release dates, budgets, box office earnings generated domestically and worldwide. The analysis will focus on following characteristics: release month, the highest number of movies released by genres, average profit by genres combined into groups, average profit by individual genres, and a number of movies released in each genre in a year over year comparison.

* I will measure the success of a movie based on budget and revenue.

* I will explore how the release month affects the success: in what months the most profitable movies are released.

* I will look at most popular genres by count.

* I will analyze a list of grouped genres vs average profit as well as individual genres vs average profit

* At the end, I will provide my recommendations and plan for further analysis.

# Business Problem

As the demand for new, original high quality content grows, driving the competition among the industry players up, the need for comprehensive targeted analytics about what makes a movie successful has been increasing. With the ever growing interest for new movies and a wide range of movie genres, precise analytics about the performance of movies can give useful information to studios, so the most strategic decisions regarding production and financing of the projects can be made. 

# Data Description
This project will use the data from the IMDB database. Specifically, the table that contains release dates, movie titles, and gross revenue domestically and worldwide.  I will also employ the table with primary titles, original titles, start year, run minutes, and genres.
# First part of the data analysis is on the release month. I will plot the histogram of the release months for the profitable movies.

![release_month](/images/ReleaseMonthHist.png)

# Genres
## Now I want to get to the main focus of our study
*** 
## Next, I am going to visualize top genres present in the movies that make profit both domestically and worldwide

<img src="/images/IndividualGenresHist.png" alt="IndividualGenresHist" style="width:600px;height:400px;"> 

## One can see that out of all titles the most movies are in the Drama and Comedy.

## I am also interested in the most common intersection of genres in the movies that bring profit and we use average profit for the resulting histogram

<img src="/images/GroupedGenresHist.png" alt="GroupedGenresHist" style="width:600px;height:400px;"> 

## Now, most common individual genres in the movies that bring profit and we use average profit for the resulting histogram.

<img src="/images/IndividualGenresByProfit.png" alt="IndividualGenresByProfit" style="width:600px;height:400px;">


## It is also interesting to look at a number of movies produced in each genre by year.

![genres_by_year](/images/genres_by_year.png
)

## We can see on the graph  above that most common  movies by genres are Comedy and Drama.
***
## One can suspect, based on the previous plot, that the total number of movies is decreasing.
***
## Next plot shows the total number of movies starts to decrease after 2014.
![total_number_of_movies](/images/total_number_of_movies.png
)

# Conclusions
## Data Modeling
***
I used the following analysis:
* Dropped duplicates, if necessary.
* There are 4000 NaN values in the genres columns of the Basic Titles table. I decided to keep these rows but skip them for visualization purposes.
* I converted dollar amounts from string format into integer format.
* I converted release month from integer format into string for  better readability in the histogram's labels.
* I used appropriate grouping and aggregation by average value for the analysis to produce insights into the genres.
***
## Trends:
###
 After investigation we can see the following trends
1. Most movies are released in December and January.
2. The most common genre among all movies is Drama, then with a big gap, Comedy. From average profit vs combination of genres histogram, we see that Drama has to be combined together with the Adventure or Sci-Fi to bring profit. From the average  profit vs individual genre histogram, we see that Sci-Fi, Adventure, and Animation bring biggest profits.
3. If we look at the Number of  Movies by Genre vs Release Year plot, we notice the most commonly produced movies are Comedies and Drama year after year. We can also notice that the total number of movies is declining. This trend is confirmed in the next plot: Total Number of Movies by Year.  
## Suggestions for a Company that wants to enter the Movie Production industry:
***
* I recommend to consider the following genres or their combination:
> 1. Drama
> 2. Adventure
> 3. Sci-fi
* I recommend to release the movie either in December or in January.
* Due to the rising popularity of the streaming platforms and decrease in total number of movies produced, I recommend to consider collaboration with one of the online streaming content provider in the production of a movie 
***

## Ways to improve the analysis
***
* It would be great to include more recent data into analysis.
* Include movies produced by streaming platforms into analysis.
* Extend the scope of the project to include:
>>> -- analysis of budgets vs profitability 

>>> -- analysis of directors vs profit

>>> -- analysis of actors/actresses and their salaries vs profit
***

Please review my full analysis in [our Jupyter Notebook](./dsc-phase1-project-template.ipynb) or our [presentation](./DS_Project_Presentation.pdf).

For any additional questions, please contact **name & email, name & email**

## Repository Structure

Describe the structure of your repository and its contents, for example:

```
├── README.md                           <- The top-level README for reviewers of this project
├── JupyterNotebooks/project.ipynb      <- Narrative documentation of analysis in Jupyter notebook
├── Project_Presentation.pdf            <- PDF version of project presentation
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```
