# Internshala-Scraping

A small web scraping project made using the BeautifulSoup library in Python to scrap Internshala for an internship in "Blockchain" with the feature of filtering on the basis of location as well as date of posting. The program scraps the website every 10 minutes for updates!

## How to use 

Clone the repository. Once cloned, ensure that you have BeautifulSoup installed. If not, use: 
```
pip install beautifulsoup4
```

Within the directory create a folder called "posts" using the command 
```
mkdir posts
```

To run the program, run the following in the terminal: 
```
python scraping.py
```

Now, in the terminal, enter the preferred location and obtain the filtered results for internships (the internships are filtered to only display internships that are atmost 1 day old)

## Problem Statement 

On internshala, while there are options to filter the internships by stipend, location etc. There isn't an option to filter internships by the date of posting. Internships just 3-4 days old have 2000+ applicants. It is statisticaly proven that early applicants have a greater advantage of getting hired. Hence, this scraping tool helps filter out internships just upto a day old. 


