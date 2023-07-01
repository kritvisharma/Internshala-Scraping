from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get('https://internshala.com/internships/blockchain-internship/').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('div', class_='container-fluid individual_internship visibilityTrackerItem')

print('Input preferred work location (eg: Work From Home, Delhi etc)')
location_pref= input('>')
print('Filtering out latest internships with preferred location...')
print(" ")

def find_jobs():
    for index, job in enumerate (jobs):
        published_date = job.find('div', class_="status-container").div.text

        if 'Today' in published_date or '1 day ago' in published_date or 'Just now' in published_date:

            post = job.find('h3', class_='heading_4_5 profile').text.replace(' ', '')
            company_name = job.find('h4', class_='heading_6 company_name').text.replace(' ', '')
            details = job.a['href']
            location = job.find('a', class_='location_link view_detail_button').text

            if location_pref in location:
                with open(f'posts/{index}.txt','w') as f:

                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Post offered: {post.strip()} \n")
                    f.write(f"More Details: {details.strip()} \n")
                    f.write(f"Location: {location} \n")

                print(f'File saved: {index}')

if __name__ == '__main__':
    while (True):
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)

    

    

