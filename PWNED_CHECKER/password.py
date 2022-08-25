import sys
import requests
import hashlib


def ft_request_api_data(hashed_char):
    url = 'https://api.pwnedpasswords.com/range/' + str(hashed_char)
    api_response = requests.get(url)
    if api_response.status_code != 200:
        raise RuntimeError(
            f'Error fetching:{api_response.status_code}, try again')
    return api_response


def ft_passwd_details(api_response, hash_to_check):
    hashes = (line.split(':')for line in api_response.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def ft_check_api(password):
    sha1passwd = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    api_pass, tail = sha1passwd[:5], sha1passwd[5:]
    api_response = ft_request_api_data(api_pass)

    return ft_passwd_details(api_response, tail)


def main(passwords):
    for passwd in passwords:
        count = ft_check_api(passwd)
        if count == 0:
            print('Few! This passwd has not been pawned')
        else:
            print(f'This passwd has been pawned {count} times')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
