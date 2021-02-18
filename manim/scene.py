from manim import *

class HelloWorld(Scene):
    def construct(self):
        #######Code#######
        # テキストを定義
        first_text = Text("Hello, World!")

        # テキストを表示
        self.wait(1)
        self.play(Write(first_text))
        self.wait(1)
        # テキスト２つ分アップ
        self.play(ApplyMethod(first_text.shift,2*UP))
        self.wait(1)

        math_text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        # 数式を表示
        self.play(Write(math_text))

        framebox1 = SurroundingRectangle(math_text[1], buff = .1)
        framebox2 = SurroundingRectangle(math_text[3], buff = .1)

        self.play(
            ShowCreation(framebox1),
        )
        self.wait()
        # manim.animation.transform
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()