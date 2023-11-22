from django.core.exceptions import ValidationError
import re

# Custom Validators
# validate_name_format: Only accepts string in the following format "First M. Last"
# Validation Error: 'Name must be in the format "First Middle Initial. Last"'
# validate_school_email: Only accepts string ending with "@school.com"
# Validation Error: 'Invalid school email format. Please use an email ending with "@school.com".'
# validate_combination_format: Only accepts string in the following format "12-12-12" (Ensures there are numbers only)
# Validation Error: 'Combination must be in the format "12-12-12"'

def validate_combination_format(combination):
    error_message = 'Combination must be in the format "12-12-12"'
    regex = r'^\d{2}-\d{2}-\d{2}$'
    good_combination = re.match(regex, combination)
    if good_combination:
        return combination
    else:
        raise ValidationError(error_message, params={ 'combination' : combination})

def validate_school_email(email):
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'
    regex = r'^.*@school\.com$'

    valid_email = re.match(regex, email)
    if valid_email:
        return email
    else:
        raise ValidationError(error_message, params= { 'email' : email })

def validate_name_format(name):
    error_message = 'Name must be in the format "First Middle Initial. Last"'
    regex = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'

    valid_name = re.match(regex, name)
    if valid_name:
        return name
    else:
        raise ValidationError(error_message, params= { 'name' : name })