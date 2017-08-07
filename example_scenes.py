#!/usr/bin/env python
# coding=utf-8
from helpers import *

from mobject.tex_mobject import TexMobject
from mobject import Mobject
from mobject.image_mobject import ImageMobject
from mobject.vectorized_mobject import *

from animation.animation import Animation
from animation.transform import *
from animation.simple_animations import *
from animation.playground import *
from topics.geometry import *
from topics.characters import *
from topics.functions import *
from topics.number_line import *
from topics.combinatorics import *
from scene import Scene
from camera import Camera
from mobject.svg_mobject import *
from mobject.tex_mobject import *

from mobject.vectorized_mobject import *


## To watch one of these scenes, run the following:
## python extract_scenes.py -p file_name <SceneName>

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.rotate(np.pi / 8)
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.dither()


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda (x, y, z): complex_to_R3(np.exp(complex(x, y))),
            square
        ))
        self.dither()


class WriteStuff(Scene):
    def construct(self):
        self.play(Write(TextMobject("Stuff").scale(3)))


class Elements(Scene):
    lastElem = 0
    llElem = 0
    lastName = 0
    startPoint = (-5, 0, 0)
    endPoint = (5, 0, 0)
    midPoint = (0, 3, 0)

    def construct(self):
        text = TextMobject("演示").set_color(GRAY).scale(1.5)
        self.play(ShowCreation(text))
        arc = Arc(3.1)
        self.transform_dither(arc, "弧")
        circle = Circle()
        self.transform_dither(circle, "圆")
        dot = Dot()
        self.transform_dither(dot, "点")
        line = Line(self.startPoint, self.endPoint)
        self.transform_dither(line, "线")
        dashedLine = DashedLine(self.startPoint, self.endPoint)
        self.transform_dither(dashedLine, "虚线")
        arrow = Arrow(self.startPoint, self.endPoint)
        self.transform_dither(arrow, "箭头")
        vector = Vector((0, 1))
        self.transform_dither(vector, "向量")
        doubleArrow = DoubleArrow(self.startPoint, self.endPoint)
        self.transform_dither(doubleArrow, "双向箭头")
        #cubicBezier = CubicBezier((self.startPoint, self.endPoint, (1, 1, 1)))
        #self.transform_dither(cubicBezier, "空间贝塞尔曲线")
        brace=Brace(text)
        self.transform_dither(brace,"大括号")
        polygon = Polygon(self.startPoint, self.midPoint, self.endPoint)
        self.transform_dither(polygon, "多边形")
        regularPolygon = RegularPolygon(6)
        self.transform_dither(regularPolygon, "正多边形")
        rectangle = Rectangle()
        self.transform_dither(rectangle, "矩形")
        square = Square()
        self.transform_dither(square, "正方形")
        surroundingRectangle = SurroundingRectangle(text)
        self.transform_dither(surroundingRectangle, "包裹矩形")
        backgroundRectangle = BackgroundRectangle(text)
        self.transform_dither(backgroundRectangle,"背景淡出")
        screenRectangle = ScreenRectangle()
        self.transform_dither(screenRectangle, "屏幕矩形")
        fullScreenFadeRectangle = FullScreenFadeRectangle()
        self.transform_dither(fullScreenFadeRectangle, "全屏化渐变")
        pictureInPictureFrame = PictureInPictureFrame()
        self.transform_dither(pictureInPictureFrame, "画中画")
        cross = Cross(text)
        self.transform_dither(cross, "叉")
        grid = Grid(5, 5)
        self.transform_dither(grid, "网格")

    def transform_dither(self, elem, name=""):
        if name == "":
            name = elem.name
        nameObjd = TextMobject(name)
        nameObjd.next_to(elem, DOWN * 2)
        if self.lastElem == 0:
            self.play(ShowCreation(elem), Write(nameObjd))
        else:
            if self.llElem != 0:
                self.play(Transform(self.lastElem, elem, run_time=2),
                          Write(nameObjd),
                          FadeOut(self.lastName),
                          FadeOut(self.llElem)
                          )
                self.remove(self.llElem)
            else:
                self.play(Transform(self.lastElem, elem, run_time=2),
                          Write(nameObjd),
                          FadeOut(self.lastName),
                          )
            self.remove(self.lastName)
        self.lastName = nameObjd
        self.dither()
        self.llElem = self.lastElem
        self.lastElem = elem
