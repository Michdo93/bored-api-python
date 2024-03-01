import requests

class BoredAPI(object):
    def __init__(self):
        self.BASE_URL = "http://www.boredapi.com/api/activity/"

        self.__min_accessibility = 0.0
        self.__max_accessibility = 1.0

        self.__types = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]

        self.__min_participants = 0
        self.__max_participants = 100

        self.__min_price = 0
        self.__max_price = 1

        self.__min_key = 1000000
        self.__max_key = 9999999

    def __floatingPointConversion(self, value):
        return int(value * 10) / 10.0
    
    def get_activity(self, accessibility=None, min_accessibility=None, max_accessibility=None, type=None, participants=None, price=None, min_price=None, max_price=None, key=None):
        url = self.BASE_URL

        if accessibility is not None and self.__min_accessibility <= accessibility <= self.__max_accessibility and isinstance(accessibility, float):
            url += "?accessibility={}".format(accessibility)
        else:
            if accessibility is not None:
                if not isinstance(accessibility, float):
                    print("The accessbility argument {} is not a float!".format(accessibility))
                elif self.__min_accessibility > accessibility:
                    print("The accessbility argument {} is lower than the minimum of {}!".format(accessibility, self.__min_accessibility))
                elif accessibility > self.__max_accessibility:
                    print("The accessbility argument {} is higher than the maximum of {}!".format(accessibility, self.__max_accessibility))

        if min_accessibility is not None and max_accessibility is not None and self.__min_accessibility <= min_accessibility and self.__max_accessibility >= max_accessibility and isinstance(min_accessibility, float) and isinstance(max_accessibility, float):
            if "?" in url:
                url += "&minaccessibility={}&maxaccessibility={}".format(min_accessibility, max_accessibility)
            else:
                url += "?minaccessibility={}&maxaccessibility={}".format(min_accessibility, max_accessibility)
        else:
            if min_accessibility is not None:
                if not isinstance(min_accessibility, float):
                    print("The min_accessibility argument {} is not a float!".format(min_accessibility))
                elif not isinstance(max_accessibility, float):
                    print("The max_accessibility argument {} is not a float!".format(max_accessibility))
                elif self.__min_accessibility > min_accessibility:
                    print("The min_accessibility argument {} is lower than the minimum of {}!".format(min_accessibility, self.__min_accessibility))
                elif min_accessibility > self.__max_accessibility:
                    print("The min_accessibility argument {} is higher than the maximum of {}!".format(min_accessibility, self.__max_accessibility))
                elif self.__min_accessibility > min_accessibility:
                    print("The max_accessibility argument {} is lower than the minimum of {}!".format(max_accessibility, self.__min_accessibility))
                elif max_accessibility > self.__max_accessibility:
                    print("The max_accessibility argument {} is higher than the maximum of {}!".format(max_accessibility, self.__max_accessibility))

        if type is not None and type in self.__types:
            if "?" in url:
                url += "&type={}".format(type)
            else:
                url += "?type={}".format(type)
        else:
            if type is not None:
                if type not in self.__types:
                    print("The type argument {} is not in the list of available types {}!".format(type, self.__types))

        if participants is not None and self.__min_participants <= participants <= self.__max_participants and isinstance(participants, int):
            if "?" in url:
                url += "&participants={}".format(participants)
            else:
                url += "?participants={}".format(participants)
        else:
            if participants is not None:
                if not isinstance(participants, int):
                    print("The participants argument {} is not an integer!".format(participants))
                elif self.__min_participants > participants:
                    print("The participants argument {} is lower than the minimum of {}!".format(participants, self.__min_participants))
                elif participants > self.__max_participants:
                    print("The participants argument {} is higher than the maximum of {}!".format(participants, self.__max_participants))

        if price is not None and self.__min_price <= price <= self.__max_price and isinstance(price, int):
            if "?" in url:
                url += "&price={}".format(price)
            else:
                url += "?price={}".format(price)
        else:
            if price is not None:
                if not isinstance(price, int):
                    print("The price argument {} is not an integer!".format(price))
                elif self.__min_price > price:
                    print("The price argument {} is lower than the minimum of {}!".format(price, self.__min_price))
                elif price > self.__max_price:
                    print("The price argument {} is higher than the maximum of {}!".format(price, self.__max_price))

        if min_price is not None and max_price is not None and self.__min_price <= min_price and self.__max_price >= max_price and isinstance(min_price, int) and isinstance(max_price, int):
            if "?" in url:
                url += "&minprice={}&maxprice={}".format(min_price, max_price)
            else:
                url += "?minprice={}&maxprice={}".format(min_price, max_price)
        else:
            if min_price is not None and max_price is not None:
                if not isinstance(min_price, int):
                    print("The min_price argument {} is not a int!".format(min_price))
                elif not isinstance(max_price, int):
                    print("The max_price argument {} is not a int!".format(max_price))
                elif self.__min_price > min_price:
                    print("The min_price argument {} is lower than the minimum of {}!".format(min_price, self.__min_price))
                elif min_price > self.__max_price:
                    print("The min_price argument {} is higher than the maximum of {}!".format(min_price, self.__max_price))
                elif self.__min_price > min_price:
                    print("The max_price argument {} is lower than the minimum of {}!".format(max_price, self.__min_price))
                elif max_price > self.__max_price:
                    print("The max_price argument {} is higher than the maximum of {}!".format(max_price, self.__max_price))

        if key is not None and self.__min_key <= key <= self.__max_key and isinstance(key, int):
            if "?" in url:
                url += "&key={}".format(key)
            else:
                url += "?key={}".format(key)
        else:
            if key is not None:
                if not isinstance(key, int):
                    print("The key argument {} is not an integer!".format(key))
                elif self.__min_key > key:
                    print("The key argument {} is lower than the minimum of {}!".format(key, self.__min_key))
                elif key > self.__max_key:
                    print("The key argument {} is higher than the maximum of {}!".format(key, self.__max_key))

        try:
            response = requests.get(url, timeout=8)
            response.raise_for_status()

            if response.ok or response.status_code == 200:
                return response.json()
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    def get_random_activity(self):
        return self.get_activity()
    
    def get_random_activities(self):
        activities = {}
        for activity_type in self.__types:
            activities[activity_type] = self.get_activity(type=activity_type)

        return activities

    def get_activity_by_key(self, key):
        return self.get_activity(key=key)

    def get_activity_by_type(self, activity_type):
        return self.get_activity(type=activity_type)

    def get_activity_by_participants(self, participants):
        return self.get_activity(participants=participants)

    def get_activity_by_price(self, price):
        return self.get_activity(price=price)

    def get_activity_by_price_range(self, min_price, max_price):
        return self.get_activity(min_price=min_price, max_price=max_price)

    def get_activity_by_accessibility(self, accessibility):
        return self.get_activity(accessibility=accessibility)

    def get_activity_by_accessibility_range(self, min_accessibility, max_accessibility):
        return self.get_activity(min_accessibility=min_accessibility, max_accessibility=max_accessibility)

