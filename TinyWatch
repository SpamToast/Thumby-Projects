import thumby
import time

# "Tommy" Logo Bitmap 70 x 17
bitmapLogo = bytearray([63,15,199,243,249,249,252,204,204,204,204,12,12,204,204,204,204,124,124,124,124,252,252,252,252,124,124,252,124,124,124,252,252,124,124,124,252,252,252,124,124,252,124,124,124,252,252,124,124,124,252,252,252,124,124,252,252,124,124,140,116,116,116,140,249,249,243,199,15,63,
           248,224,199,159,63,63,127,127,127,127,127,96,96,127,127,127,120,112,111,111,111,112,121,127,127,96,96,126,127,127,96,96,126,127,127,96,96,127,127,96,96,126,127,127,96,96,126,127,127,96,96,127,127,126,108,97,113,124,126,127,127,127,127,127,63,63,159,199,224,248,
           1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1])

# TinyWatch Logo Bitmap 51 x 21
bitmapTWLogo = bytearray([3,3,3,3,255,255,3,3,3,3,0,24,251,251,0,0,0,0,0,252,252,12,12,12,12,12,12,252,248,0,28,60,48,48,48,48,48,48,252,252,0,248,4,2,2,34,83,130,4,248,16,
           248,248,0,0,195,195,0,0,251,251,3,3,99,99,99,99,99,99,96,227,195,0,96,248,248,96,96,99,3,0,192,227,99,99,99,99,99,99,99,97,0,248,249,98,98,98,98,98,97,224,192,
           15,31,28,30,15,15,30,28,31,15,0,14,31,27,27,27,27,27,27,31,31,0,0,15,31,24,24,24,24,0,15,31,24,24,24,24,24,24,24,24,0,31,31,0,0,0,0,0,0,31,31])

# Digit Bitmaps 12 x 21
bitmap0 = bytearray([248,248,248,7,7,7,7,7,7,248,248,248,
            255,255,255,0,0,0,0,0,0,255,255,255,
            3,3,3,28,28,28,28,28,28,3,3,3])

bitmap1 = bytearray([0,0,0,192,192,192,56,56,56,255,255,255,
           0,0,0,1,1,1,0,0,0,255,255,255,
           0,0,0,0,0,0,0,0,0,31,31,31])

bitmap2 = bytearray([56,56,56,7,7,7,7,7,7,248,248,248,
            128,128,128,112,112,112,14,14,14,1,1,1,
            31,31,31,28,28,28,28,28,28,28,28,28])
            
bitmap3 = bytearray([56,56,56,7,7,7,7,7,7,248,248,248,
            128,128,128,0,0,0,14,14,14,241,241,241,
            3,3,3,28,28,28,28,28,28,3,3,3])
            
bitmap4 = bytearray([0,0,0,192,192,192,56,56,56,255,255,255,
            126,126,126,113,113,113,112,112,112,255,255,255,
            0,0,0,0,0,0,0,0,0,31,31,31])
            
bitmap5 = bytearray([255,255,255,199,199,199,199,199,199,7,7,7,
            129,129,129,1,1,1,1,1,1,254,254,254,
            3,3,3,28,28,28,28,28,28,3,3,3])
            
bitmap6 = bytearray([248,248,248,7,7,7,7,7,7,56,56,56,
            255,255,255,14,14,14,14,14,14,240,240,240,
            3,3,3,28,28,28,28,28,28,3,3,3])
            
bitmap7 = bytearray([7,7,7,7,7,7,7,7,7,255,255,255,
            0,0,0,240,240,240,14,14,14,1,1,1,
            0,0,0,31,31,31,0,0,0,0,0,0])
            
bitmap8 = bytearray([248,248,248,7,7,7,7,7,7,248,248,248,
            241,241,241,14,14,14,14,14,14,241,241,241,
            3,3,3,28,28,28,28,28,28,3,3,3])
            
bitmap9 = bytearray([248,248,248,7,7,7,7,7,7,248,248,248,
            129,129,129,14,14,14,14,14,14,255,255,255,
            3,3,3,28,28,28,28,28,28,3,3,3])
            
# Colon Bitmap 4 x 15
bitmap10 = bytearray([15,15,15,15,
           120,120,120,120])

# Array with digit Bitmaps
digits = [thumby.Sprite(12, 21, bitmap) for bitmap in [bitmap0, bitmap1, bitmap2, bitmap3, bitmap4, bitmap5, bitmap6, bitmap7, bitmap8, bitmap9]]

