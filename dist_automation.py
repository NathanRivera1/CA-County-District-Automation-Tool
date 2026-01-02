# District List Declarations
distOne = ["Del Norte", "Humboldt", "Eureka", "Mendocino", "Lake"]
distTwo = ["Siskiyou", "Modoc", "Lassen", "Shasta", "Trinity", "Tehama", "Plumas"]
distThree = ["Glenn", "Butte Sierra", "Colusa", "Yuba", "Nevada", "Sutter", "Placer", "El Dorado", "Sacramento", "Yolo"]
distFour = ["Sonoma", "Napa", "Marin", "Solano", "Contra Costa", "Alameda", "Santa Clara"]
distFive = ["San Benito", "Monterey", "Santa Barbara", "San Luis Obispo"]
distSix = ["Madera", "Fresno", "Tulare", "Kings", "Kern"]
distSeven = ["Ventura", "Los Angeles"]
distEight = ["San Bernardino", "Riverside"]
distNine = ["Inyo", "Mono"]
distTen = ["Alpine", "Amador", "Calaveras", "San Joaquin", "Tuolumne", "Mariposa", "Merced", "Stanislaus"]
distEleven = ["San Diego", "Imperia"]
distTwelve = ["Orange"]

# User Input String Validation
while True:
    countyInput = input("Enter a California county: ")

    try: 
        countyInput = int(countyInput)
        print("Invalid Input")
        print()

    except ValueError:
        break

# Finding the District Number of User's County Input
if countyInput in distOne:
    print(f"{countyInput} belongs in district 01")

if countyInput in distTwo:
    print(f"{countyInput} is in district 02")

if countyInput in distThree:
    print(f"{countyInput} is in district 03")

if countyInput in distFour:
    print(f"{countyInput} is in district 04")

if countyInput in distFive:
    print(f"{countyInput} is in district 05")

if countyInput in distSix:
    print(f"{countyInput} is in district 06")

if countyInput in distSeven:
    print(f"{countyInput} is in district 07")

if countyInput in distEight:
    print(f"{countyInput} is in district 08")

if countyInput in distNine:
    print(f"{countyInput} is in district 09")

if countyInput in distTen:
    print(f"{countyInput} is in district 10")

if countyInput in distEleven:
    print(f"{countyInput} is in district 11")

if countyInput in distTwelve:
    print(f"{countyInput} is in district 12")
    