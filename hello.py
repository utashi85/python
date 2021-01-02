# 関数
def increment(x):
    return x + 1

# 初期化
i = 0
# loop や if 文のブロックは indent で表現
while i < 100:
    print(i, 'Hello, World!!')
    i = increment(i)
print('End')
# indent が異なる End は最後に一回だけ表示される