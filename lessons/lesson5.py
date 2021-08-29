favorite_misician = ["ブルーノマーズ", "デュアリパ", "yama", "ヒゲダン"]

hawaii = (19.8968, 155.5828)
japan = (34.6432, 136.9976)

fruits = {
    "color": "purple", 
    "shape": "sphere", 
    "taste": "sweet"}

n = input("input color or shape or taste: ")

if n in fruits:
    print(fruits[n])
else:
    print("input color or shape or taste")

music_list = {
    "ブルーノマーズ" : ["24K magic", "Uptown Funk", "Tresure", "Gorolla"],
    "デュアリパ": ["Don't Start Now", "Levitating", "Break My Heat"],
    "yama": ["春を告げる", "麻痺", "あるいは映画のような", "A.M.3:21"]
}

#set関数は集合として使える。重複は要素から取り除かれる
s1 = set([1, 3, 5, 10])
s2 = set([4, 10, 20, 4])

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
#部分集合どうか
print(s1.issubset(s2))