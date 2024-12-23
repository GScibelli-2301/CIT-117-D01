class Numerology:
    def __init__(self, sName, sDOB):
        self.name = sName
        self.dob = sDOB
        self.soul_number = None
        self.personality_number = None
        self.power_name_number = None
        self.life_path_number = None
        self.birthday_number = None
        self.attitude_number = None
    
    def _reduce_number(self, num):
        """Reduces a number to a single digit between 1 and 9."""
        while num > 9:
            num = sum(int(digit) for digit in str(num))
        return num

    def getName(self):
        return self.name

    def getBirthdate(self):
        return self.dob

    def getAttitude(self):
        """Computes Attitude Number: Birth Month + Birth Day"""
        
        month, day, year = map(int, self.dob.split('-'))
        attitude = month + day
        return self._reduce_number(attitude)

    def getBirthDay(self):
        """Computes Birthday Number: The sum of the digits of the day."""
        day = int(self.dob.split('-')[1])
        return self._reduce_number(day)

    def getLifePath(self):
        """Computes Life Path Number: The sum of all digits of the birthdate."""
        
        digits = [int(digit) for digit in self.dob.replace('-', '')]
        life_path = sum(digits)
        return self._reduce_number(life_path)
    
    def getSoul(self):
        """Computes Soul Number: Sum of the vowels in the name."""
        vowels = "aeiou"
        name = self.name.lower()
        soul_number = sum(self._letter_to_number(char) for char in name if char in vowels)
        return self._reduce_number(soul_number)
    
    def getPersonality(self):
        """Computes Personality Number: Sum of consonants in the name."""
        consonants = "bcdfghjklmnpqrstvwxyz"
        name = self.name.lower()
        personality_number = sum(self._letter_to_number(char) for char in name if char in consonants)
        return self._reduce_number(personality_number)

    def getPowerName(self):
        """Computes Power Name Number: Sum of Soul and Personality Numbers."""
        soul = self.getSoul()
        personality = self.getPersonality()
        power_name = soul + personality
        return self._reduce_number(power_name)

    def _letter_to_number(self, char):
        """Converts a letter to a corresponding number."""
        letter_map = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
            'h': 8, 'i': 9, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6,
            'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5,
            'x': 6, 'y': 7, 'z': 8
        }
        return letter_map.get(char, 0)  
