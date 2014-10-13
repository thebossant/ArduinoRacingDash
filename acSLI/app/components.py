import ac


class Window:

    def __init__(self, name="defaultAppWindow", width=100, height=100):
        self.app = ac.newApp(name)
        ac.drawBorder(self.app, 0)
        ac.setBackgroundOpacity(self.app, 0)
        ac.setSize(self.app, width, height)

    def setPos(self, x, y):
        ac.setPosition(self.app, x, y)
        return self

    def setVisible(self, visible):
        ac.setVisible(self.app, visible)
        return self


class Label:

    def __init__(self, window, text, xPos, yPos):
        self.label = ac.addLabel(window, text)
        ac.setPosition(self.label, xPos, yPos)

    def setText(self, text):
        ac.setText(self.label, text)
        return self

    def setSize(self, w, h):
        ac.setSize(self.label, w, h)
        return self

    def setColor(self, color):
        ac.setFontColor(self.label, *color)
        return self

    def setFontSize(self, fontSize):
        ac.setFontSize(self.label, fontSize)
        return self

    def setAlign(self, align = "left"):
        ac.setFontAlignment(self.label, align)
        return self

    def setVisible(self, value):
        ac.setVisible(self.label, value)
        return self


class Button:

    def __init__(self, window, clickFunc, width=60, height=20, x=0, y=0, text=""):
        self.button = ac.addButton(window, text)
        self.setSize(width, height)
        self.setPos(x, y)
        ac.addOnClickedListener(self.button, clickFunc)

    def setSize(self, width, height):
        ac.setSize(self.button, width, height)
        return self

    def setPos(self, x, y):
        ac.setPosition(self.button, x, y)
        return self

    def setAlign(self, align = "left"):
        ac.setFontAlignment(self.button, align)
        return self