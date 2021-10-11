from bypassadshorteners import recursive_bypass_url, bypass_url


def main():
    # url = input("Enter the url to bypass : ")
    # bypass_url(url)
    url = "https://ouo.io/HOboAf"

    print(f'{"*" * 5} Started Bypassing {"*" * 5}')
    a = bypass_url(url)
    print(a)
    print(f'{"*" * 5} Bypass completed {"*" * 5}')

    print(f'{"*" * 5} Started Bypassing Recursively {"*" * 5}')
    a = recursive_bypass_url(url)
    print(a)
    print(f'{"*" * 5} Recursive Bypass completed {"*" * 5}')


if __name__ == '__main__':
    main()
