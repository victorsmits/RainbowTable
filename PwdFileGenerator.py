from passlib.hash import lmhash


def generator(list,path):
    file = open(path,"w+")
    for pwd in list:
        hash = [pwd,lmhash.hash(pwd)]
        file.write("{}\n".format(hash[1]))
    file.close()


list = ["didier", "password", "123456", "123456789", "12345678", "12345", "111111", "1234567", "sunshine", "qwerty",
        "iloveyou", "princess", "admin", "welcome", "666666", "abc123", "football", "123123", "monkey", "654321",
        "!@#$%^&*", "charlie", "aa123456", "donald", "password1", "qwerty123", "zxcvbnm", "121212", "bailey", "freedom",
        "shadow",
        "passw0rd", "baseball", "buster", "daniel", "hannah", "thomas", "summer", "george", "harley", "222222",
        "jessica", "ginger",
        "letmein", "abcdef", "solo", "jordan", "55555", "tigger", "joshua", "pepper", "sophie", "robert", "matthew",
        "12341234",
        "andrew", "lakers", "andrea", "1qaz2wsx", "starwars", "ferrari", "cheese", "computer", "corvette", "mercedes",
        "blahblah",
        "maverick", "hello", "nicole", "hunter", "amanda", "jennifer", "banana", "chelsea", "ranger", "trustno1",
        "merlin",
        "cookie", "ashley", "bandit", "killer", "aaaaaa", "1q2w3e", "zaq1zaq1", "hockey", "dallas", "whatever",
        "admin123", "pussy",
        "liverpool", "querty", "william", "soccer", "london", "biteme", "victor", "bruxelles", "azertyuiop",
        "ordinateur", "internet"]

generator(list,"mypassword.lst")