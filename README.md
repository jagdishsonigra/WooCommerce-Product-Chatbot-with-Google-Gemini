# WooCommerce-Product-Chatbot-with-Google-Gemini
This project implements a chatbot that interacts with users to provide product details from a WooCommerce store. The chatbot is powered by Google Gemini (Generative AI), and it helps customers find the right products by providing product names, prices, descriptions, and links to the products.
Features
Fetches product data from a WooCommerce store via its REST API.
Uses Google Gemini API to generate conversational responses based on user queries.
Provides product details such as name, price, and description.
Offers links to product pages. 
Responds politely and provides product recommendations, guiding users according to their preferences (e.g., budget, use case).
Handles queries like "Tell me about jackets," "What are your best-selling shoes?" or "I want something cheap."
Gracefully informs the user if the requested product is unavailable and suggests similar products if possible.
Prerequisites
Before you begin, ensure you have the following:

A Google Gemini API key for generating AI-based responses.
Access to a WooCommerce store and WooCommerce REST API credentials (Consumer Key and Consumer Secret).
Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/jagdishsonigra/WooCommerce-Product-Chatbot-with-Google-Gemini.git
cd WooCommerce-Product-Chatbot-with-Google-Gemini

3. Install required dependencies
You can use pip to install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Where requirements.txt should include the following:

Copy code
google-generativeai
woocommerce
3. Configuration
Google Gemini API Key: Replace the API_KEY placeholder with your actual Google Gemini API key.
WooCommerce API Credentials: Replace the following placeholders with your actual WooCommerce store details:
store_link: Your WooCommerce store URL.
consumer_key: Your WooCommerce API consumer key.
consumer_secret: Your WooCommerce API consumer secret.
These can be found or generated in your WooCommerce admin panel under Settings > Advanced > REST API.

4. Run the Chatbot
After setting up your API credentials, you can start the chatbot:

bash
Copy code
python chatbot.py
The chatbot will fetch product data from your WooCommerce store and be ready to interact with users. It will continue running until you type "exit" or "quit."

Example Queries
"Tell me about jackets."
"What are your best-selling shoes?"
"Do you have waterproof jackets?"
"I want something cheap."
If a product is unavailable, the chatbot will inform the user politely and, if possible, recommend a similar product from the same category.

Usage
Once the bot is running, you can interact with it by typing product-related queries. The bot will:

Provide product names, descriptions, and prices.
Share links to product pages.
Offer polite responses if the product is unavailable and suggest similar products.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Google Gemini API: For generating intelligent and conversational responses.
WooCommerce API: For fetching product data from the store.
