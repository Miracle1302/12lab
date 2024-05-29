import json


def load_data(filename):
    """ Load data from a JSON file. """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"data": []}


def save_data(filename, data):
    """ Save data to a JSON file. """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def display_data(data):
    """ Display the contents of the JSON file. """
    print(json.dumps(data, indent=4))


def add_record(data, day, precipitation, temperature):
    """ Add a new record to the JSON file. """
    data["data"].append({"day": day, "precipitation": precipitation, "temperature": temperature})
    return data


def delete_record(data, day):
    """ Delete a record by specified day. """
    data["data"] = [record for record in data["data"] if record["day"] != day]
    return data


def find_record(data, day):
    """ Find data in the JSON file by day. """
    for record in data["data"]:
        if record["day"] == day:
            return record
    return None


def classify_precipitation(data):
    """ Determine the amount of precipitation in the form of snow and rain. """
    snow = 0
    rain = 0
    for record in data["data"]:
        if record["temperature"] > 0:
            rain += record["precipitation"]
        else:
            snow += record["precipitation"]
    return {"snow": snow, "rain": rain}


def main():
    filename = "weather_data.json"
    data = load_data(filename)

    while True:
        print("\nAvailable options:")
        print("1. Display data")
        print("2. Add record")
        print("3. Delete record")
        print("4. Find record")
        print("5. Classify precipitation")
        print("6. Exit")

        choice = input("Enter the option number: ")

        if choice == "1":
            display_data(data)
        elif choice == "2":
            day = int(input("Day: "))
            precipitation = int(input("Precipitation (mm): "))
            temperature = int(input("Temperature (°C): "))
            data = add_record(data, day, precipitation, temperature)
            save_data(filename, data)
        elif choice == "3":
            day = int(input("Day to delete: "))
            data = delete_record(data, day)
            save_data(filename, data)
        elif choice == "4":
            day = int(input("Day to find: "))
            record = find_record(data, day)
            if record:
                print("Record:", record)
            else:
                print("Record not found.")
        elif choice == "5":
            result = classify_precipitation(data)
            print("Snow: {} mm, Rain: {} mm".format(result["snow"], result["rain"]))
            save_data("classified_precipitation.json", result)
        elif choice == "6":
            break
        else:
            print("Unknown option, please try again.")


if __name__ == "__main__":
    main()

