my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing

elit. Mauris vulputate lacus id eros consequat tempus.

Nam viverra velit sit amet lorem lobortis, at tincidunt

nunc ultricies. Duis facilisis ultrices lacus, id

tiger123@email.cz auctor massa molestie at. Nunc tristique

fringilla congue. Donec ante diam cnn@info.com, dapibus

lacinia vulputate vitae, ullamcorper in justo. Maecenas

massa purus, ultricies a dictum ut, dapibus vitae massa.

Cras abc@gmail.com vel libero felis. In augue elit, porttitor

nec molestie quis, auctor a quam. Quisque b2b@money.fr

pretium dolor et tempor feugiat. Morbi libero lectus,

porttitor eu mi sed, luctus lacinia risus. Maecenas posuere

leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam

erat volutpat. Donec eleifend felis at leo ullamcorper cursus.

Pellentesque id dui viverra, auctor enim ut, fringilla est.

Maecenas gravida turpis nec ultrices aliquet.

'''


def format_text(text):
    splitted = text.split()
    emails = []
    for word in splitted:
        if "@" in word:
            email = word.strip(".,:!?")
            emails.append(email)
    return emails

def get_numeric(emails):
    numerics = []
    for email in emails:
        if has_number(email):
            numerics.append(email)
    return numerics

def get_domains(emails):
    domains = []
    for email in emails:
        domains.append(email.split("@")[1])
    return domains

def has_number(string):
    for num in range(10):
        if str(num) in string:
            return True
    return False

def main(default=my_str):
    result = {
        "emails with nums": None,
        "domains": None
    }

    default = format_text(default)

    result["emails with nums"] = get_numeric(default)
    result["domains"] = get_domains(default)

    print(result)
    return result

main()