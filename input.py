# inputで取得した値はstrになる
a = input("numerator:")
b = input("denominator:")

# 割り算
def divided(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        # 例外処理
        return "zero !!"

# 結果出力
print(divided(int(a), int(b)))

# global変数
g = 0

# scope のテスト
def scope_1(x = 8):
    # これだとローカル変数 g となる
    g = x

# scope のテスト
def scope_2(x = 8):
    # global 宣言することで global 変数として扱う
    global g
    g = x

# 引数を指定しないとデフォルトで x＝8 となる
scope_1()
# scope_1 はローカル変数の変更のみなので g = 0 のまま
print("g = ", g)

# 引数を指定しないとデフォルトで x＝8 となる
scope_2(10)
# scope_2 global 変数を変更するので g == 10
print("g = ", g)
