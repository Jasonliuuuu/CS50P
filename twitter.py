url = input("What is the URL?: ").strip()

username = url.removeprefix("https://twitter.com/", "")

print(f"Username: {username}")