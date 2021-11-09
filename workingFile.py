def validate_password(password):
    def validate_length(password):
        if len(password)>=6:
            return True
        return False
    def validate_symbol(password):
        if "@" in password or "$" in password or "#" in password:
            return True
        return False
    def validate_lower(password):
        return any([True for x in password if "a"<=x<="z"])
    def validate_upper(password):
        return any([True for x in password if "A"<=x<="Z"])
    def validate_digit(password):
        return any([True for x in password if x.isnumeric()])
    return all([
        validate_length(password),
        validate_symbol(password),
        validate_lower(password),
        validate_upper(password),
        validate_digit(password)
    ])