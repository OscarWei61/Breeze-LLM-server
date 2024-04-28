from urllib.parse import quote
import requests

# Prompt the user to input the content for LLM inquiry
input_string = input("想詢問LLM的內容 : ")

# Encode the input string in a URL
encoded_string = quote(input_string, safe='')

# Construct the URL for making a GET request to the LLM server
# Remember to replace the IP address with the actual IP address of the server
server_ip = "http://202.5.255.35"
port = "5100"
api_endpoint = "/generate_text"
url = f"{server_ip}:{port}{api_endpoint}?input_string={encoded_string}"

# Send a GET request to the LLM server and store the response
response = requests.get(url)

# Extract the generated text from the JSON response
output_string = response.json()["result"]

# Print the generated text as the answer to the user's inquiry
print("Answer : ", output_string)