# Bypass Ad Shorteners

Hi, This is just a simple python wrapper for [Auto Link Bypasser](https://chrome.google.com/webstore/detail/auto-link-bypasser/doiagnjlaingkmdjlbfalakpnphfmnoh) chrome extension by yu yummari.

# Supported Url

At the time of writing this, here are the[supported domains](https://gist.github.com/RohanDebroy/db439cf742950244b200b8a09de68373)

# Dependencies

1. Python 3
2. Request
3. Shortened Urls :)

# Usage

```
from bypassadshorteners import recursive_bypass_url, bypass_url


def main():
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

```

# Credits

[Yu Yumari](https://yuumari.com/) for his chrome extension. He also has an api which is paid and tbh I don't have enough to pay.

# Desclaimer

For educational use only.

# License

GNU GPL v3