tommyLogo = thumby.Sprite(70,17,bitmapLogo)

colon = thumby.Sprite(4,15,bitmap10)

TWLogo = thumby.Sprite(51,21,bitmapTWLogo)

digit_width = 12
digit_height = 21

tick_noise = False

#Globals Hour
digit_hour = 0
show_hour1 = digits[0]
show_hour2 = digits[0]
show_hour1_x = 2
show_hour1_y = int(round(thumby.display.height / 2) - 21 / 2)
show_hour2_x = 16
show_hour2_y = show_hour1_y

#Globals Minute
digit_minute = 0
show_minute1 = digits[0]
show_minute2 = digits[0]
show_minute1_x = 43
show_minute1_y = show_hour1_y
show_minute2_x = 57
show_minute2_y = show_hour1_y

#Globals Stopwatch
#Minutes
digit_minuteSW = 0
show_minute1SW = digits[0]
show_minute2SW = digits[0]
show_minute1SW_x = 2
show_minute1SW_y = 0
show_minute2SW_x = 16
show_minute2SW_y = show_minute1SW_y
#Seconds
digit_seconds = 0
show_seconds1 = digits[0]
show_seconds2 = digits[0]
show_seconds1_x = 43
show_seconds1_y = show_minute1SW_y
show_seconds2_x = 57
show_seconds2_y = show_minute1SW_y
#Millis
digit_millis = 0
show_millis1 = digits[0]
show_millis2 = digits[0]
show_millis3 = digits[0]
show_millis1_x = 30
show_millis1_y = 19
show_millis2_x = show_millis1_x + 14
show_millis2_y = show_millis1_y
show_millis3_x = show_millis2_x + 14
show_millis3_y = show_millis1_y



def select_hour():
    global digit_hour
    global show_hour1
    global show_hour2
    global show_hour1_x
    global show_hour1_y
    global show_hour2_x
    global show_hour2_y
    
    
    
    while True:
        digit_hour = digit_hour % 24
        tens = digit_hour // 10
        units = digit_hour % 10
        show_hour1 = digits[tens]
        show_hour2 = digits[units]
        
        z = int((time.ticks_ms() % 800) / 400)

        if z == 1:
            thumby.display.blit(show_hour1.bitmap, show_hour1_x, show_hour1_y, digit_width, digit_height, 0, 0, 0)
            thumby.display.blit(show_hour2.bitmap, show_hour2_x, show_hour2_y, digit_width, digit_height, 0, 0, 0)
        elif z == 0:
            # Clear the area where the digits are displayed
            thumby.display.drawFilledRectangle(show_hour1_x, show_hour1_y, 28, 21, 0)

        thumby.display.update()
        if thumby.buttonU.justPressed():
            digit_hour += 1
            thumby.display.drawFilledRectangle(show_hour1_x, show_hour1_y, 28, 21, 0)
            thumby.display.update()
        if thumby.buttonD.justPressed():
            digit_hour -= 1
            thumby.display.drawFilledRectangle(show_hour1_x, show_hour1_y, 28, 21, 0)
            thumby.display.update()
        if thumby.buttonA.justPressed():
            thumby.display.blit(show_hour1.bitmap, show_hour1_x, show_hour1_y, digit_width, digit_height, 0, 0, 0)
            thumby.display.blit(show_hour2.bitmap, show_hour2_x, show_hour2_y, digit_width, digit_height, 0, 0, 0)
            thumby.display.update()
            break
        
def select_minute():
    global digit_minute
    global show_minute1
    global show_minute2
    global show_minute1_x
    global show_minute1_y
    global show_minute2_x
    global show_minute2_y
    
    while True:
        digit_minute = digit_minute % 60
        tens = digit_minute // 10
        units = digit_minute % 10
        show_minute1 = digits[tens]
        show_minute2 = digits[units]
        z = int((time.ticks_ms() % 800) / 400)

        if z == 1:
            thumby.display.blit(show_minute1.bitmap, show_minute1_x, show_minute1_y, digit_width, digit_height, 0, 0, 0)
            thumby.display.blit(show_minute2.bitmap, show_minute2_x, show_minute2_y, digit_width, digit_height, 0, 0, 0)
        elif z == 0:
            # Clear the area where the digits are displayed
            thumby.display.drawFilledRectangle(show_minute1_x, show_minute1_y, 28, 21, 0)

        thumby.display.update()
        if thumby.buttonU.justPressed():
            digit_minute += 1
            thumby.display.drawFilledRectangle(show_minute1_x, show_minute1_y, 28, 21, 0)
            thumby.display.update()
        if thumby.buttonD.justPressed():
            digit_minute -= 1
            thumby.display.drawFilledRectangle(show_minute1_x, show_minute1_y, 28, 21, 0)
            thumby.display.update()
        if thumby.buttonA.justPressed():
            thumby.display.blit(show_minute1.bitmap, show_minute1_x, show_minute1_y, digit_width, digit_height, 0, 0, 0)
            thumby.display.blit(show_minute2.bitmap, show_minute2_x, show_minute2_y, digit_width, digit_height, 0, 0, 0)
            thumby.display.update()
            break
        
