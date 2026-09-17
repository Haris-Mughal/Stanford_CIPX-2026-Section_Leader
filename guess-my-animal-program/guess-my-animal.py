from animal import get_random_animal
from ai import call_gpt

def main():
    animal = get_random_animal()
    
    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")
    
    while True:
        question = input("Ask me a yes or no question: ")
        
        # Check if the user's input matches the secret animal name directlyy
        if question.strip().lower() == animal.lower():
            print("Correct!")
            break
            
        # Construct the prompt for GPT to evaluate the user's question..
        prompt = f"The secret animal is a {animal}. The user asks: '{question}'. Answer strictly with 'Yes.' or 'No.'"
        
        # Call the AI model and display the response..
        response = call_gpt(prompt)
        print(response)

if __name__ == "__main__":
    main()