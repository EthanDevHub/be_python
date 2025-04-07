print("[Exercise 1]")
print("========================================================================")
print("Create a Wi-Fi configuration file - wifi_settings.conf (method_1)")
# method 1
file = open("./wifi_settings.conf", mode="w", encoding="utf-8")
file.write("SSID_2G = home_guest_24g\nWPAPSK_2G = 12345678\n")
file.close()


print("\n")
print("[Exercise 2]")
print("========================================================================")
print("Create a Wi-Fi configuration file - wifi_settings.conf (method_2)")
# method 2
#write
with open("./wifi_settings.conf", mode="a", encoding="utf-8") as file:
    file.write("SSID_5G = home_guest_5g\nWPAPSK_5G = 87654321\n")

# read
with open("./wifi_settings.conf", mode="r", encoding="utf-8") as file:
    data = file.read()
    print(f"Content of wifi_settings.conf is:\n{data}")


print("\n")
print("[Exercise 3]")
print("========================================================================")
print("Read a file and calculate the sum in the file")
with open("./scores.txt", mode="w", encoding="utf-8") as file:
    file.write("90\n89\n九十二\n95\n79\n")

total = 0
with open("./scores.txt", mode="r", encoding="utf-8") as file:
    # Get all content. (The typeof data is string)
    data = file.read()          # the fp will be moved to the tail.
    print(f"data = \n{data}")

    # Covert all content as list type, each element in list is a line in file.
    file.seek(0)                # move fp back to the head
    line = file.readlines()     # read all content and retuen a list (fp will be moved to the tail)
    print(f"line = {line}")

    # Use a for loop to read each line from the file and assign it to the variable 'score'
    file.seek(0)                # move fp back to the head
    for score in file:
        try:
            total += int(score.strip())  # strip() helps remove '\n' or spaces...
        except ValueError:
            print(f"Skip invalid score: {score.strip()}")

print(f"The total score in scores.txt = {total}")


print("\n")
print("[Exercise 4]")
print("========================================================================")
print("Load a JSON file")
import json

# load
with open("./config.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)

print(f"data = {data}")
print(f"name = {data['name']}")
print(f"version = {data['version']}")
print(f"release_date = {data['release_date']}")

# modify
data["version"] = "1.0.3"
with open("./config.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file)