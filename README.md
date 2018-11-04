# Investing for Social Good

# Abstract
*"Society is demanding that companies, both public and private, serve a social purpose. To prosper over time, every company must not only deliver financial performance but also show how it makes a positive contribution to society."* - Laurence D. Fink, CEO BlackRock (largest asset manager in the world)

Asset managers are increasingly challenged by their investors to manage their portfolios for social impact. However, it is non-trivial for investors and investment managers to maintain regular oversight over the social impact composition of their portfolios. The U.S. Securities and Exchange Commission’s (SEC’s) EDGAR maintains a digital record of the portfolio filings of publicly traded asset managers. All the News is a Kaggle dataset of news articles primarily from 2016 to 2017. 

Furthermore, it could be interesting to correlate the great public's interest into social good project expressed on social media like Twitter, Facebook or the news with the actual investments that are done. 

# Research questions
- How to map news article sentiments to specific investments held by companies?

- What are the most popular “ethical” or “unethical” investments held by asset managers?

- What asset managers have the portfolios with the greatest/least social impact?
- What is the great public's opinion regarding the companies that held many investments in social good versus those who do not invest in social good? 
  - How to make a raking of “public opinion” regarding a company? 
- Was there a transition toward investing more into social good then into other projects? If yes, when did it happen? 
- Can we extend the project to other countries in other to build a global social good investement chart? 

# Dataset
List the datasets containing the information needed to answer the above mentionned questions: 

- [The news][https://www.kaggle.com/snapcrack/all-the-news/home]

- [SEC asset manager portfolios][https://www.sec.gov/cgi-bin/browse-edgar?company=&CIK=&type=13F&owner=include&count=40&action=getcurrent]
- Twitter : 1% of the tweets of 2017 

Once the projet topic was chosen, the group spent a considerable amount of time to look at the quality of the data. For the members, it was important to make sure that the time allocated to the project will be spend on data science and information extraction and not data cleaning! We found some libraries to generates a .csv-like file listing by company and date the URLs in the SEC archives where the investment portfolios are stored (https://github.com/edouardswiac/python-edgar). Regading the dataset on kaggle, we took a closer look to the comments made about the data and we found no issues. The twitter data is a dataset provided by the course so we are confident that there should not be too many insolvable issues and the data does not look *too bad*. 

# A list of internal milestones up until project milestone 2
- Milestone 1 (M1) 
  - Download the required data
  - Set up the Git and Project plan
- Week 1 - Data Exploration
  - Clean and organize our data
  - NaN values, how can we deal with bots and spam etc. (Read papers that might give us interesting insights)
  - establish a process for performing tests and evaluations on smaller parts of the dataset and understanding to what extent we will need to work within the frameworks of the cluster
  - Understand how the cluster works
- Week 2 - Data Explotation
  - Explore data visualization possibilities
  - Decide which visualizations formats serves the best our purpose.
  - Simple Natural Language Processing (NLP) methods (LSI, pLSI, LDA and VSM using lemmatization, stemming and n-grams) to preform analysis on the twitter data set.
    - Determine a dictionary of keywords linked to emotion and opinion identifiers regarding companies. 
  - Process and perform a detailed analysis of the news and SEC asset manager datasets, perform data wrangling and preprocessing.
- Week 3 - Wraping up 
  - Process and perform a detailed analysis of the news and SEC datasets, filtering out the relevant data and understand how to combine the two datasets with the information on Twitter for instance.
  - Find trends in the data regarding the social opinion to the investors and correlate it with the findings regarding the investments done by companies. 
- Prepare Milestone 2 
  - Comment and debug the code
  - learn from the mistakes made in M1
  - Set clear goals and plans for the next milestone.

#### Questions for TA's

- What technologies do professional data blogs like FiveThirtyEight use for visualisation?
- Is the content we have enough to make a project?
