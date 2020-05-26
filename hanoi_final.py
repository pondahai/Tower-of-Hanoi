#產生演算法
def hanoi(n, a, b, c):
    if n == 1:
        return [(a, c)]
    else:
        return hanoi(n-1, a, c, b) + hanoi(1, a, b, c) + hanoi(n-1, b, a, c)

#使用者輸入盤子數目
n = input("請輸入整數：")
#製作柱子變數 
poles=[list(range(1,int(n)+1)),[],[]]
#印出柱子初始狀態
print(poles)
#運算並列舉出演算法結果
for move in hanoi(int(n), '1', '2', '3'):
    #逐步顯示演算法結果
    print("盤由柱 %c 移至柱 %c" % move)
    #根據結果對柱子產生動作
    poles[int(move[1])-1].insert(0,poles[int(move[0])-1].pop(0))
    #將柱子狀態印出
    print(poles)
    
