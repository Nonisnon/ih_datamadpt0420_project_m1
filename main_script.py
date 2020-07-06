import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man

def argument_parser():
    parser = argparse.ArgumentParser(description = 'Specify path and url...')
    parser.add_argument("-p", "--path", type=str, help="Specify path...", required=True)
    parser.add_argument("-u", "--url", type=str, help="Specify url...", required=True)
    #parser.add_argument('-c', '--country', type=str, help='Specify country', required=True)
    args = parser.parse_args()
    return args

def main(arguments):
     data_base = mac.raw_data(arguments.path)
     data_countries = mwr.get_info(arguments.url)
     #prueba = mwr.wrangling(data_base)
     jobs = mwr.job_id(data_base)
     data_jobs = mwr.get_jobs(jobs)
     data_base_age_clean = mwr.clean_age(data_base)
     data_age_group = mwr.age_group(data_base)
     df_final = mwr.clean_gender(data_base)
     data_mrg = mwr.data_merged(df_final, data_countries, data_jobs)
     data_group = man.data_grouped(data_mrg)
     print('pipeline finished!!!')
     print(data_group)

if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)


