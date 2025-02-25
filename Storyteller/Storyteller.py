import thumby
import time
import math
import random

####################################
# Created by: Austinio & SpamToast #
####################################

# A-Sprite 3 x 5
bitmapA = bytearray([30, 11, 30])

blink_A = thumby.Sprite(3, 5, bitmapA)

texts = ["This is the Textengine 'Storyteller'", "It was created by Austinio and SpamToast.",
         "To use Storyteller just write your Texts into the 'texts'-array.", "Storyteller will take care of the rest.",
         "Have Fun!"]


def storyteller(text, start_x, start_y, area_width, area_height, font_width, font_height):
    """Display the given text with a typewriter effect."""

    # Define letter length and line height change based on font dimensions (+1 for space between letters and lines)
    letter_length, line_height_change = font_width + 1, font_height + 1

    # Set the speed of typing and calculate the maximum number of lines that can fit in the area
    scroll_speed, max_lines = 0.05, (area_height - font_height) // line_height_change

    # Initialize the starting position for the first letter and the first line
    letter_position, line_height, lines_printed = start_x, start_y, 0

    # Clear the display before starting
    thumby.display.fill(0)

    # Split the input text into words
    words = text.split()
    for word in words:
        # Check if the word fits in the current line, if not, move to the next line
        if letter_position + len(word) * letter_length >= start_x + area_width:
            line_height += line_height_change
            letter_position = start_x
            lines_printed += 1

        # If the maximum number of lines is reached, wait for user input to continue
        if lines_printed >= max_lines:
            a_blink(text, start_x, start_y, area_width, area_height, font_width, font_height)

            # Clear the display and reset the position for new text
            thumby.display.fill(0)
            letter_position, line_height, lines_printed = start_x, start_y, 0

        # Type out each character in the word
        for i in word:
            thumby.display.drawText(i, letter_position, line_height, 1)
            thumby.display.update()
            letter_position += letter_length
            time.sleep(scroll_speed)
            thumby.audio.play(random.randrange(270, 300), 50)

        # Add a space between words
        letter_position += letter_length

    # Play a sound to indicate the end of the text display
    thumby.audio.play(300, 100)
    a_blink(text, start_x, start_y, area_width, area_height, font_width, font_height)


def a_blink(text, start_x, start_y, area_width, area_height, font_width, font_height):
    while True:
        blink_A.x = start_x + area_width - font_width
        blink_A.y = start_y + area_height - font_height
        blink_rate = int((time.ticks_ms() % 800) / 400)
        if blink_rate >= 1:
            # Display "(A)" to indicate more text is available
            thumby.display.drawSprite(blink_A)
            thumby.display.update()
        else:
            # Clear the "(A)" and wait again
            thumby.display.drawFilledRectangle(start_x + area_width - font_width, start_y + area_height - font_height,
                                               area_width, font_height, 0)
            thumby.display.update()

        # Check if button A is pressed to continue
        if thumby.buttonA.justPressed():
            thumby.audio.play(3000, 50)
            break


while True:
    # thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
    storyteller(texts[0], 1, 1, 70, 40, 5, 7)
    storyteller(texts[1], 1, 1, 70, 40, 5, 7)
    storyteller(texts[2], 1, 1, 70, 40, 5, 7)
    storyteller(texts[3], 1, 1, 70, 40, 5, 7)
    storyteller(texts[4], 1, 1, 70, 40, 5, 7)