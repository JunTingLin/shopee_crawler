import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def on_pie_click(event):
    # 在這裡處理圓餅圖的點擊事件
    # 可以根據點擊的位置和數據做相對應的處理
    # 在這個例子中，當點擊圓餅圖時，打印出相應的點擊位置座標
    print(f"Clicked at x={event.x}, y={event.y}")

    # 在這裡添加跳轉到其他畫面的處理代碼

def show_pie_chart():
    # 創建圓餅圖的數據
    data = [25, 35, 20, 10, 10]
    labels = ['A', 'B', 'C', 'D', 'E']

    # 繪製圓餅圖
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.pie(data, labels=labels, autopct='%1.1f%%')
    ax.set_title('Pie Chart')

    # 綁定點擊事件
    canvas = FigureCanvasTkAgg(fig, master=pie_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# 創建Tkinter窗口
root = tk.Tk()
root.geometry("500x500")

# 創建四個並排按鈕
button_frame = tk.Frame(root)
button_frame.pack()
btn_pie_chart = tk.Button(button_frame, text="圓餅圖", command=show_pie_chart)
btn_pie_chart.pack(side=tk.LEFT, padx=10, pady=10)

# 創建顯示圓餅圖的Frame
pie_frame = tk.Frame(root)
pie_frame.pack()

root.mainloop()
