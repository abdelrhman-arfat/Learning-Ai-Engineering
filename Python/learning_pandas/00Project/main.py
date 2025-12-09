import pandas as pd
import os

df = pd.read_csv(
    r"C:\Users\COMPUMARTS\OneDrive\Desktop\AI enginnering\Python\learning_pandas\00Project\csv\sales_data.csv", encoding="latin1")

# Your first task is get all sales data in the date of 2002-2005 in custom files

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
df['SALES'] = df['QUANTITYORDERED'] * df['PRICEEACH']

output_dir = r"C:\Users\COMPUMARTS\OneDrive\Desktop\AI enginnering\Python\learning_pandas\00Project\json"
os.makedirs(output_dir, exist_ok=True)

wantedYears = [i + 2003 for i in range(4)]

for y in wantedYears:
    df_year = df[df['ORDERDATE'].dt.year == y]
    df_year = df_year[['ORDERNUMBER', 'STATUS', 'QUANTITYORDERED', 'PRICEEACH',
                      'PRODUCTCODE', 'PRODUCTLINE', 'PHONE', 'ADDRESSLINE1', 'SALES']]
    df_year.to_json(
        os.path.join(output_dir, f'sales_data_{y}.json'),
        orient='records',
        indent=4
    )
# now make a data_time file that will provide the more data about the order :
json_data = df.groupby("STATUS").agg(
    status_name=("STATUS", 'first'),
    order_count=("ORDERNUMBER", 'count'),
    total_quantity=('QUANTITYORDERED', 'sum'),
    total_sales=("SALES", 'sum')
)

json_data.to_json(
    os.path.join(output_dir, 'status_data.json'),
    orient='records',
    indent=4
)

json_product_grouped_data = df.groupby("PRODUCTLINE").agg(
    product_line=("PRODUCTLINE", 'first'),
    total_orders=("ORDERNUMBER", 'count'),
    total_quantity=("QUANTITYORDERED", 'sum'),
    total_sales=("SALES", 'sum')
)

json_product_grouped_data.to_json(
    os.path.join(output_dir, 'product_data.json'),
    orient='records',
    indent=4
)


print("columns of the data: \n", df.columns)
print("===========================")
print("information about the data: \n", df.info())
print("===========================")
print("description of the data: \n", df.describe())
