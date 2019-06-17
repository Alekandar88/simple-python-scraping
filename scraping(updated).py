import pandas as pd 
import urllib.request, urllib.parse, urllib.error
import urllib.request,urllib.parse,urllib.error
import datetime



data = pd.read_csv("stc.csv") 
#data = pd.read_csv("stc_whole.csv") 
data["Salesperson Name"]=''
data["Salesperson Registration Number"]=''
data["Salesperson Estate Agent Name"]=''
#data.head()
url='https://www.cea.gov.sg/public-register?category=Salesperson&mobile='
for index, row in data.iterrows():
	if ' ' in str(row['Contact']):
		lst=row['Contact'].split(' ')
		print(lst)
		for fnumber in lst:
			url_mobile=url+fnumber
			print(url_mobile)
			html=urllib.request.urlopen(url_mobile).read()
	#print(html)
			tables_data = pd.read_html(html,header=0)
			print(tables_data)
			tables_data_df = tables_data[0]
			no_rows=tables_data_df['Salesperson Name'].count()
			print(no_rows)
			if no_rows == 1:
				data.loc[index,'Salesperson Name']=tables_data_df.loc[0]['Salesperson Name'].replace('&AMP;', ' & ')
				data.loc[index,'Salesperson Registration Number']=tables_data_df.loc[0]['Salesperson Registration Number'].replace('&AMP;', ' & ')
				data.loc[index,'Salesperson Estate Agent Name']=tables_data_df.loc[0]['Salesperson Estate Agent Name'].replace('&AMP;', ' & ')
				break
		print(data.loc[index])

		#fnumber=row['Contact'].split(' ',1)[0]
	else:
     # access data using column names
		fnumber=row['Contact']
	print(fnumber)
	url_mobile=url+fnumber
	print(url_mobile)
	html=urllib.request.urlopen(url_mobile).read()
	#print(html)
	tables_data = pd.read_html(html,header=0)
	print(tables_data)
	tables_data_df = tables_data[0]
	no_rows=tables_data_df['Salesperson Name'].count()
	print(no_rows)
	if no_rows == 1:
		data.loc[index,'Salesperson Name']=tables_data_df.loc[0]['Salesperson Name'].replace('&AMP;', ' & ')
		data.loc[index,'Salesperson Registration Number']=tables_data_df.loc[0]['Salesperson Registration Number'].replace('&AMP;', ' & ')
		data.loc[index,'Salesperson Estate Agent Name']=tables_data_df.loc[0]['Salesperson Estate Agent Name'].replace('&AMP;', ' & ')
	print(data.loc[index])
    

now = datetime.datetime.now()
date = now.strftime("%d%B%Y")
print(date)
data.to_csv (r'new_stc_{}.csv'.format(date), index = None, header=True)
         

