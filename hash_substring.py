# python3

def read_input():
    input_type = input().rstrip()
    if input_type == 'F':
        with open('input.txt', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        pattern = input().rstrip()
        text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return occurrences
    
    prime = 1000000007
    x = 263
    p_hash = sum([ord(pattern[i]) * pow(x, i, prime) for i in range(p_len)]) % prime
    t_hash = sum([ord(text[i]) * pow(x, i, prime) for i in range(p_len)]) % prime
    x_p = pow(x, p_len - 1, prime)
    
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                occurrences.append(i)
        if i < t_len - p_len:
            t_hash = ((t_hash - ord(text[i]) * x_p) * x + ord(text[i+p_len])) % prime
    
    return occurrences



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))






