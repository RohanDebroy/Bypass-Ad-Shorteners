# Bypass Ad Shorteners

Hi, This is just a simple python wrapper for [Auto Link Bypasser](https://chrome.google.com/webstore/detail/auto-link-bypasser/doiagnjlaingkmdjlbfalakpnphfmnoh) chrome extension by Yu Yumari.

# Supported Url

At the time of writing this, here are the[supported domains](https://gist.github.com/RohanDebroy/db439cf742950244b200b8a09de68373)

Update 1: 
-   Yuumari removed ouo.io and other similar domains for free users. Read more [here](https://yuumari.com/ex/alb/#information)
-   You can find the new list of supported domains [here](https://yuumari.com/ex/alb/#domains)

# Dependencies

1. Python 3
2. Request
3. Shortened Urls :)

# Usage

```
from bypassadshorteners import recursive_bypass_url, bypass_url


def main():
    //Adf.ly shortened url
    url = "http://fumacrom.com/1u0t"

    print(f'{"*" * 5} Started Bypassing {"*" * 5}')
    extended_url = bypass_url(url)
    print(extended_url)
    print(f'{"*" * 5} Bypass completed {"*" * 5}')

    print(f'{"*" * 5} Started Bypassing Recursively {"*" * 5}')
    extended_url = recursive_bypass_url(url)
    print(extended_url)
    print(f'{"*" * 5} Recursive Bypass completed {"*" * 5}')


if __name__ == '__main__':
    main()

```

# Credits

[Yuumari](https://yuumari.com/) for his chrome extension. He also has an api which is paid and tbh I don't have enough to pay.

# Desclaimer

For educational use only.

# License

GNU GPL v3
