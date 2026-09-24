import ollama

print("My Chatbot")
print("Type exit to quit")

# Store conversation history
messages = []

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Add user's message to history
    messages.append({
        "role": "user",
        "content": question
    })

    # Send complete conversation history
    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    # Get bot's response
    answer = response["message"]["content"]

    print("Bot:", answer)

    # Add bot response to history
    messages.append({
        "role": "assistant",
        "content": answer
    })