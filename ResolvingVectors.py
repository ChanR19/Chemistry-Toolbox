import math

from TextBox import TextBox
from Button import Button
from Switch import Switch

class ResolvingVectors:
    add_input_button = Button(250,30,200,30,"Add Input Boxes",20)
    delete_input_button = Button(450,30,200,30,"Delete Input Boxes",20)
    calculate_button = Button(650,30,120,30,"Calculate",20)
    magnitude_text_boxes = [TextBox(250,110,100,30,20)]
    direction_text_boxes = [TextBox(450,110,100,30,20)]
    text_box_y = 140
    x_answers = []
    y_answers = []
    z_answers = []
    sum = 0
    def update(self):
        self.add_input_button.update()
        self.delete_input_button.update()
        self.calculate_button.update()
        text("Magnitude",250,90)
        text("Direction",450, 90)
        text("X",620,90)
        text("Y",720,90)
        text("Z",820,90)
        
        #Code for adding and deleting input boxes
        if self.add_input_button.getData() == True: 
            self.magnitude_text_boxes.append(TextBox(250,self.text_box_y,100,30,20))
            self.direction_text_boxes.append(TextBox(450,self.text_box_y,100,30,20))
            self.text_box_y += 30
        elif self.delete_input_button.getData() == True:
            self.magnitude_text_boxes.pop(len(self.magnitude_text_boxes) - 1)
            self.direction_text_boxes.pop(len(self.direction_text_boxes) - 1)
            self.text_box_y -= 30
        
        #Update input boxes
        for text_box in self.magnitude_text_boxes: 
            text_box.update()
        for text_box in self.direction_text_boxes:
            text_box.update()
        
        #If the Calculate button is pressed, calculate values
        if self.calculate_button.getData() == True:
            self.x_answers = []
            self.y_answers = []
            self.z_answers = []
            for i in range(len(self.magnitude_text_boxes)):
                self.x_answers.append(float(self.magnitude_text_boxes[i].getData())*math.cos(int(self.direction_text_boxes[i].getData())))
                self.y_answers.append(float(self.magnitude_text_boxes[i].getData())*math.sin(int(self.direction_text_boxes[i].getData())))
                inside = pow(float(self.magnitude_text_boxes[i].getData()),2)-pow(self.x_answers[i],2)-pow(self.y_answers[i],2)
                self.z_answers.append(pow( inside, .333))
        
        #If there are an answers, display them
        if len(self.x_answers) > 0: 
            last_index = 0   
            for i in range(len(self.x_answers)):
                text(self.x_answers[i],600,140+i*30)
                text(self.y_answers[i],700,140+i*30)
                text(self.z_answers[i],800,140+i*30)
                last_index = i
            text("Totals:",450,170+last_index*30)
            text(sum(self.x_answers),600,170+last_index*30)
            text(sum(self.y_answers),700,170+last_index*30)
            text(sum(self.z_answers),800,170+last_index*30)
