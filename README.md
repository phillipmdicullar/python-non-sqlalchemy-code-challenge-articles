# Phase 3 Code Challenge: Article management system

An interactive Python program that models a magazine publishing system with Author, Article, and Magazine entities. It showcases object-oriented principles like encapsulation, properties, and relationships between classes.

## Features

-**Authors**: Manage authors, their articles, and topic areas.
-**Articles**: Associate articles with authors and magazines, with validation for title length and format.
-**Magazines**: Manage magazines, their categories, articles, and contributing authors.

## Getting started
### Prerequisites
-**Python 3.7+**
-**Basic understanding of OOP concepts in Python.**

### Setup
1. Clone the repository:
2. git clone <repo-url>
3. cd <repo-directory>
4. python <many_to_many.py>

### Usage

#### Author

##### Methods:
-**articles()**: Returns all articles written by the author.
-**magazines()**: Returns magazines the author has contributed to.
-**add_article(magazine, title)**: Adds a new article for the author.
-**topic_areas()**: Lists unique categories of magazines the author has written for.

##### Articles

-**Properties**: `author, magazine, title`
-`Automatically tracks all created articles.`
 
##### Magazine

-**Properties**: `name, category`
#### Methods:
`articles():` Lists all articles in the magazine.
`contributors():` Returns all authors who have written for the magazine.
`article_titles():` Lists titles of all articles in the magazine.
`contributing_authors():` Filters authors contributing more than two articles.
### Usage
#### Creating authors
- **author1 = Author("John Doe")**
- **author2 = Author("Jane Smith")**
#### Creating magazines
-**magazine1 = Magazine("Tech Trends", "Technology")**
-**magazine2 = Magazine("Foodie's Delight", "Culinary")**

#### Publishing articles
`article1 = Article(author1, magazine1, "AI in 2024")`
`article2 = Article(author2, magazine2, "Top 10 Vegan Recipes")`
#### Retrieve data 
`print(author1.articles())`
#### Get magazine contributions
`print(magazine1.contributors())`
##### Retrieve topic areas
`print(author1.topic_areas())`
#### Conclusion
Feel free to fork the repository and submit pull requests for improvements.