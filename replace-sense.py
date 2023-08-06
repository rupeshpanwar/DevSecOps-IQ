import re
import random
import string

def random_string(length=32):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def random_digits(length=8):
    """Generate a random digits of fixed length."""
    return ''.join(random.choice(string.digits) for i in range(length))

def mask_sensitive_info(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

        # Replace account numbers (assuming they're sequences of 8-16 digits)
        content = re.sub(r'\b\d{8,16}\b', random_digits(8), content)

        # Replace secret keys (assuming they're alphanumeric strings of 32 characters)
        content = re.sub(r'\b[A-Za-z0-9]{32}\b', random_string(), content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    mask_sensitive_info('pages/conversation.html')
