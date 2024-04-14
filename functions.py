def get_student_dict(firstname, lastname, semester=1):
    return {
        'firstname': firstname,
        'lastname': lastname,
        'semester': semester
    }

def kwary(**kwargs):
    for k, v in kwargs.items():
        print(k, " -> ", v)

if __name__ == "__main__":
    print(get_student_dict('Maria', 'Hill'))
    print(kwary(one=1, chudy=True, niski=True, size=150))
