from barrierimplement import Circle
from barrierimplement import Rectangle
from barrierimplement import DrawingEngine

# 创建绘图引擎
engine = DrawingEngine()

# 创建圆形和矩形对象
circle = Circle(0, 0, 5)
rectangle = Rectangle(2, 2, 4, 3)

# 使用绘图引擎绘制图形
engine.draw_shape(circle)
engine.draw_shape(rectangle)

