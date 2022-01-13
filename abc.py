import requests
import pandas as pd
url = 'https://raw.githubusercontent.com/saarques/credit-card-fraud-detection/master/fraud_values.csv'
res = requests.get(url, allow_redirects=True)
with open('fraud_values.csv.csv','wb') as file:
    file.write(res.content)
sales_team = pd.read_csv('sales_team.csv')