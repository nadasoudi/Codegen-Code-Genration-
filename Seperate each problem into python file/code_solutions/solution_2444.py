def solution(email):
    email = email.split('@')
    if email[1].find('.')!= -1:
        return email[1].split('.')[0]
    else:
        return email[0]

print(solution("john.doe@company.com"))
print(solution("john.doe2001@