import webbrowser
import geocoder

def main():
    # webbrowser.open("http://google.com")
    print(geocoder.ip('me').latlng)


if __name__ == "__main__":
    main()
    pass