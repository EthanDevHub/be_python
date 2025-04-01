print("[Exercise 1]")
print("========================================================================")
print("Create a Wi-Fi configuration file - wifi_settings.conf (method_1)")
# method 1
file = open("/home/ethan/be_python/proj_file_control/wifi_settings.conf", mode="w", encoding="utf-8")
file.write("SSID_2G = home_guest_24g\nWPAPSK_2G = 12345678\n")
file.close()


print("\n")
print("[Exercise 2]")
print("========================================================================")
print("Create a Wi-Fi configuration file - wifi_settings.conf (method_1)")
# method 2
#write
with open("/home/ethan/be_python/proj_file_control/wifi_settings.conf", mode="a", encoding="utf-8") as file:
    file.write("SSID_5G = home_guest_5g\nWPAPSK_5G = 87654321\n")

# read
with open("/home/ethan/be_python/proj_file_control/wifi_settings.conf", mode="r", encoding="utf-8") as file:
    print(f"{file.read()}")


print("\n")
print("[Exercise 3]")
print("========================================================================")
print("Read a file and calculate the sum in the file")
with open("/home/ethan/be_python/proj_file_control/scores.txt", mode="w", encoding="utf-8") as file:
    file.write("90\n89\n95\n79")

sum = 0
with open("/home/ethan/be_python/proj_file_control/scores.txt", mode="r", encoding="utf-8") as file:
    for score in file:
        sum += int(score)

print(f"The total score in scores.txt = {sum}")


print("\n")
print("[Exercise 4]")
print("========================================================================")
print("Load a JSON file")
import json

# load
with open("/home/ethan/be_python/proj_file_control/config.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)

print(f"data = {data}")
print(f"name = {data['name']}")
print(f"version = {data['version']}")
print(f"release_date = {data['release_date']}")

# modify
data["version"] = "1.0.3"
with open("/home/ethan/be_python/proj_geometry/config.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file)