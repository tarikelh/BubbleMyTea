import re

class is_valid:
    @staticmethod
    def email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return True if re.fullmatch(regex, email) else False

    @staticmethod
    def password(password):
        SpecialSym =['$', '@', '#', '%', '!']
        message = ''
        val = True
     
        if len(password) < 6:
            message = 'length should be at least 6'
            val = False
            
        if not any(char.isdigit() for char in password):
            message = 'Password should have at least one numeral'
            val = False
            
        if not any(char.isupper() for char in password):
            message = 'Password should have at least one uppercase letter'
            val = False
            
        if not any(char.islower() for char in password):
            message = 'Password should have at least one lowercase letter'
            val = False
            
        if not any(char in SpecialSym for char in password):
            message = 'Password should have at least one of the symbols $@#'
            val = False

        return { 'val': val, 'message': message }
