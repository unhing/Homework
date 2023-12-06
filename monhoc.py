A = ["TOÁN", "LÝ", "HÓA"]
B = ["SIN", "TOÁ", "HÓ"]
C = ["VĂN", "SỬ", "ĐỊA"]
D = ["ANH", "TOÁN", "VĂN"]
name = ["A","B","C","D"]    # để lấy tên
khoi = [A,B,C,D]

def inputgrade(name):
    A = []
    for i in range(len(name)):
        subject = float(input("- Nhập điểm " + name[i] + ": "))
        A.append(subject)
    return A


def total(khoi):
    answer = khoi[0] * 2 + khoi[1] + khoi[2]
    return answer


def position(final):
    maxvalue = final[0]
    pos = 0
    for i in range(len(final)):
        if final[i] > maxvalue:
            maxvalue = final[i]
            pos = i
    return pos


lst = []
final = []
for i in range(len(khoi)):
    print("\nNhập điểm khối",name[i])
    lst.append(inputgrade(khoi[i])) # list điểm của 1 khối
    print("Tổng điểm 3 môn là:",total(lst[i]))
    final.append(total(lst[i]))     # list tổng điểm các khối

print(lst)
print(final)
print("\nBạn nên thi khối", name[position(final)], "vì bạn có tổng điểm cao nhất là", max(final))