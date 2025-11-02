

temp_str = input("Enter temperature in Celsius: ")
temp = float(temp_str)

if temp <= 10:
    print("wear a heavy jacket")

elif temp <= 18:
    print("wear a light jacket or pull-over.")

elif temp <= 30:
    print("wear a long-sleeve shirt or a thin cardigan/sweater.")

elif temp > 30:
    print("wear a light t-shirt and shorts/light trousers.")
