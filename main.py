#Задание 12.7.3


per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
sto = 100
# print(per_cent.values())  # dict_values([4.28, 4.0, 5.6, 5.9])
# print(per_cent.keys())  # dict_keys(['VTB', 'SBER', 'TKB', 'SKB'])
pr = (list(per_cent.values()))  # dict_values([5.9, 4.28, 5.6, 4.0])
# print(pr)  # [5.9, 4.28, 5.6, 4.0]

print("Bank :", " ".join(per_cent.keys()))
print("% year :", (pr[:]))

int_tugric = int(input("Money :"))
print("Bank :", "  ".join(per_cent.keys()))
s: int = 100
a_pr = (pr[0] / s)
b_pr = (pr[1] / s)
c_pr = (pr[2] / s)
d_pr = (pr[3] / s)
deposit = [round(int_tugric * a_pr), round(int_tugric * b_pr), round(int_tugric * c_pr), round(int_tugric * d_pr)]
print("Deposit :", round(int_tugric * a_pr), round(int_tugric * b_pr), round(int_tugric * c_pr),
      round(int_tugric * d_pr))
print("Max :", max(deposit))
