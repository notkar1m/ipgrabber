import requests as re
import sys, base64
try:
    if sys.argv[1].lower() == "new":
        url = sys.argv[2].lower()
        if url == "help":
            print("ipgrabber new https://example.com")
            print("    command^   Url ^")
        else:
            message = url
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print(base64_message)
            print(re.get(f"https://tricker.notkar1myt.repl.co/new-link-cmd_url={base64_message}").text)
    elif sys.argv[1].lower() == "old":
        code = sys.argv[2].lower()
        if code == "help":
            print("ipgrabber old 1234")
            print("   command^ Code ^")
        else:
            print(re.get(f"https://tricker.notkar1myt.repl.co/statics-cmd_code={code}").text)
    elif sys.argv[1].lower() == "help":
        print("Commands:\n\nipgrabber new https://example.com  :  ipgrabber [command] [url]\nipgrabber help\nipgrabber old 1234  :  ipgrabber [command] [code]")
    else:
        print(f"'{sys.argv[1]}' Not Found\nhelp For List Of Commands")
except:
    print("Commands:\n\nipgrabber new https://example.com  :  ipgrabber [command] [url]\nipgrabber help\nipgrabber old 1234  :  ipgrabber [command] [code]")
