import requests

credit_card_number = input("Enter your credit card number: ")
expire_date = input("Enter your expiration date (MM/YY): ")
cvv = input("Enter your CVV code: ")

payload = {
    "cardnumber": credit_card_number,
    "exp-date": expire_date,
    "cvc": cvv
}

response = requests.post("https://checkout.stripe.com/c/pay/cs_live_a1cXLyjRUQTpkU6yQkHLAJE9k1ppzSNkF414xBYaefbilCsVJ5NiANb91k#fidkdWxOYHwnPyd1blppbHNgWkJpXElMcWQzUm90RER2NFRjNnRIb1c3bjU1d3NGNjJGfXEnKSdobGF2Jz9%2BJ2JwbGEnPydLRCcpJ2hwbGEnPydLRCcpJ3ZsYSc%2FJ0tEJ3gpJ2dgcWR2Jz9eWCknaWR8anBxUXx1YCc%2FJ3Zsa2JpYFpscWBoJyknd2BjYHd3YHdKd2xibGsnPydtcXF1dj8qKm9wbGZ8dmh2K2ZqaCd4JSUl", data=payload)

if response.status_code == 200:
    print("Payment successful!")
else:
    print("Payment failed. Error code:", response.status_code)
