def solution(phone_book):
    max=len(phone_book);
    for i in range(max):
        for j in range(i+1,max):
            if ((phone_book[i].find(phone_book[j])==0)|(phone_book[j].find(phone_book[i])==0)):
                return False;
    return True;

print(solution(["119", "97674223", "1195524421"]));