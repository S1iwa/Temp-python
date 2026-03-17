from src.functions import countMembers

def main():
    czlonkowieZero = []
    czlonkowieJeden = ["Miłosz Przybył"]

    print("Zero członków w zespole:")
    print(countMembers(czlonkowieZero))

    print("Jeden członek w zespole:")
    print(countMembers(czlonkowieJeden))

if __name__ == "__main__":
    main()