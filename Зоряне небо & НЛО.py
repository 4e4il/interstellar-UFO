#космос - зоряне небо & НЛО 
from turtle import * # Імпортуємо модуль  turtle для малювання графіки
from random import * # Імпортуємо всі функції з бібліотеки random для генерації випадкових значень
setup(500,500) #розмір вікна
bgcolor ("black") #колір фону

a=Turtle() # a-створили об'єкт зірка
a.hideturtle()  #сховали виконавця
a.color("blue") #колір зірки
a.width(2) #ширина лінії
a.speed(3) #швидкість побудови зірок


b=Turtle()  # b-створили об'єкт НЛО
b.shape("circle") #виконавець коло
b.up()  #підняли перо

#random зорі
for turn in range(100): # тривалість проекту
  for _ in range( 3 ): #кількість послідовних зірок
    a.up() #підняти перо
    a.goto(randint( -250, 250 ),randint( -250, 250 ) ) #координати зірки
    a.down() #опустити перо
    L = randint( 1, 10 ) #довжина променя 
    for luch in range( 8 ): #кількість променів
        a.forward( L ) #довжина променя 
        a.backward( L ) #довжина променя 
        a.right( 45 )#кут повороту
        
# НЛО  

  colors=['red','green','orange','blue'] # додамо кольорів в  НЛО
  b.speed(1)
  for x in range(4):
      b.color(colors[x%4]) #[x%4] індекс елемента списку 
      b.circle(randint( 1, 50 ))
      b.left(randint(0,360))# Генерація випадкового кута та відстані
      b.forward(randint(1,300))
      y=b.xcor() #повератємо НЛО коли воно вилетіло за межі
      x=b.ycor()
      if x>500 or y>500 or x>-500 or y>-500: 
          b.goto(randint( -250, 250 ),randint( -250, 250 ) )
          
mainloop()  # Запускаємо головний цикл для утримання вікна відображення
