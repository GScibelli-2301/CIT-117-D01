import pickle
import os

def main():
#Stored planets dict
    dictPlanetWeights = {
        'Mercury:': 0.38,
        'Venus:': 0.91,
        'our Moon:': 0.165,
        'Mars:': 0.38,
        'Jupiter:': 2.34,
        'Saturn:': 0.93,
        'Uranus:': 0.92,
        'Neptune:': 1.12,
        'Pluto:': 0.066
    }

    sFilename = "bcPlanetaryWeights.db"
 
    dictPlanetHistory = {}
    try:
        if os.path.exists(sFilename):
            with open(sFilename, 'rb') as file:
                dictPlanetHistory = pickle.load(file)
    except Exception as e:
        print(f"Error loading history: {e}")

    sViewHistory = input("Would you like to see the history? (Y/N): ").strip().lower()
    if sViewHistory == 'y':
        for sName, weights in dictPlanetHistory.items():
            print(f"{sName}: {weights}")

    while True:
        sPersonName = input("Enter your name (or blank to exit): ").strip()
        if not sPersonName:
            break


        if any(sName.lower() == sPersonName.lower() for sName in dictPlanetHistory.keys()):
            print("Name already exists. Please enter a unique name.")
            continue
#prompt weight
        while True:
            try:
                fEarthWeight = float(input("Enter your weight on Earth: "))
                break  
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        dictPersonWeights = {}

        for sPlanet, fGravityFactor in dictPlanetWeights.items():
            fPlanetWeight = fEarthWeight * fGravityFactor
            dictPersonWeights[sPlanet] = fPlanetWeight
#Show weight
        print(f"{sPersonName}, here are your weights in the Solar System's planets:")
        for sPlanet, fWeight in dictPersonWeights.items():
           
            print(f"Weight on {sPlanet:<10} {fWeight:10.2f}")

        dictPlanetHistory[sPersonName] = dictPersonWeights

    with open(sFilename, 'wb') as file:
        pickle.dump(dictPlanetHistory, file)

if __name__ == "__main__":
    main()
