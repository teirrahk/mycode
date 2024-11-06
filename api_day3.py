import requests
from pprint import pprint

def main():
    # API URL
    url = "https://aux1-7db214f2-7074-4400-abe0-2a5559030ea9.live.alta3.com/quotes"

    # Send GET request to retrieve all quotes
    response = requests.get(url)
    
    # Check if the GET request was successful
    if response.status_code == 200:
        quotes = response.json().get("quotes", [])
        print("Current quotes in the API:")
        pprint(quotes)

    else:
        print("Failed to retrieve quotes!")

    # TODO: Add code to send a POST request with a new quote
    getname = input("\nEnter name: \n>")
    getquote = input("\nEnter quote: \n>")

    new_quote = {"name": getname, "quote": getquote}

    post_newquote = requests.post(url, json=new_quote)

    if post_newquote.status_code == 201:
        print("Quote added successfully!")
    else:
        error = post_newquote.json().get("error", "Unknown error occurred!")
        print(f"Failed to add quote: {error}")



if __name__ == "__main__":
    main()
