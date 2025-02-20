"""Orange France."""

from lib.providers.abstract_orange_provider import AbstractOrangeProvider


class OrangeFranceProvider(AbstractOrangeProvider):
    """Orange France provider."""

    def __init__(self):
        """Initialize Orange France provider."""
        self.mco = "OFR"
        self.groups = {
            "TNT": [192, 4, 80, 34, 47, 118, 111, 445, 119, 195, 446, 444, 234, 78, 481, 226, 458, 482, 1404, 1401]
            + [1403, 1402, 1400, 1399, 112, 2111],
            "Mini-généralistes": [205, 191, 145, 115, 225],
            "Premium": [3505, 3501, 35, 3779, 3349, 33, 1563, 3347, 3348, 1290, 1304, 1335, 282],
            "Cinéma": [1562, 2072, 185, 10, 284, 283, 401, 285, 287, 1190],
            "Divertissement": [128, 1960, 5, 2752, 87, 1167, 54, 2326, 49],
            "Jeunesse": [2803, 321, 928, 3738, 229, 32, 888, 473, 2065, 1746, 58, 299, 300, 344, 197, 293],
            "Découverte": [3561, 1072, 3360, 3106, 90115, 3155, 12, 2037, 38, 7, 88, 451, 829, 63, 508, 719, 147, 662]
            + [402],
            "Jeunes adultes": [2353, 2942, 121, 6, 2040, 1585],
            "Musique et spectacle vivant": [90150, 605, 2006, 2321, 1989, 453, 90159, 265, 90161, 90162, 90163, 90165]
            + [2958, 125, 907, 1353],
            "Sport": [64, 2837, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 15, 3629],
            "Jeux": [1061],
            "Société": [1996, 531, 90216, 3767, 57, 110, 90221],
            "Information française": [992, 90226, 529, 1073, 140, 90230, 90231],
            "Information internationale": [671, 90233, 53, 51, 410, 19, 525, 90239, 3413, 90242, 781, 830, 61, 90246]
            + [3562],
            "France 3 Régions": [1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 308, 1931, 1932, 1933, 1934]
            + [1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944],
        }
