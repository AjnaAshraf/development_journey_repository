#pip install google-genai  - to connect gemini and python

from google import genai
from mysql import connector

connection = connector.connect(

    username = "root",
    password = "Password@123",
    database = "customer_support_db",
    host = "localhost"
)

cursor = connection.cursor()

query = "select * from supportticket where id = 3"

cursor.execute(query)

ticket = cursor.fetchone()

# print(ticket)

GEMINI_API_KEY = "abc"

client = genai.Client(api_key = GEMINI_API_KEY) #authenticate

prompt = f"""
You are a customer support ticket analysis system.

Analyze the following support ticket.

Customer Name:
{ticket[1]}

Subject:
{ticket[3]}

Description:
{ticket[4]}

Provide the following information:

1. Category
2. Priority
3. Sentiment
4. Summary
5. Suggested response

Category must be one of:

payment
delivery
account
technical
refund
other

Priority must be one of:

low
medium
high
urgent

Sentiment must be one of:

positive
neutral
negative

Return the answer in a clear format."""

response = client.models.generate_content(

    model="gemini-3.5-flash",

    contents=prompt

)

print(response)

