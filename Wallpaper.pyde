def setup():
    size(360, 760)
    background(173,216,230)
    x = -50
    y = 0
    color = 15
    noStroke()
    while y < 800:
        x = -28
        while x < 360:
            xTwo = x + 50
            xThree = x + 60
            xFour = x + 10
            fill(0, color, 255)
            
            if y % 152 == 0:
                xThree -= 20
                xFour -= 20
            
            quad(x, y, xTwo, y, xThree, y + 75, xFour, y + 75)
            x = x + 51
            color += 2.1
        y = y + 76
