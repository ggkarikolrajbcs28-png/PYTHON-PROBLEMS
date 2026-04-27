def get_hits_and_near_hits():
    # Get input from user
    code = input("Enter the secret code: ")
    guess = input("Enter your guess: ")

    hits = 0
    near_hits = 0

    # We use lists to track which characters have already been 'used'
    code_list = list(code)
    guess_list = list(guess)

    # Step 1: Find Hits
    # We must mark hits first so they aren't double-counted as near hits
    hit_indices = []
    for i in range(len(code_list)):
        if i < len(guess_list) and code_list[i] == guess_list[i]:
            hits += 1
            hit_indices.append(i)

    # Mark hit positions as None so they aren't used for Near Hits
    for i in hit_indices:
        code_list[i] = None
        guess_list[i] = None

    # Step 2: Find Near Hits
    # Check remaining guess digits against remaining code digits
    for i in range(len(guess_list)):
        if guess_list[i] is not None: # Skip hits
            if guess_list[i] in code_list:
                near_hits += 1
                # Remove the digit from code_list so it can't be matched again
                code_list[code_list.index(guess_list[i])] = None

    print(f"Output: {hits}H{near_hits}N")

# Run the function
get_hits_and_near_hits()
