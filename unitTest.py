from getGenPass import generatePasswordString

def isgeneratePasswordString_generates_string():
    gen_pass_string = generatePasswordString(12, 10)
    assert type(gen_pass_string) == str, "Should be String"

def isgeneratePasswordString_generate_12_digit_password():
    gen_pass_string = generatePasswordString(12, 10)
    assert len(gen_pass_string) == 12, "Password must have 12 length"


if __name__ == '__main__':
    isgeneratePasswordString_generates_string()
    isgeneratePasswordString_generate_12_digit_password()
    print("Everything Passed")
    


