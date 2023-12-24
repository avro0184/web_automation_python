import time
from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def generateurl():
    excel_file_path = 'output/output_res.xlsx'
    df_excel = pd.read_excel(excel_file_path)
    # data={"Website": [], "Total search result":[],"Time & Date":[] }
    for _, row in df_excel.iterrows():
        row_values_without_quotes = ' '.join(map(str, row))
        time.sleep(10)
        url = f"https://www.google.com/search?q=site:{row_values_without_quotes}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Mozilla/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            result_stats = soup.find(id="result-stats")
            if result_stats:
                result_count = re.search(r'\d+', result_stats.text)
                if result_count:
                    count_value = int(result_count.group())
                    print(url)
                    print(count_value)
                    current_datetime = datetime.now()
                    formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    data={"Website": [], "Total search result":[],"Time & Date":[] }
                    data["Website"].append(row_values_without_quotes)
                    data["Total search result"].append(count_value)
                    data["Time & Date"].append(formatted_date)
                    result_df = pd.DataFrame(data)
                    result_df.to_excel('output/output_11.xlsx', index=False)

    # result_df = pd.DataFrame(data)
    # result_df.to_excel('output/output_11.xlsx', index=False)


generateurl()