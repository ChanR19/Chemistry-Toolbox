import math

from TextBox import TextBox
from Button import Button
from Switch import Switch

class VectorDotProduct:
    x1 = TextBox(250,40,100,30,20)
    x2 = TextBox(250,110,100,30,20)
    y1 = TextBox(380,40,100,30,20)
    y2 = TextBox(380,110,100,30,20)
    button = Button(250,180,250,30,"Calculate",20)
    magnitude1 = 0
    magnitude2 = 0
    direction = 0
    dot_product = 0
    def update(self):
        #update input boxes, button, and show text
        self.x1.update()
        self.x2.update()
        self.y1.update()
        self.y2.update()
        self.button.update()
        text("X1",250,30)
        text("Y1",380,30)
        text("X2",250,100)
        text("Y2",380,100)
        text("Magnitude 1:",250,250)
        text("Magnitude 2:",250,280)
        text("Direction:",250,310)
        text("Dot Product:",250,340)
        
        #If the Calculate button is pressed, calculate values
        if self.button.getData() == True:
            self.magnitude1 = sqrt(pow(int(self.x1.getData()),2) + pow(int(self.y1.getData()),2))
            self.magnitude2 = sqrt(pow(int(self.x2.getData()),2) + pow(int(self.y2.getData()),2))
            self.direction = math.asin(int(self.y2.getData())/self.magnitude2) - math.asin(int(self.y1.getData())/self.magnitude1)
            self.dot_product = abs(int(self.x1.getData())*int(self.x2.getData())*int(self.y1.getData())*int(self.y2.getData())) * math.cos(self.direction)
        
        #display answers
        text(self.magnitude1,400,250)
        text(self.magnitude2,400,280)
        text(self.direction,400,310)
        text(self.dot_product,400,340)
