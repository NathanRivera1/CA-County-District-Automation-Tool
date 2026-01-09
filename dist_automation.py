# District List Declarations
distOne = ["DEL NORTE", "HUMBOLDT", "EUREKA", "MENDOCINO", "LAKE"]
distTwo = ["SISKIYOU", "MODOC", "LASSEN", "SHASTA", "TRINITY", "TEHAMA", "PLUMAS"]
distThree = ["GLENN", "BUTTE", "SIERRA" "COLUSA", "YUBA", "NEVADA", "SUTTER", "PLACER", "EL DORADO", "SACRAMENTO", "YOLO"]
distFour = ["SONOMA", "NAPA", "MARIN", "SOLANO", "CONTRA COSTA", "ALAMEDA", "SANTA CLARA", "SAN MATEO"]
distFive = ["SANTA CRUZ", "SAN BENITO", "MONTEREY", "SANTA BARBARA", "SAN LUIS OBISPO"]
distSix = ["MADERA", "FRESNO", "TULARE", "KINGS", "KERN"]
distSeven = ["VENTURA", "LOS ANGELES"]
distEight = ["SAN BERNARDINO", "RIVERSIDE"]
distNine = ["INYO", "MONO"]
distTen = ["ALPINE", "AMADOR", "CALAVERAS", "SAN JOAQUIN", "TUOLUMNE", "MARIPOSA", "MERCED", "STANISLAUS"]
distEleven = ["SAN DIEGO", "IMPERIAL"]
distTwelve = ["ORANGE"]


# User Input String Validation
while True:
    countyInput = input("Enter a California county: ").upper()

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
    print(f"{countyInput} is in district 06, BE AWARE THAT CERTAIN ROUTES GET CODED TO DISTRICT 09")

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