def show_time():
    colon_blink = time.ticks_ms()
    z = time.ticks_ms()
    global colon
    global digit_hour
    global digit_minute
    global show_hour1
    global show_hour2
    global show_minute1
    global show_minute2
    global show_hour1_x
    global show_hour1_y
    global show_hour2_x
    global show_hour2_y
    global show_minute1_x
    global show_minute1_y
    global show_minute2_x
    global show_minute2_y
    global tick_noise
    colon.x = int(round(thumby.display.width/2)-4/2)
    colon.y = int(round(thumby.display.height/2)-15/2)
    
    while True:
        
        digit_hour = digit_hour % 24
        tens = digit_hour // 10
        units = digit_hour % 10
        show_hour1 = digits[tens]
        show_hour2 = digits[units]
        
        digit_minute = digit_minute % 60
        tens = digit_minute // 10
        units = digit_minute % 10
        show_minute1 = digits[tens]
        show_minute2 = digits[units]
        
        thumby.display.blit(show_hour1.bitmap, show_hour1_x, show_hour1_y, digit_width, digit_height, 0, 0, 0)
        thumby.display.blit(show_hour2.bitmap, show_hour2_x, show_hour2_y, digit_width, digit_height, 0, 0, 0)
        thumby.display.blit(show_minute1.bitmap, show_minute1_x, show_minute1_y, digit_width, digit_height, 0, 0, 0)
        thumby.display.blit(show_minute2.bitmap, show_minute2_x, show_minute2_y, digit_width, digit_height, 0, 0, 0)
        thumby.display.update()
        
        if time.ticks_ms() - colon_blink >= 1000 and tick_noise == False:
            thumby.display.drawSprite(colon)
            thumby.display.update()
            thumby.audio.play(2000, 10)
            tick_noise = True
        if time.ticks_ms() - colon_blink >= 2000 and tick_noise == True:
            thumby.display.drawFilledRectangle(colon.x,colon.y,4, 15, 0)
            thumby.display.update()
            thumby.audio.play(1500, 10)
            tick_noise = False
            colon_blink = time.ticks_ms()
        
        if time.ticks_ms() - z >= 60000:
            digit_minute += 1
            thumby.display.fill(0)
            z = time.ticks_ms()
        if digit_minute > 59:
            digit_hour += 1
            thumby.display.fill(0)
            
def intro():
    thumby.display.setFPS(60)
    thumby.display.fill(1)
    tommyLogo.x = int((thumby.display.width/2) - (70/2))
    tommyLogo.y = int(round((thumby.display.height/2) - (17/2)))
    thumby.display.drawSprite(tommyLogo)
    thumby.display.update()
    thumby.audio.play(2000, 200)
    time.sleep(.1)
    thumby.audio.play(3000, 300)
    time.sleep(1)
    thumby.display.fill(0)
            
def menu():
    s = time.ticks_ms()
    global tick_noise
    TWLogo.x = int((thumby.display.width/2)-(51/2))
    TWLogo.y =int((thumby.display.height/2)-20)
    thumby.display.drawSprite(TWLogo)
    thumby.display.drawText("A:Clock", 1, 24, 1)
    thumby.display.drawText("B:Stopwatch", 1, 32, 1)
    thumby.display.update()
    
    while True:
        if time.ticks_ms() - s >= 1000 and tick_noise == False:
            thumby.audio.play(2000, 10)
            thumby.display.drawFilledRectangle(1, 23, 70, 40 ,0)
            thumby.display.drawText("A:Clock", 1, 23, 1)
            thumby.display.drawText("B:Stopwatch", 1, 31, 1)
            thumby.display.update()
            tick_noise = True
            
        if time.ticks_ms() - s >= 2000 and tick_noise == True:
            thumby.audio.play(1500, 10)
            thumby.display.drawFilledRectangle(1, 23, 70, 40 ,0)
            thumby.display.drawText("A:Clock", 1, 24, 1)
            thumby.display.drawText("B:Stopwatch", 1, 32, 1)
            thumby.display.update()
            s = time.ticks_ms()
            tick_noise = False
            
        if thumby.buttonA.justPressed():
            thumby.display.fill(0)
            return 1
        
        if thumby.buttonB.justPressed():
            thumby.display.fill(0)
            return 2
 
