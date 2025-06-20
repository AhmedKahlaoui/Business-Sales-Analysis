import pandas as pd 
from datetime import datetime
import re 

#Importing raw data
orders=pd.read_csv("../data/raw/Orders.csv", sep=';',usecols=range(5))
customers=pd.read_csv("../data/raw/Customers.csv", sep=';')
product=pd.read_csv("../data/raw/Product.csv", sep=';')



#Orders data cleaning
orders.columns = orders.columns.str.strip().str.lower().str.replace(" ", "_")
orders['order_date'] = pd.to_datetime(orders['order_date'],format='%d/%m/%Y') 
today = datetime.today().strftime('%d/%m/%Y')
print(orders[orders['order_date'] > today] ) 
orders = orders.groupby(['order_id', 'order_date', 'customer_id', 'product_id'], as_index=False)['quantity'].sum()
print(orders.info()) 

#Creating Time Dimension
time_dim = pd.DataFrame({
    'order_date': orders['order_date'],
    'day': orders['order_date'].dt.day_name(),                   # Extract the day
    'month_name': orders['order_date'].dt.month_name(),   # Extract the month name
    'year': orders['order_date'].dt.year                  # Extract the year
})

time_dim = time_dim.drop_duplicates(subset=['order_date'], keep='first')
print(time_dim.info())


#Customers data cleaning
customers.columns=customers.columns.str.strip().str.lower().str.replace(" ", "_")
customers = customers.dropna(subset=['customer_id']) 
customers['country']=customers['country'].str.upper().replace({'UNITED STATES':'US','UNITED KINGDOM':'UK','IRELAND':'IR'})
customers.fillna({'customer_name':'No name','email':'No email','phone_number':'No phone number'},inplace=True) 

def validate_phone_number(row): 
    phone_number = row['phone_number']
    country = row['country']
    if country == 'US':
        pattern = r'^\+1 \(\d{3}\) \d{3}-\d{4}$'
    elif country == 'UK':
        pattern = r'^\+44 \(\d{3}\) \d{3}-\d{4}$'
    elif country == 'IR':
        pattern = r'^\+353 \(\d{3}\) \d{3}-\d{4}$'
    else:
        return False
    return bool(re.match(pattern, phone_number))

customers['PhoneNumberValid'] = customers.apply(validate_phone_number, axis=1)
print(customers.info()) 


#Prouct data cleaning
product.columns=product.columns.str.strip().str.lower().str.replace(" ", "_")
cols_to_float=['size','unit_price','price_per_100g','profit'] 
product[cols_to_float]=product[cols_to_float].apply(lambda x: x.str.replace(',', '.').astype(float)) 
print(product.info())

#Joining data
full_df=orders.merge(customers,on='customer_id',how='inner') \
              .merge(product,on='product_id',how="inner") \
              .merge(time_dim,on='order_date',how="inner")

print(full_df.head())

#Saving new datasets
  #to csv
orders.to_csv("../data/cleaned/order_cleaned.csv",index=False)
customers.to_csv("../data/cleaned/customers_cleaned.csv",index=False)
product.to_csv("../data/cleaned/product_cleaned.csv",index=False)
time_dim.to_csv("../data/cleaned/time_dim.csv",index=False)
full_df.to_csv("../data/joined/joined_data.csv",index=False)
  #to excel
with pd.ExcelWriter('../data/joined/joined_data.xlsx') as writer:
    orders.to_excel(writer, sheet_name='Orders', index=False)
    customers.to_excel(writer, sheet_name='Customers', index=False)
    product.to_excel(writer, sheet_name='Products', index=False)
    time_dim.to_excel(writer,sheet_name='Time', index=False)





    