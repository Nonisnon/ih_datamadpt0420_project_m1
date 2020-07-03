# My project README file

---

![Image](https://res.cloudinary.com/springboard-images/image/upload/q_auto,f_auto,fl_lossy/wordpress/2019/05/aiexcerpt.png)
## **Name**
Module 1 Ironhack Project

### :baby: **Status**
The Pipeline is ready to run

### :running: **One-liner**
There are 3 different datasource involved:

 - Tables (.db). Here you can find the .db file with the main dataset.

 - API. We will use the API from the Open Skills Project.

 - Web Scraping. Finally, we will need to retrieve information about country codes from Eurostat website.
 
 We are going to find out the % of each data job profile grouped by age group
### :computer: **Technology stack**
Python, Pandas, BeautifulSoup, Argparse, Sqlalchemy, Pycharm and Jupyter

### :boom: **Core technical concepts and inspiration**
- Reporting tool to analyze the different job profiles by age group and country.
- This code will generate a .csv file

### :wrench: **Configuration**
Requirements:
- Path: data/raw/raw_data_project_m1.db
- URL: https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes

Libraries:
- You can check it in requirements.txt

### :file_folder: **Folder structure**
```
└── project
    ├── data
        ├── raw
            ├──.db
    ├── processed
    ├── results
        ├── data_grouped
    ├── notebooks
    │   ├── data,api,webscraping.ipynb
    │   └── Function tables.ipynb
    ├── p_acquisition
        ├── m_acquisition.py
    ├── p_analysis
        ├── m_analysis.py
    ├── p_reporting
        ├── m_reporting.py
    ├── p_wrangling
        ├── m_wrangling.py
    ├── .env.txt
    ├── .gitignore
    ├── main_script.py
    ├── README.md
    ├── requirements.txt

```

### :love_letter: **Contact info**
If you have any doubts contact me through antoniodediegosuanzes@gmail.com

---



