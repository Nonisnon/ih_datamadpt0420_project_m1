import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

#Function to clean Age column
def clean_age(df):
    df['age'] = df['age'].apply(lambda age: re.sub(' years old', '', age))
    df['age'] = df['age'].apply(lambda age: age if len(age)<3 else 2016-int(age))
    return df


def age_group(df_group):
    df_group['age_group'] = df_group['age_group'].replace('juvenile','14_25').replace('_','-')
    return df_group


#function to clean Gender column
def clean_gender(df_gender):
    df_gender['gender'] = df_gender['gender'].replace('male','Male')\
        .replace('female', 'Female')\
        .replace('FeMale', 'Female')\
        .replace('Fem', 'Female')

    return df_gender


def job_id(df_normalized_job_codes):
    jobs_id = list(df_normalized_job_codes['normalized_job_code'].unique())
    print('importing...')
    return jobs_id


#Api function
def get_jobs(jobs_id):
    print('calling the api...')
    jobs_titles = []
    for i in jobs_id:
        if i == None:
            pass
        else:
            response = requests.get(f'http://api.dataatwork.org/v1/jobs/{i}')
            jobs_json = response.json()
            jobs_titles.append(jobs_json)
    df_jobs = pd.DataFrame(jobs_titles)
    df_jobs = df_jobs.rename(columns={'uuid': 'normalized_job_code'})
    df_jobs = df_jobs[['normalized_job_code', 'title', 'normalized_job_title']]
    return df_jobs

#function web scraping
def get_info(url):
    print('Scraping...')
    #url = ('https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes')
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table')
    list_a = []

    rows = table.find_all('tr')

    for tr in rows:
        columns = tr.find_all('td')
        for td in columns:
            list_a.append(td.text)

    list_cleaned = [i.replace('\n', '').replace('(', '').replace(')', '') for i in list_a]
    row_split = 2
    rows_refactored = [list_cleaned[x:x + row_split] for x in range(0, len(list_cleaned), row_split)]
    df_countries = pd.DataFrame(rows_refactored, columns={'country_name', 'country_code'})
    df_countries['country_code'].replace({'EL': 'GR'}, inplace=True)
    return df_countries


#merge
def data_merged(df_countries, df_raw, df_jobs):
    print('Merging data...')
    m1 = df_raw.merge(df_countries, how='left', on='country_code')
    m2 = m1.merge(df_jobs, how='left', on='normalized_job_code')
    m2.rename(columns={'title': 'Job_Title', 'country_name': 'Country', 'age': 'Age', 'age_group': 'Age_Group', 'uuid': 'Quantity'}, inplace=True)
    m2['Job_Title'].fillna('Unemployed', inplace=True)
    m3 = m2[['Country', 'Job_Title', 'Age_Group', 'Quantity']]
    m4 = pd.DataFrame(m3)
    #m4.to_csv(f'/Users/Nonis/desktop/ih_datamadpt0420_project_m1/data/processed/data_merged.csv', index=False)
    return m4


#def wrangling(data_base):
    #url = ('https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes')
    #countries = get_info(url)
    #jobs = job_id(data_base)
    #data_jobs = get_jobs(jobs)
    #data_base_age_clean = clean_age(data_base)
    #data_age_group = age_group(data_base)
    #df_final = clean_gender(data_base)
    #data_merge = data_merged(df_final, countries, data_jobs)
    #data_merge.to_csv(f'/Users/Nonis/desktop/ih_datamadpt0420_project_m1/data/processed/data_merge.csv', index=False)
    #return data_merge