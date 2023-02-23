def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False




def reverse(string):
    return string == string[::-1]


def palindrome3(string):
    string = string.lower()
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False

        start += 1
        end -= 1

    return True