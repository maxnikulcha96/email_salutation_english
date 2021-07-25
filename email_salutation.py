academic_titles = ["Bc.", "Ing.", "Mgr.", "Ph.D.", "doc.", "prof.", "RNDr.", "CSc."]


def get_recipient_full_name_without_titles(recipient):
    recipient = recipient.replace(',', '')

    for title in academic_titles:
        if title in recipient:
            recipient = recipient.replace(title, '')

    return recipient.lstrip().rstrip()


def get_salutation(recipient):
    recipient_full_name_without_titles = get_recipient_full_name_without_titles(recipient)
    first_name, last_name = recipient_full_name_without_titles.split(' ', 1)

    if "prof." in recipient or "doc." in recipient:
        return "Dear professor {},".format(last_name)
    elif "Ph.D." in recipient:
        return "Dear Dr. {},".format(recipient_full_name_without_titles)
    else:
        return "Dear Ms./Mr. {},".format(last_name)


def main():
    recipient = input("Enter the recipient full name (including academic titles): ")

    salutation = get_salutation(recipient)
    print(salutation)


main()
