import requests ,json ,time
import mysql.connector

# bin_num="44317890"


def get_binlist(bin_num):

	all_record=[]

	try:
		headers = {'Accept-Version': '3'}
		respose=requests.get('https://lookup.binlist.net/'+bin_num, headers=headers)
		# print(respose.json())
		time.sleep(2)
		j_reponse=respose.json()

		try:
			c_shema=j_reponse['scheme']
		except Exception as e:
			c_shema=""

		try:
			c_type=j_reponse['type']
		except Exception as e:
			c_type=""

		try:
			c_brand=j_reponse['brand']
		except Exception as e:
			c_brand=""
		
		try:
			c_prepaid=j_reponse['prepaid']
		except Exception as e:
			c_prepaid=""
		
		try:
			c_bank_name=j_reponse['bank']['name']
		except Exception as e:
			c_bank_name=""

		try:
			c_country=j_reponse['country']['alpha2']
		except Exception as e:
			c_country=""

		try:
			c_country_name=j_reponse['country']['name']
		except Exception as e:
			c_country_name=""

		
		try:
			c_currency=j_reponse['country']['currency']
		except Exception as e:
			c_currency=""

		all_record+=[bin_num,c_shema,c_type,c_brand,c_prepaid,c_bank_name , c_country_name,c_country,c_currency]

		# print(bin_num,c_shema,c_type,c_brand,c_prepaid,c_bank_name , c_country_name,c_country,c_currency)
		# print(all_record)
	except Exception as e:
		print(str(e))

	return all_record





def check_connect_mysql():
	print(" CHECK SQL  CONNECTION       : ",end='',flush=True)
	try:
		mydb = mysql.connector.connect(host="127.0.0.1",user="cicada3301",passwd="binpass",database="all_bin")
		mycursor = mydb.cursor()
		print("MYSQL CONNECTED OK ")
		time.sleep(2)
		#return mycursor
	except  Exception as e :
		#print("FIELED")
		print(" SQL ERROR CONNECTION        : "+str(e)+" ",end='',flush=True)
		# fix_mysql(str(e))


# | Id | BIN  | scheme_c | Type | Brand | prepaid_c | Bank | Country | Country_Code | Currency |


def insert_to_db(aal_arry):

	mydb = mysql.connector.connect(host="127.0.0.1",user="cicada3301",passwd="binpass",database="all_bin")
	mycursor = mydb.cursor()

	sql = "INSERT INTO ta_bin (BIN, scheme_c,Type,Brand,prepaid_c,Bank,Country,Country_Code ,Currency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = (aal_arry[0], aal_arry[1],aal_arry[2], aal_arry[3],aal_arry[4], aal_arry[5],aal_arry[6], aal_arry[7],aal_arry[8])
	mycursor.execute(sql, val)
	time.sleep(2)

	mydb.commit()



























for binn in range(400000,499999):
	aal_arry=[]
	check_connect_mysql()
	aal_arry=get_binlist(str(binn))
	print(aal_arry)
	try:
		insert_to_db(aal_arry)
	except:
		print("passs")
