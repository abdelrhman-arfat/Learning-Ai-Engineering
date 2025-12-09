# 🐼 NumPy & Pandas Practical Reference - AI / Data Engineering Focus

"""
This file is organized for learning AI, data cleaning, and embeddings.
Each section contains explanations in English and Arabic.
"""

```python
# Required Libraries
import numpy as np
import pandas as pd
import time
import os
```

---

## 1️⃣ Pandas Basics - Loading and Inspecting Data

# English: Load CSV files, inspect data, check columns, types, and summary statistics.

# Arabic: تحميل ملفات CSV، فحص البيانات، عرض الأعمدة وأنواعها والإحصاءات الأساسية.

```python
# Load CSV
df = pd.read_csv('sales_data.csv', encoding='latin1')

# Convert ORDERDATE to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

# Create a SALES column
df['SALES'] = df['QUANTITYORDERED'] * df['PRICEEACH']

# Inspect first rows
print(df.head())

# Show columns
print("Columns:", df.columns)

# Information
print(df.info())

# Descriptive statistics
print(df.describe())
```

**Explanation:**

* `.head()` shows first 5 rows.
* `.info()` shows types and missing values.
* `.describe()` gives count, mean, min, max, std.
* بالعربي: `.head()` أول 5 صفوف، `.info()` معلومات عن الأعمدة، `.describe()` احصاءات عامة.

---

## 2️⃣ Selecting Columns and Filtering Rows

# English: Access specific columns and filter rows based on conditions.

# Arabic: الوصول لأعمدة معينة وتصفيه الصفوف حسب شروط.

```python
# Select a single column
print(df['QUANTITYORDERED'])

# Filter by year 2003
df_2003 = df[df['ORDERDATE'].dt.year == 2003]
print(df_2003.head())

# Filter by multiple conditions (STATUS = 'Shipped' and SALES > 1000)
df_filtered = df[(df['STATUS'] == 'Shipped') & (df['SALES'] > 1000)]
print(df_filtered.head())
```

**Explanation:**

* Use `[]` for column selection.
* Use boolean conditions for filtering.
* بالعربي: `[]` لاختيار الأعمدة، شروط منطقية لتصفية البيانات.

---

## 3️⃣ Grouping and Aggregation

# English: Summarize data by grouping.

# Arabic: تلخيص البيانات بواسطة التجميع.

```python
# Group by STATUS
status_summary = df.groupby('STATUS').agg(
    order_count=('ORDERNUMBER', 'count'),
    total_quantity=('QUANTITYORDERED', 'sum'),
    total_sales=('SALES', 'sum')
)
print(status_summary)

# Group by PRODUCTLINE
product_summary = df.groupby('PRODUCTLINE').agg(
    total_orders=('ORDERNUMBER', 'count'),
    total_quantity=('QUANTITYORDERED', 'sum'),
    total_sales=('SALES', 'sum')
)
print(product_summary)
```

**Explanation:**

* `.groupby()` + `.agg()` to calculate counts and sums.
* بالعربي: `.groupby()` مع `.agg()` لحساب المجموعات والإجماليات.

---

## 4️⃣ Exporting Data to JSON

# English: Save filtered or aggregated data to JSON files.

# Arabic: حفظ البيانات المفلترة أو المجمعة في ملفات JSON.

```python
output_dir = './json'
os.makedirs(output_dir, exist_ok=True)

# Export year 2003 data
df_2003.to_json(os.path.join(output_dir, 'sales_data_2003.json'), orient='records', indent=4)

# Export aggregated status data
status_summary.to_json(os.path.join(output_dir, 'status_data.json'), orient='records', indent=4)
```

**Explanation:**

* `orient='records'` for list of dictionaries.
* `indent=4` for readable format.
* بالعربي: `orient='records'` لقائمة القواميس، `indent=4` لتنسيق قابل للقراءة.

---

## 5️⃣ Combining Pandas with Numpy for Calculations

# English: Use NumPy to perform fast element-wise calculations within pandas.

# Arabic: استخدام NumPy للقيام بحسابات سريعة لكل عنصر داخل pandas.

```python
# Calculate discount if quantity > 50
df['DISCOUNT'] = np.where(df['QUANTITYORDERED'] > 50, df['SALES']*0.1, 0)
print(df[['QUANTITYORDERED', 'SALES', 'DISCOUNT']].head())
```

**Explanation:**

* `np.where` acts like SQL CASE WHEN.
* بالعربي: `np.where` تعمل مثل شرط SQL CASE WHEN.

---

## 6️⃣ Merging / Joining DataFrames

# English: Combine multiple DataFrames using joins.

# Arabic: دمج عدة DataFrames باستخدام الانضمام (joins).

```python
# Example: Merge status summary with product summary (for illustration)
merged_df = pd.merge(status_summary.reset_index(), product_summary.reset_index(), how='outer', left_index=False, right_index=False)
print(merged_df.head())
```

**Explanation:**

* `.merge()` joins DataFrames on keys or indexes.
* بالعربي: `.merge()` يربط DataFrames حسب الأعمدة أو الفهارس.

---

This file now contains **everything a beginner/intermediate AI engineer needs for pandas and numpy**, with explanations in English and Arabic for reference. You can expand it later with visualization (Matplotlib/Seaborn) and AI embeddings.
