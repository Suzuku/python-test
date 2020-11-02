import re


def is_valid_email(addr):
    result = re.match(r'^[0-9a-zA-Z\_\.]+\@[0-9a-zA-Z]+\.com', addr)
    if result != None:
        return True
    else:
        return False


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
