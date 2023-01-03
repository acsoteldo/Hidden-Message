def extract(text):
  # Split the text into words
  words = text.split()
  
  # Initialize an empty string for the hidden message
  message = ""
  
  # Iterate over the words
  for i, word in enumerate(words):
    # If the index of the word is a multiple of 5, add the first letter of the word to the message
    if (i + 1) % 5 == 0:
      message += word[0]
  
  # Return the hidden message
  return message
  
hidden_message = extract("Yesterday I saw an aardvark while walking my pet tortoise, Frank. What a sight this was! Aarvarks are nocturnal animals appearing in daylight with caution. Make sure to bring kippers when you visit.")
print(hidden_message)
