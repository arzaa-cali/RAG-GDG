import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load the variables from .env into the system environment
load_dotenv()

# 2. Retrieve the key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found. Check your .env file.")
else:
    # 3. Configure and test
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-flash-latest')
    
    try:
        response = model.generate_content("Give me a one-sentence fun fact about space.")
        print(f"Success! Response: {response.text}")
    except Exception as e:
        print(f"Validation failed: {e}")
