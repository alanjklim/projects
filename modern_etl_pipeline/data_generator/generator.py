import pandas as pd
from faker import Faker
import random

# Initialize Faker with locale for Australia
fake = Faker('en_AU')

# Variable for the number of customers to create
num_customers = 100

# List to store data
customers_data = []
accounts_data = []
transactions_data = []
events_data = []

# Common lists to simulate realistic account types, transaction types, and merchants
account_types = ['Transaction Account', 'Savings Account', 'Credit Card', 'Home Loan', 'Term Deposit']
transaction_types = ['Purchase', 'Withdrawal', 'Deposit', 'Transfer']
merchants = [
    'Woolworths', 'Coles', 'Kmart', 'JB Hi-Fi', 'BP Petrol', 'Bunnings Warehouse', 
    'Amazon Australia', 'Uber Eats', 'Telstra', 'Optus', 'Australian Taxation Office'
]
devices = ['iPhone', 'Android Phone', 'Desktop PC', 'Laptop', 'iPad']

# Generate Customer and related Account, Transactions, Events data
for i in range(1, num_customers + 1):
    customer_id = i
    # Customer Information
    customer = {
        'customer_id': customer_id,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': f"{fake.first_name().lower()}.{fake.last_name().lower()}@example.com",
        'phone_number': fake.phone_number(),
        'address': fake.address(),
        'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=80),
        'created_at': fake.date_this_decade(),
        'occupation': fake.job()
    }
    customers_data.append(customer)
    
    # Generate Account Information (1-3 accounts per customer)
    num_accounts = random.randint(1, 3)
    for j in range(num_accounts):
        account_number = fake.unique.bban()  # Generates a realistic-looking bank account number
        account_type = random.choice(account_types)
        account_balance = round(random.uniform(500, 100000), 2)
        account_opened_at = fake.date_between(start_date=customer['created_at'], end_date='today')
        
        account = {
            'account_number': account_number,
            'customer_id': customer_id,
            'account_type': account_type,
            'balance': account_balance,
            'opened_at': account_opened_at,
            'branch_name': random.choice(['Sydney', 'Melbourne', 'Perth', 'Brisbane', 'Adelaide', 'Canberra'])
        }
        accounts_data.append(account)
        
        # Generate Transactions (10-50 per account, with realistic transaction amounts)
        num_transactions = random.randint(10, 50)
        for k in range(num_transactions):
            transaction = {
                'account_number': account_number,
                'transaction_date': fake.date_between(start_date=account['opened_at'], end_date='today'),
                'merchant': random.choice(merchants),
                'amount': round(random.uniform(-2000, 5000), 2),  # Negative for withdrawals/purchases, positive for deposits
                'transaction_type': random.choice(transaction_types),
                'transaction_location': random.choice(['Online', 'In-store', 'ATM', 'POS'])
            }
            transactions_data.append(transaction)
    
    # Generate Event Logs (5-15 per customer, with realistic devices and IPs)
    num_events = random.randint(5, 15)
    for l in range(num_events):
        event = {
            'customer_id': customer_id,
            'event_date': fake.date_time_this_year(),
            'event_type': random.choice(['Login', 'Logout', 'Password Change', 'Fund Transfer']),
            'device': random.choice(devices),
            'ip_address': fake.ipv4_public()
        }
        events_data.append(event)

# Create DataFrames
customers_df = pd.DataFrame(customers_data)
accounts_df = pd.DataFrame(accounts_data)
transactions_df = pd.DataFrame(transactions_data)
events_df = pd.DataFrame(events_data)

# Save data to CSV
customers_df.to_csv('data/customers.csv', index=False)
accounts_df.to_csv('data/accounts.csv', index=False)
transactions_df.to_csv('data/transactions.csv', index=False)
events_df.to_csv('data/events.csv', index=False)