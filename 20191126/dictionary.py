phone = {"조세림" : "010-1234-5678", "김예슬" : "010-2345-3456"}
print(phone["조세림"])
phone["김도한"] = "010-2344-2345"
print(phone)
print(type(phone))

phonelist = ["010-2344-2333", "010-2342-2345"]
nameList = ["조세림, 김예슬"]
print(nameList[0] + "번호는 : " + phonelist[0])


# Dictionary의 Key는 int, float, string, tuple이 가능하다.
tupleList = {("조세림", "학동"): "010-1234-5678"}
print(tupleList[("조세림", "학동")])
serim = tupleList.get(("조세림", "학동"))
print(serim)

# Dictionary 만드는 방법 2.
# dict 함수는 key가 string일지라도 따옴표를 붙이지 않는다.
dictionary = dict(조세림 = "010-2234-2345", 김예슬 = "010-2342-5534")
print(dictionary)

is_serim_exist = "조세림" in dictionary
print(is_serim_exist)

if "조세림" in dictionary:
    print("조세리미 있습니다.")
else:
    print("조세림이 없습니다.")


