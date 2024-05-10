import psycopg2
import os
from datetime import date
import time

# Menunggu database siap
while True:
    try:
        conn = psycopg2.connect(
            host="db",
            database="Customers",
            user="postgres",
            password=os.environ.get("POSTGRES_PASSWORD", "default_password")
        )
        conn.close()
        break
    except psycopg2.OperationalError:
        print("Database tidak tersedia, menunggu 5 detik...")
        time.sleep(5)
        
# Membuat koneksi ke database
conn = psycopg2.connect(
    host="db",
    database="Customers",
    user="postgres",
    password=os.environ.get("POSTGRES_PASSWORD","default_password")
)
cur = conn.cursor()

# Melakukan ETL
cur.execute("SELECT * FROM customers")
data = cur.fetchall()

# Membuat tabel baru untuk menyimpan data hasil transformasi
cur.execute("""
    CREATE TABLE transformed_customers (
        customer_id SERIAL PRIMARY KEY,
        gender VARCHAR(10),
        age INTEGER,
        annual_income NUMERIC,
        spending_score INTEGER,
        profession VARCHAR(50),
        work_experience NUMERIC,
        family_size INTEGER,
        income_category VARCHAR(20),
        age_group VARCHAR(20),
        load_date DATE
    )
""")

# Menyimpan data hasil transformasi ke tabel baru
for row in data:
    customer_id, gender, age, annual_income, spending_score, profession, work_experience, family_size = row
    income_category = 'High' if annual_income >= 100000 else 'Low'
    
    # Menentukan age_group berdasarkan rentang umur
    if age < 18:
        age_group = 'Minor'
    elif age < 30:
        age_group = 'Youth'
    elif age < 50:
        age_group = 'Adult'
    else:
        age_group = 'Senior'
    
    # Mengubah format tanggal
    load_date = date.today().strftime('%Y-%m-%d')
    
    cur.execute("""
        INSERT INTO transformed_customers (gender, age, annual_income, spending_score, profession, work_experience, family_size, income_category, age_group, load_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (gender, age, annual_income, spending_score, profession, work_experience, family_size, income_category, age_group, load_date))

conn.commit()
cur.close()
conn.close()