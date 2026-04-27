def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255 or (part != str(num)):
            return False
    return True
print("Type 'exit' to stop.")

while True:
    user_input = input("\nEnter an IP address to verify: ").strip()

    if user_input.lower() in [ 'exit']:
        print("Exiting...")
        break

    if is_valid_ip(user_input):
        print(f"It is a VALID IP address.")
    else:
        print(f"It is INVALID.")
