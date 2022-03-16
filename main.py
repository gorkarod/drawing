# from pagebot.document import Document
# from pagebot.elements import newText
# from pagebot.fonttoolbox.objects.font import findFont

import drawBot

drawBot.newDrawing()
drawBot.newPage(1000, 1000)
drawBot.rect(10, 10, 100, 100)
drawBot.saveImage("main.png")
drawBot.endDrawing()