if __name__ == "__main__":
    # Erstelle eine Instanz der BoredAPI-Klasse
    bored_api = BoredAPI()

    print(bored_api.get_random_activity())
    print(bored_api.get_random_activities())

    """
    # Teste verschiedene Szenarien
    print("Test 1: Gültige Aktivität abrufen")
    print(bored_api.get_random_activity())

    print("\nTest 2: Aktivität mit bestimmtem Typ abrufen")
    print(bored_api.get_activity_by_type("recreational"))

    print("\nTest 3: Aktivität mit bestimmter Anzahl von Teilnehmern abrufen")
    print(bored_api.get_activity_by_participants(2))

    print("\nTest 4: Aktivität mit bestimmtem Preis abrufen")
    print(bored_api.get_activity_by_price(0))

    print("\nTest 5: Aktivität mit bestimmter Zugänglichkeit abrufen")
    print(bored_api.get_activity_by_accessibility(0.5))

    print("\nTest 6: Aktivität mit bestimmtem Schlüssel abrufen")
    print(bored_api.get_activity_by_key(1234567))

    print("\nTest 7: Aktivität mit benutzerdefinierten Parametern abrufen")
    print(bored_api.get_activity(
        accessibility=0.3,
        type="diy",
        participants=1,
        price=0.2,
        key=9876543
    ))

    print("\nTest 8: Fehlerhafte Parameter testen")
    print(bored_api.get_activity_by_price("invalid"))  # Sollte einen Fehler auslösen
    print(bored_api.get_activity_by_type("invalid_type"))  # Sollte einen Fehler auslösen
    print(bored_api.get_activity_by_participants("invalid"))  # Sollte einen Fehler auslösen
    print(bored_api.get_activity_by_accessibility("invalid"))  # Sollte einen Fehler auslösen
    print(bored_api.get_activity_by_key("invalid"))  # Sollte einen Fehler auslösen

    print("\nTest 9: Fehler bei Aktivitätsabruf behandeln")
    print(bored_api.get_activity_by_key(99999999))  # Sollte einen Fehler beim Abrufen einer nicht existierenden Aktivität auslösen

    print("\nTest 10: Gültige Aktivität im Preisspektrum abrufen")
    print(bored_api.get_activity_by_price_range(0, 0.5))
    """
