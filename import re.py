import re

text = "Email: user@example.com, support@domain.org, contact@company.net"
emails = re.findall(r"\w+@\w+\.[a-zA-Z0-9]{2,3}", text)
if emails:
    print("Найденные email-адреса:", emails)
else:
    print("Email-адреса не найдены")
