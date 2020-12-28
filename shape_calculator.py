class Rectangle:
    def __init__(self,wd,h):
        self.width=wd
        self.height=h
    
    def __str__(self):
        string="Rectangle(width="
        string+=str(self.width)
        string+=", height="
        string+=str(self.height)
        string+=")"
        return string

    def set_width(self,wd):
        self.width=wd
    
    def set_height(self,h):
        self.height=h
    
    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height>50 or self.width>50:
            return "Too big for picture."
        string=""
        for x in range(0,self.height):
            for y in range(0,self.width):
                string+="*"
            string+="\n"
        return string
    
    def get_amount_inside(self,rect):
        a=self.width
        b=self.height
        c=rect.width
        d=rect.height
        count=0
        while a>=0 and b>0:
            if a>=c and b>=d:
                count+=1
                a-=c
            else:
                a=self.width
                b-=d
        return count


class Square(Rectangle):

    def __init__(self,side):
        self.width=side
        self.height=side
    def __str__(self):
        string="Square(side="
        string+=str(self.width)
        string+=")"
        return string
    
    def set_side(self,side):
        self.width=side
        self.height=side
    
    def set_width(self, wd):
        self.width=wd
        self.height=wd

    def set_height(self, h):
        self.width=h
        self.height=h