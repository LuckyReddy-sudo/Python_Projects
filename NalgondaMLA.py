candidates = ['Lucky', 'Hinduja', 'Sandeep', 'Jagadeshwar', 'NOTA']

vote = input("Enter the MLA Choice: ")

match vote:
    case 'Lucky':
        print("Lucky is your MLA")
    case 'Hinduja':
        print("Hinduja is your MLA")
    case 'Sandeep':
        print("Sandeep is your MLA")
    case 'Jagadeshwar':
        print("Jaggu is your MLA")
    case 'NOTA':
        print("NOTA")
    case _:
        print(f'{vote} is your MLA')


