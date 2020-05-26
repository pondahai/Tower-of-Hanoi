#產生演算法並顯示過程
def hanoi(n, a, b, c,poles):
    if n == 1:
        print("步驟： 盤由柱 %c 移至柱 %c" % (a,c))
        poles[int(c)-1].insert(0,poles[int(a)-1].pop(0))
        print('結果： ', poles)
        print()
        
    else:
        hanoi(n-1, a, c, b,poles)
        hanoi(1, a, b, c,poles)
        hanoi(n-1, b, a, c,poles)

#使用者輸入盤子數目
n = input("請輸入整數：")
#製作柱子變數 
poles=[list(range(1,int(n)+1)),[],[]]
#印出柱子初始狀態
print(poles)
print()
#運算並列舉出演算法結果
hanoi(int(n), '1', '2', '3',poles)
print('完成')
