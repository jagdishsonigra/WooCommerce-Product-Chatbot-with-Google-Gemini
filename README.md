# WooCommerce Product Chatbot with Google Gemini

This project implements a chatbot that interacts with users to provide product details from a WooCommerce store. The chatbot is powered by Google Gemini (Generative AI), and it helps customers find the right products by providing product names, prices, descriptions, and links to the products.

## Features

- Fetches product data from a WooCommerce store via its REST API.
- Uses Google Gemini API to generate conversational responses based on user queries.
- Provides product details such as name, price, and description.
- Offers links to product pages.
- Responds politely and provides product recommendations, guiding users according to their preferences (e.g., budget, use case).
- Handles queries like:
  - "Tell me about jackets."
  - "What are your best-selling shoes?"
  - "I want something cheap."
- Gracefully informs the user if the requested product is unavailable and suggests similar products if possible.

## Prerequisites

Before you begin, ensure you have the following:

1. A **Google Gemini API** key for generating AI-based responses.
2. Access to a **WooCommerce store** and **WooCommerce REST API credentials** (Consumer Key and Consumer Secret).

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jagdishsonigra/WooCommerce-Product-Chatbot-with-Google-Gemini.git
cd WooCommerce-Product-Chatbot-with-Google-Gemini
