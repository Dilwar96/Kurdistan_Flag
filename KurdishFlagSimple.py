import turtle
import math

def draw_kurdish_flag():
    # إعداد النافذة
    window = turtle.Screen()
    window.title("العلم الكوردي مع الشمس ذات 21 شعاعًا - الإصدار المعدل")
    window.setup(width=800, height=500)
    window.bgcolor("white")
    
    # الألوان الأساسية للعلم
    colors = ["red", "white", "green"]
    stripe_height = 500 / 3  # ارتفاع كل شريط
    
    # رسم الأشرطة الأفقية مع تغطية كاملة للمنطقة الصفراء
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    
    for i, color in enumerate(colors):
        pen.color(color)
        pen.begin_fill()
        pen.goto(-400, 250 - (i * stripe_height))
        pen.pendown()
        pen.forward(800)
        pen.right(90)
        pen.forward(stripe_height)
        pen.right(90)
        pen.forward(800)
        pen.right(90)
        pen.forward(stripe_height)
        pen.right(90)
        pen.end_fill()
        pen.penup()
    
    # رسم الشمس المركزية (بدون خلفية بيضاء)
    sun_radius = stripe_height * 0.8
    pen.goto(0, -sun_radius)
    pen.color("yellow")
    pen.begin_fill()
    pen.circle(sun_radius)
    pen.end_fill()
    
    # رسم الأشعة (21 شعاعًا) فوق الخلفية الصفراء
    pen.color("yellow")
    pen.pensize(6)  # زيادة سمك الأشعة
    
    rays = 21
    ray_length = sun_radius * 1.5
    inner_ray_length = sun_radius * 0.7  # تقليل المسافة من المركز
    
    for i in range(rays):
        angle = i * (360 / rays)
        radian_angle = math.radians(angle)
        
        x_start = inner_ray_length * math.sin(radian_angle)
        y_start = inner_ray_length * math.cos(radian_angle)
        x_end = ray_length * math.sin(radian_angle)
        y_end = ray_length * math.cos(radian_angle)
        
        pen.penup()
        pen.goto(x_start, y_start)
        pen.pendown()
        pen.goto(x_end, y_end)
    
    
    pen.penup()
    pen.goto(0, -240)
    pen.color("black")
    pen.write("Kurdistan", align="center", font=("Arial", 24, "bold"))
    
    pen.hideturtle()
    turtle.done()

draw_kurdish_flag()