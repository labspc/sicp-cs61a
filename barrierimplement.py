# 任务：设计一个简单的图形绘制程序，绘制一个圆形和矩形
# Circle 和 Rectangle 类分别表示圆形和矩形，它们封装了各自的数据（坐标、尺寸等）和绘制方法
# 定义圆形类
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle at ({self.x}, {self.y}) with radius {self.radius}")

# 定义矩形类
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")

# 引入抽象屏障：绘图引擎
# 定义绘图引擎类：它的 draw_shape 方法接受一个形状对象，并调用该对象的 draw 方法进行绘制
class DrawingEngine:
    def draw_shape(self, shape):
        shape.draw()

if __name__ == '__main__':
    main()


