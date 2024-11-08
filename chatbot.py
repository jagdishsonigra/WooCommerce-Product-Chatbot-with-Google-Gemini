import json
import google.generativeai as genai
from woocommerce import API

# Initialize Google Gemini API (replace with your actual API key)
API_KEY = "Api key here"  # Replace this with your actual Gemini API key
genai.configure(api_key=API_KEY)

# Initialize WooCommerce API credentials
wcapi = API(
    url="store link",  # Replace with your WooCommerce store URL
    consumer_key="consumer key",  # Replace with your Consumer Key
    consumer_secret="secret key",  # Replace with your Consumer Secret
    version="wc/v3"
)

# Fetch all products from WooCommerce API
def fetch_products():
    response = wcapi.get("products", params={"per_page": 100})  # Adjust the 'per_page' value as needed
    if response.status_code == 200:
        products_data = response.json()
        valid_products = []
        for product in products_data:
            # Filter out placeholder products
            if "Import placeholder" not in product['name']:
                valid_product = {
                    "name": product['name'],
                    "price": product.get('price', ""),
                    "description": product.get('description', ""),
                    "permalink": product.get('permalink', "")
                }
                valid_products.append(valid_product)
        return valid_products
    else:
        print(f"Failed to fetch products. Status Code: {response.status_code}")
        return []

# Editable prompt for Gemini to act as a salesperson chatbot
editable_prompt = """
You are a helpful and friendly salesperson chatbot. When a customer asks about a product, you should respond by:
1. Providing the product name, price, and description.
2. Including a link to the product page which can be opened properly.
3. Offering more information if requested and guiding the customer.

you should be helpfull in guiding users according to thier budget liking or use case and your reply should be visually appealing so user likes to read it 
Here is a list of available products:

{product_data}

Use the product data provided above to answer any product-related questions. Be sure to give helpful, detailed, and polite responses, guiding the customer towards finding the best product for their needs.

Example user queries:
- "Tell me about jackets."
- "What are your best-selling shoes?"
- "Do you have waterproof jackets?"
- "i want something cheap"
if the product is not available give them a polite answer saying no and if possible recomend them similar product of same category or type which is available

dont suggest anything which is not available and dont keep responses too long 
"""

# Function to generate response using Google Gemini
def generate_response(user_query, product_data):
    # Replace the placeholder in the prompt with the actual product data
    product_data_json = json.dumps(product_data, indent=4)
    prompt = editable_prompt.replace("{product_data}", product_data_json) + f"\nUser query: {user_query}\nAnswer:"

    # Generate a response using the Google Gemini API
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Adjust if needed
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"

# Main chatbot function
def main():
    # Fetch products from WooCommerce
    products = fetch_products()
    
    if not products:
        print("No products found.")
        return
    
    # Start a simple chatbot interaction
    print("Welcome to the product chatbot! Ask me about any product.")
    
    while True:
        # Take user input
        user_query = input("\nYour question: ")
        
        if user_query.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        # Generate response using the entire product data and user query
        response = generate_response(user_query, products)
        
        # Output the chatbot's response
        print(f"Bot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()
