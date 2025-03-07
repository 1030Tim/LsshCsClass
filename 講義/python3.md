---
marp: true
theme: default
paginate: true
title: Python 程式設計
author: 陳閔駿
style: |
  section {
    background-color: black;
    color: white;
  }
---

# Python 程式設計
## by.陳閔駿

---

# 🚀 學習目標  
- 學習 **Python** 的基本語法與邏輯  
- 交叉學習 **C++** 與 **Python**，減少知識落差  
- 透過 **實作解題** 強化應用能力  
- 培養程式設計思維，提高解決問題的能力  
- 學習如何撰寫高效且可讀性高的程式碼  

---

# 📖 章節大綱  
1. **Python 是什麼？**  
2. **基本運算與變數**  
3. **值的型別與資料結構**  
4. **條件判斷與迴圈**  
5. **函式與模組**  
6. **演算法入門與問題解決**  

---

# 🔧 使用工具  
- **IDE**：Python 3 / Visual Studio Code  
- **開發環境**：Windows / macOS / Linux  

---

## 🐍 Python 可以做什麼？  

----

強大的程式語言，應用廣泛包括但不限於：  
- ✅ **基本運算與自動化處理**  
- ✅ **物件導向程式設計**  
- ✅ **數據分析與視覺化**  
- ✅ **機器學習與人工智慧**  
- ✅ **網頁開發與後端應用**  
- ✅ **網路爬蟲與自動化測試**  

---

# ⚖ Python3 vs. C++  
| 特色           | Python3  | C++  |
|---------------|---------|------|
| **型別**      | 動態型別 | 強制型別 |
| **執行方式**  | 直譯執行 | 編譯執行 |
| **效能**      | 慢 (直譯) | 快 (編譯) |
| **學習難度** | 易學 | 需掌握指標與記憶體管理 |

---

## 📌 interpret vs. compiler  

- **直譯**：一行翻譯、一行執行，開發效率高  
- **編譯**：全部翻譯、全部執行，效能較高  

----


<img src="https://hackmd.io/_uploads/ByA5Lfu51l.png" width="700">



----

<img src="https://hackmd.io/_uploads/HJr8YMOqJg.png"
     width="800px">

----

中階語言 ->組合語言
![image](https://hackmd.io/_uploads/H12JqMdq1e.png)

----

機器語言
![image](https://hackmd.io/_uploads/rkfD5MO5yl.png)



---


# 📌 強制型 vs. 動態型  

### C++ (強制型)  
```cpp
#include<iostream>
using namespace std;
int main()
{
    int a = 5;
    float b = 7.0;
    char c = 'h';
    cout << a << "\n";
    cout << b << "\n";
    cout << c << "\n";
    return 0;
}
```

----

### Python3 （動態型）  
```python=
a = 5
b = 7.0
c = "Hello World"
print(a)
print(b)
print(c)
```

----

python幫你做好了很多的事情

---

# 環境安裝  

✅ 安裝 Python3：[Python 官方網站](https://www.python.org)  
✅ 安裝 VS Code：[Visual Studio Code 官方網站](https://code.visualstudio.com)  
Jupyter Notebook（線上）：


---

# ✅ 確認 Python 版本  
**Mac 用戶**：
```zsh
python3 --version
```
**Windows 用戶**：
```cmd
python --version
```

---


# 數值運算  

Python 提供強大的數值運算功能，例如：
```python=
x = 10
y = 3
print(x + y)  # 加法
print(x - y)  # 減法
print(x * y)  # 乘法
print(x / y)  # 除法（浮點數）
print(x // y) # 整數除法
print(x % y)  # 取餘數
print(x ** y) # 次方
```

----

## 程式在哪裡運行
1. 滑鼠
2. 鍵盤
3. CPU
4. 記憶體


----

## 程式在哪裡運行
1. 滑鼠
2. 鍵盤
3. CPU
4. <a style="color: red;">記憶體</a>


----

# 變數與賦值  
```python=
a = 5
```

>> `=` 不是數學中的等號，而是**賦值**，將右邊的數值 5 賦予給變數 `a`。

----

記憶體
![image](https://hackmd.io/_uploads/H1LA0fd91e.png)

----

assignment operator
```python=
a = 5
```

----

![image](https://hackmd.io/_uploads/rJgAtJm_q1l.png)


----

In C++ and other language

----

指標
```cpp=
signed main(){
    int x = 10;
    cout << &x << endl; 
}
```
輸出 0x16f8df0ec

---

# 進一步學習  
✅ **推薦資源**  
- Python 官方文件：[https://docs.python.org/3/](https://docs.python.org/3/)  
- W3Schools Python 教學：[https://www.w3schools.com/python/](https://www.w3schools.com/python/)  
- LeetCode 練習題：[https://leetcode.com/](https://leetcode.com/)  
- Kaggle 數據分析：[https://www.kaggle.com/](https://www.kaggle.com/)  

---
