import Image
f = "C:\\Users\\Ýrem\\Desktop\\image homework 2\\urban3.tiff" #input image
picfilter = "filter.tiff" #output image
img = Image.open(f) #open the input image
class kernel:
    def __init__(self):
        
        self.size = img.size
        self.width = img.size[0] #get the size of columns
        self.height = img.size[1] #get the size of rows
        self.pixels = img.load() #get the image value
        self.imgfilter = Image.new(img.mode,img.size,color=0) #create a new empty image
        
    def filtered(self):
        self.kernel_1 = [0,0,1,0,0,0,0,0,0] #first filter
        self.kernel_2 = [0,0,0,0,1.5,0,0,0,0] #second filter
        self.kernel_3 = [2,5,2,0,0,0,-2,-5,-2] #third filter
       
        for c in range(1,self.width-1):
            for r in range(1,self.height-1):
                self.total = 0
                for k in range(3):
                    self.counter=8
                    self.counter = self.counter-k
                    for m in range(3):
                        #self.total += ((self.pixels[c-k+1,r-m+1])*int(self.kernel_1[self.counter]))
                        #self.total += ((self.pixels[c-k+1,r-m+1])*int(self.kernel_2[self.counter]))
                        self.total += ((self.pixels[c-k+1,r-m+1])*int(self.kernel_3[self.counter]))
                        self.counter-=3

                    
                new_value = int(self.total)
                if new_value <0 :
                    self.imgfilter.putpixel((c,r),0)
                elif new_value > 255:
                     self.imgfilter.putpixel((c,r),255)
                else:
                    self.imgfilter.putpixel((c,r),new_value)
                
        self.imgfilter.save(picfilter)#save the image with filter
s=kernel()
s.filtered()
