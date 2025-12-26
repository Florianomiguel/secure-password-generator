import secrets
import string
import zxcvbn

def try_level(password_text):
    try:
        result = zxcvbn.zxcvbn(password_text)
        score = result['score'] 
    
        levels = {
            0: "Too weak 🔴",
            1: "Weak 🟠",
            2: "Medium 🟡",
            3: "Strong 🟢",
            4: "Super Strong 🛡️"
        } 
        print(f"Safety Level: {levels[score]}") 
        
        suggestions = result['feedback']['suggestions']
        if suggestions:
            print(f"Tip: {suggestions[0]}")
        return score
            
    except TypeError:
        print("Error: The function zxcvbn was called incorrectly or the password is not a string.")        
        return None

def generate_password(length):
    while True:
        try:
            # Characters used to generate the password
            alphabet = string.ascii_letters + string.digits + string.punctuation
            
            # Secure generation using secrets
            secure_password = ''.join(secrets.choice(alphabet) for _ in range(length))
            
            # Analyze the generated password
            try_level(secure_password)
            
            print("-" * 30)
            print(f"Your generated password is: \033[1;32m{secure_password}\033[0m")
            print("-" * 30)
            break          
            
        except (TypeError, ValueError):
            print('Please enter integers only for the length.')