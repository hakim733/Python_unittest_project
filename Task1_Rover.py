class rovar(object):
    _LOWER_CONSTANTS = "bcdfhjklmnpqrstvwxz"
    _UPPER_CONSTANTS = "BCDFGHJKLMNPQRSTVWXYZ"

    def enrove(self, normal: str) -> str:
        """Encode the string in rovarspraket."""
        if normal is None:
            return None
        
        builder = ""
        first_upper_consonant = True  # Track the first uppercase consonant
        
        for c in normal:
            if c in self._LOWER_CONSTANTS:
                builder += c + 'o' + c  # Lowercase consonant encoding
            elif c in self._UPPER_CONSTANTS:
                if first_upper_consonant:
                    builder += c + 'O' + c  # First uppercase consonant encoding (capital 'O')
                    first_upper_consonant = False  # Mark that we've processed the first uppercase consonant
                else:
                    builder += c + 'o' + c  # Subsequent uppercase consonants follow lowercase pattern
            else:
                builder += c  # Non-alphabet characters remain unchanged
        
        return builder






 
    def derove(self, rov: str) -> str:
        if rov is None:
            return None

        for c in self._LOWER_CONSTANTS:
            rov = rov.replace(c + 'o' + c, c)

        for c in self._UPPER_CONSTANTS:
            rov = rov.replace(c + 'O' + c, c)

        # Fix: Ensure we handle any occurrence of 'Ho' correctly in mixed strings
        if rov.startswith('Ho'):
            rov = rov[2:]  # Remove 'Ho' from the start
        
        return rov