def clock():
    select_hour()
    select_minute()
    show_time()
    
def stopwatch():
    global tick_noise
    global digit_minuteSW
    global show_minute1SW
    global show_minute2SW
    global show_minute1SW_x
    global show_minute1SW_y
    global show_minute2SW_x
    global show_minute2SW_y
    
    global digit_seconds
    global show_seconds1
    global show_seconds2
    global show_seconds1_x
    global show_seconds1_y
    global show_seconds2_x
    global show_seconds2_y
    
    global digit_millis
    global show_millis1
    global show_millis2
    global show_millis3
    global show_millis1_x
    global show_millis1_y
    global show_millis2_x
    global show_millis2_y
    global show_millis3_x
    global show_millis3_y
    
    colon.x = int(round(thumby.display.width/2)-4/2)
    colon.y = show_minute1SW_y + 3
    millis = digit_seconds / 10
    colon_blink = time.ticks_ms()
    s = time.ticks_ms()
    thumby.display.drawSprite(colon)
    
    while True:
        
        digit_minuteSW = digit_minuteSW % 60
        tens = digit_minuteSW // 10
        units = digit_minuteSW % 10
        show_minute1SW = digits[tens]
        show_minute2SW = digits[units]
        
        digit_seconds = digit_seconds % 60
        tens = digit_seconds // 10
        units = digit_seconds % 10
        show_seconds1 = digits[tens]
        show_seconds2 = digits[units]
        
        digit_millis = time.ticks_ms()
        digit_millis = digit_millis % 1000
        hundreds = digit_millis // 100
        tens = (digit_millis // 10) % 10
        ones = digit_millis % 10
        show_millis1 = digits[hundreds]
        show_millis2 = digits[tens]
        show_millis3 = digits[ones]
        
        thumby.display.blit(show_minute1SW.bitmap, show_minute1SW_x, show_minute1SW_y, digit_width, digit_height, 0, 0, 0)
        thumby.display.blit(show_minute2SW.bitmap, show_minute2SW_x, show_minute2SW_y, digit_width, digit_height, 0, 0, 0)
        thumby.display.blit(show_seconds1.bitmap, show_seconds1_x, show_seconds1_y, digit_width, digit_height, 0, 0, 0)
        thumby.display.blit(show_seconds2.bitmap, show_seconds2_x, show_seconds2_y, digit_width, digit_height, 0, 0, 0)
        thumby.display.blit(show_millis1.bitmap, show_millis1_x, show_millis1_y, digit_width, digit_height, 0, 0, 0)
        thumby.display.blit(show_millis2.bitmap, show_millis2_x, show_millis2_y, digit_width, digit_height, 0, 0, 0)
        thumby.display.blit(show_millis3.bitmap, show_millis3_x, show_millis3_y, digit_width, digit_height, 0, 0, 0)
        
        thumby.display.update()
        
        if time.ticks_ms() - colon_blink >= 1000 and tick_noise == False:
            thumby.display.drawFilledRectangle(colon.x,colon.y,4, 15, 0)
            thumby.display.update()
            thumby.audio.play(2000, 10)
            tick_noise = True
        if time.ticks_ms() - colon_blink >= 2000 and tick_noise == True:
            thumby.display.drawSprite(colon)
            thumby.display.update()
            thumby.audio.play(1500, 10)
            tick_noise = False
            colon_blink = time.ticks_ms()
        
        if time.ticks_ms() - s >= 1000:
            digit_seconds += 1
            thumby.display.drawFilledRectangle(show_seconds1_x, show_seconds1_y, digit_width*2+2, digit_height, 0)
            s = time.ticks_ms()
        if digit_seconds > 59:
            digit_minuteSW += 1
            thumby.display.drawFilledRectangle(show_minute1SW_x, show_minute1SW_y, digit_width*2+2, digit_height, 0)
        thumby.display.drawFilledRectangle(show_millis1_x, show_millis1_y, digit_width * 3 + 6, digit_height, 0)
    
            
# Main program
while True:
    intro()
    option = menu()
    if option == 1:
        clock()
    elif option == 2:
        stopwatch()
