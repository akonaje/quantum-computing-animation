from manim import *


class FullVideo(ThreeDScene):
    def construct(self):

        # introduction
        self.introduction()
        self.wait(1)

        self.simple_problem()
        self.wait(1)


        self.exp_problem()
        self.wait(1)

        # body
        self.Video_body()
        self.wait(2)
        self.bit_intro()
        self.wait(2)

        self.Superposition()
        self.wait(2)
 
        self.entanglement()
        self.wait(2)

        self.parallelism()
        self.wait(2)



    def bit_intro(self):
        # Title at the top
        title = Text("A brief intro to bits").to_edge(UP)
        self.play(Write(title))

        # --- Classic bit on the right ---
       
        dot1 = Dot(radius=0.1, color=RED)
        classic_label = Text("Classic bit", font_size=20)
        dot1_label = Text("0 or 1", font_size=16)

        # Arrange: label on top, dot in middle, 0/1 label at bottom
        classic_group = VGroup(classic_label, dot1, dot1_label).arrange(DOWN, buff=0.3)
        classic_group.to_edge(RIGHT, buff=3)

        # --- Quantum bit on the left ---
        qubit_label = Text("Quantum bit", font_size=20)
        circ = Circle(radius=1, color=RED)

        dot2 = Dot(radius=0.1, color=RED).move_to(circ.point_at_angle(PI / 2))
        dot3 = Dot(radius=0.1, color=RED).move_to(circ.point_at_angle(-PI / 2))

        circ_label = Text("0, 1, or  00, 10, 01, 11", font_size=16).next_to(circ, DOWN, buff=0.2)

        quantum_graphic = VGroup(circ, dot2, dot3, circ_label)
        quantum_group = VGroup(qubit_label, quantum_graphic).arrange(DOWN, buff=0.3)
        quantum_group.to_edge(LEFT, buff=3)

        # --- Align both vertically ---
        # Make both bottom-aligned to match
        #classic_group.move_to(quantum_group, aligned_edge=DOWN)

        # --- Animate everything ---
        self.play(FadeIn(classic_group), FadeIn(quantum_group))
        self.wait(2)

        # Classic bit color change
        self.play(dot1.animate.set_color(BLUE))
        self.play(dot1.animate.set_color(YELLOW))
        self.wait()

        # Quantum bit rotation + color
        # can both be 1, 0, or diff values
        self.play(dot2.animate.set_color(BLUE), dot3.animate.set_color(BLUE))
        self.wait()
        self.play(dot2.animate.set_color(YELLOW), dot3.animate.set_color(YELLOW))
        self.wait()
        self.play(dot2.animate.set_color(BLUE), dot3.animate.set_color(YELLOW))
        self.wait()
        self.play(dot2.animate.set_color(YELLOW), dot3.animate.set_color(BLUE))
        self.wait()

        # rotation
        self.play(
            Rotate(VGroup(dot2, dot3), angle=2 * PI, about_point=circ.get_center()),
            run_time=4
        )
        self.wait(2)
        self.play(FadeOut(title), FadeOut(classic_group), FadeOut(quantum_group), FadeOut(quantum_graphic))


    def parallelism(self):
        
        # --- Title ---
        title = Text("Quantum Parallelism").to_edge(UP)
        self.play(Write(title))

        # --- First Visualization: Clues activating sequentially ---
        line = Line(LEFT * 4, RIGHT * 4)

        # Create 11 dots along the line
        points = [Dot(point=line.point_from_proportion(i / 10)) for i in range(11)]

        # Label only the first and last
        point_A = Text("Clue 1").next_to(points[0], LEFT, buff=0.2)
        point_end = Text("Conclusion").next_to(points[-1], RIGHT, buff=0.2)

        for point in points:
            point.set_color(WHITE)

        self.play(FadeIn(line, *points, point_A, point_end))

        # Sequential highlight animation
        for i, point in enumerate(points):
            self.play(point.animate.set_color(RED), run_time=0.3)
            if i > 0:
                self.play(points[i-1].animate.set_color(WHITE), run_time=0.3)

        self.wait()
        self.play(FadeOut(line, *points, point_A, point_end))

        # --- Second Visualization: Parallel lines converging ---
        start_x = -5
        end_x = 4
        y_positions = [2, 1, -1, -2]

        start_dots = VGroup()
        lines = VGroup()

        # Create end dot
        end_dot = Dot(point=[end_x, 0, 0], color=WHITE)
        end_text = Text("Conclusion").next_to(end_dot, RIGHT, buff=0.4)

        for y in y_positions:
            dot = Dot(point=[start_x, y, 0], color=WHITE)
            line = Line(dot.get_center(), end_dot.get_center(), color=WHITE)
            start_dots.add(dot)
            lines.add(line)

        start_text = Text("Clues").next_to(start_dots, UP, buff=0.5)

        self.play(FadeIn(start_dots, end_dot, start_text, end_text))
        self.wait(0.5)

        self.play(*[
            GrowFromPoint(line, dot.get_center())
            for line, dot in zip(lines, start_dots)
        ], run_time=1)

        self.wait(1)

    

    def entanglement(self):
        title = Text("Entanglement").to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        self.set_camera_orientation(phi=60 * DEGREES, theta=90 * DEGREES)
        # axes = ThreeDAxes()

        # Create 3D cubes
        cube1 = Cube(side_length=1, fill_opacity=0.7, fill_color=BLUE).move_to(LEFT * 1.5)
        cube2 = Cube(side_length=1, fill_opacity=0.7, fill_color=BLUE).move_to(RIGHT * 1.5)
        cubes = VGroup(cube1, cube2)
        self.add(cube1, cube2)

        def get_arrow():
            p1 = self.camera.project_point(cube1.get_center() + RIGHT * 0.5)
            p2 = self.camera.project_point(cube2.get_center() + LEFT * 0.5)
            return DoubleArrow(p1, p2, color=YELLOW, stroke_width=4)

        arrow = always_redraw(get_arrow)
        self.add_fixed_in_frame_mobjects(arrow)

        self.wait(1)
        self.play(
            cube1.animate.shift(LEFT * 2),
            cube2.animate.shift(RIGHT * 2),
            run_time=2
        )

        arrow_label = Text("The ends of the globe", font_size=20).move_to(UP * 0.5)
        self.add_fixed_in_frame_mobjects(arrow_label)
        self.play(FadeIn(arrow_label))
        self.wait(2)

        

        self.play(FadeOut(cubes), FadeOut(arrow), FadeOut(arrow_label), FadeOut(title))
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait(2)



    def introduction(self):
        title = Text("Welcome to our video on quantum computing!", font_size=50).to_edge(UP)
        title.move_to(ORIGIN)

        self.play(Write(title))
        self.play(FadeOut(title))

    def simple_problem(self):
        title = Text("Most problems are easy to solve for classic computers", font_size=36).to_edge(UP)
        self.play(Write(title))
        boxes = VGroup(*[
            Square(side_length=0.8).set_color(WHITE)
            for _ in range(5)
        ]).arrange(RIGHT, buff=0.5).move_to(DOWN)

        labels = VGroup(*[
            Text(str(i + 1), font_size=24).move_to(box.get_center())
            for i, box in enumerate(boxes)
        ])

        self.play(FadeIn(boxes), FadeIn(labels))

        # Animate a dot "searching" linearly
        search_dot = Dot(radius=0.1, color=YELLOW).move_to(boxes[0].get_top() + UP * 0.3)
        self.play(FadeIn(search_dot))

        for box in boxes:
            self.play(search_dot.animate.move_to(box.get_top() + UP * 0.3), run_time=0.3)

        self.play(FadeOut(search_dot), FadeOut(boxes), FadeOut(labels))

        # Simple linear graph overlay
        axes = Axes(
            x_range=[0, 6], y_range=[0, 6], axis_config={"color": WHITE}
        ).scale(0.6)

        line = axes.plot(lambda x: x, color=GREEN)
        label = axes.get_graph_label(line, label="f(n) = n")

        self.play(Create(axes), Create(line), FadeIn(label))
        self.wait(2)
        self.play(FadeOut(axes), FadeOut(line), FadeOut(title), FadeOut(label))

    def exp_problem(self):

        title = Text("Some problems take longer", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Initial dot
        root_dot = Dot(ORIGIN).set_color(BLUE)
        self.play(FadeIn(root_dot))

        # Track all elements for later fading
        tree_elements = VGroup(root_dot)

        # Start with the root
        current_dots = [root_dot]
        current_positions = [ORIGIN]

        for level in range(3):
            new_dots = []
            new_positions = []
            for dot, pos in zip(current_dots, current_positions):
                left = pos + LEFT * (1.5 / (level + 1)) + DOWN
                right = pos + RIGHT * (1.5 / (level + 1)) + DOWN

                # Create lines and new dots
                line1 = Line(pos, left)
                line2 = Line(pos, right)
                left_dot = Dot(left).set_color(BLUE)
                right_dot = Dot(right).set_color(BLUE)

                # Add to animation group
                tree_elements += VGroup(line1, line2, left_dot, right_dot)

                # Play animation
                self.play(
                    Create(line1),
                    Create(line2),
                    FadeIn(left_dot),
                    FadeIn(right_dot),
                    run_time=0.4
                )

                # Prepare for next level
                new_dots.extend([left_dot, right_dot])
                new_positions.extend([left, right])

            current_dots = new_dots
            current_positions = new_positions

        self.wait(1)
        self.play(FadeOut(tree_elements))

        # Exponential curve overlay
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 20, 5],
            axis_config={"color": WHITE}
        ).scale(0.6)

        curve = axes.plot(lambda x: 2**x, color=RED)
        graph_label = axes.get_graph_label(curve, label="2^n")

        self.play(Create(axes), Create(curve), FadeIn(graph_label))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(graph_label), FadeOut(axes), FadeOut(curve))


    def Video_body(self):
        title = Text("Concepts that are key towards understanding quantum computers", font_size=36)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))


    def Superposition(self):
        title = Text("Superposition").to_edge(UP)
        self.play(Write(title))

        # Coin body: thin cylinder

        radius = 1
        height = 0.1

        # Create front face (gold)
        top = Dot(radius=radius, color=GOLD_D, fill_opacity=1).move_to(OUT * height / 2)
        front_text = Text("Heads", font_size=24).move_to(top.get_center())

        # Create back face (red)
        bottom = top.copy().set_color(RED).move_to(IN * height / 2)

        # Edge of the coin
        edge = Cylinder(radius=radius, height=height).set_fill(GREY, opacity=1)

        # Combine all parts
        coin = VGroup(edge, top, bottom, front_text)

        self.play(FadeIn(coin))
        self.wait(0.5)

        # Flip multiple times
        for _ in range(20):
            self.play(Rotate(coin, angle=PI, axis=UP), run_time=0.18)

        self.play(FadeOut(coin))
        self.play(FadeOut(title))
        self.wait(2)

         



### -- THE INTRO TO THE VIDEO -- ###


class Introduction(Scene):
    def construct(self):
        title = Text("Welcome to our video on quantum computing!", font_size=50).to_edge(UP)
        title.move_to(ORIGIN)

        self.play(Write(title))

        self.wait(15)
        self.play(FadeOut(title))


class SimpleProblem(Scene):
    def construct(self):
        
        title = Text("Most problems are easy to solve for classic computers", font_size=36).to_edge(UP)
        self.play(Write(title))
        boxes = VGroup(*[
            Square(side_length=0.8).set_color(WHITE)
            for _ in range(5)
        ]).arrange(RIGHT, buff=0.5).move_to(DOWN)

        labels = VGroup(*[
            Text(str(i + 1), font_size=24).move_to(box.get_center())
            for i, box in enumerate(boxes)
        ])

        self.play(FadeIn(boxes), FadeIn(labels))

        # Animate a dot "searching" linearly
        search_dot = Dot(radius=0.1, color=YELLOW).move_to(boxes[0].get_top() + UP * 0.3)
        self.play(FadeIn(search_dot))

        for box in boxes:
            self.play(search_dot.animate.move_to(box.get_top() + UP * 0.3), run_time=0.3)

        self.play(FadeOut(search_dot), FadeOut(boxes), FadeOut(labels))

        # Simple linear graph overlay
        axes = Axes(
            x_range=[0, 6], y_range=[0, 6], axis_config={"color": WHITE}
        ).scale(0.6)

        line = axes.plot(lambda x: x, color=GREEN)
        label = axes.get_graph_label(line, label="f(n) = n")

        self.play(Create(axes), Create(line), FadeIn(label))
        self.wait(2)
        self.play(FadeOut(axes), FadeOut(line), FadeOut(title), FadeOut(label))


# Scene 1: The Problem
class ExponentialGrowthScene(Scene):
    def construct(self):

        title = Text("Some problems take longer", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Initial dot
        root_dot = Dot(ORIGIN).set_color(BLUE)
        self.play(FadeIn(root_dot))

        # Track all elements for later fading
        tree_elements = VGroup(root_dot)

        # Start with the root
        current_dots = [root_dot]
        current_positions = [ORIGIN]

        for level in range(3):
            new_dots = []
            new_positions = []
            for dot, pos in zip(current_dots, current_positions):
                left = pos + LEFT * (1.5 / (level + 1)) + DOWN
                right = pos + RIGHT * (1.5 / (level + 1)) + DOWN

                # Create lines and new dots
                line1 = Line(pos, left)
                line2 = Line(pos, right)
                left_dot = Dot(left).set_color(BLUE)
                right_dot = Dot(right).set_color(BLUE)

                # Add to animation group
                tree_elements += VGroup(line1, line2, left_dot, right_dot)

                # Play animation
                self.play(
                    Create(line1),
                    Create(line2),
                    FadeIn(left_dot),
                    FadeIn(right_dot),
                    run_time=0.4
                )

                # Prepare for next level
                new_dots.extend([left_dot, right_dot])
                new_positions.extend([left, right])

            current_dots = new_dots
            current_positions = new_positions

        self.wait(1)
        self.play(FadeOut(tree_elements))

        # Exponential curve overlay
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 20, 5],
            axis_config={"color": WHITE}
        ).scale(0.6)

        curve = axes.plot(lambda x: 2**x, color=RED)
        graph_label = axes.get_graph_label(curve, label="2^n")

        self.play(Create(axes), Create(curve), FadeIn(graph_label))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(graph_label), FadeOut(axes), FadeOut(curve))


### -- TRANSITION FROM INTRO TO BODY -- ###

class QuantumIntroScene(Scene):
    def construct(self):
        title = Text("Quantum computers solve this problem...", font_size=36).to_edge(UP)
        self.play(Write(title))
        # You can add visuals of quantum states, qubits, etc.
        self.wait(1)


## -- BEGINNING OF THE BODY OF THE VIDEO -- ##


class Video_body(Scene):
    def construct(self):
        title = Text("Concepts that are key towards understanding quantum computers", font_size=36)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))


class bitIntro(Scene):
    def construct(self):
       
         # Title at the top
        title = Text("A brief intro to bits").to_edge(UP)
        self.play(Write(title))

        # --- Classic bit on the right ---
       
        dot1 = Dot(radius=0.1, color=RED)
        classic_label = Text("Classic bit", font_size=20)
        dot1_label = Text("0 or 1", font_size=16)

        # Arrange: label on top, dot in middle, 0/1 label at bottom
        classic_group = VGroup(classic_label, dot1, dot1_label).arrange(DOWN, buff=0.3)
        classic_group.to_edge(RIGHT, buff=3)

        # --- Quantum bit on the left ---
        qubit_label = Text("Quantum bit", font_size=20)
        circ = Circle(radius=1, color=RED)

        dot2 = Dot(radius=0.1, color=RED).move_to(circ.point_at_angle(PI / 2))
        dot3 = Dot(radius=0.1, color=RED).move_to(circ.point_at_angle(-PI / 2))

        circ_label = Text("0, 1, or  00, 10, 01, 11", font_size=16).next_to(circ, DOWN, buff=0.2)

        quantum_graphic = VGroup(circ, dot2, dot3, circ_label)
        quantum_group = VGroup(qubit_label, quantum_graphic).arrange(DOWN, buff=0.3)
        quantum_group.to_edge(LEFT, buff=3)

        # --- Align both vertically ---
        # Make both bottom-aligned to match
        #classic_group.move_to(quantum_group, aligned_edge=DOWN)

        # --- Animate everything ---
        self.play(FadeIn(classic_group), FadeIn(quantum_group))
        self.wait(2)

        # Classic bit color change
        self.play(dot1.animate.set_color(BLUE))
        self.play(dot1.animate.set_color(YELLOW))
        self.wait()

        # Quantum bit rotation + color
        # can both be 1, 0, or diff values
        self.play(dot2.animate.set_color(BLUE), dot3.animate.set_color(BLUE))
        self.wait()
        self.play(dot2.animate.set_color(YELLOW), dot3.animate.set_color(YELLOW))
        self.wait()
        self.play(dot2.animate.set_color(BLUE), dot3.animate.set_color(YELLOW))
        self.wait()
        self.play(dot2.animate.set_color(YELLOW), dot3.animate.set_color(BLUE))
        self.wait()

        # rotation
        self.play(
            Rotate(VGroup(dot2, dot3), angle=2 * PI, about_point=circ.get_center()),
            run_time=3
        )
        self.wait(1)
        self.play(FadeOut(title), FadeOut(classic_group), FadeOut(quantum_group), FadeOut(quantum_graphic))


## 1. Superposition

class Superposition(Scene):
    def construct(self):
       
        title = Text("Superposition").to_edge(UP)
        self.play(Write(title))

        # Coin body: thin cylinder

        radius = 1
        height = 0.1

        # Create front face (gold)
        top = Dot(radius=radius, color=GOLD_D, fill_opacity=1).move_to(OUT * height / 2)
        front_text = Text("Heads", font_size=24).move_to(top.get_center())

        # Create back face (red)
        bottom = top.copy().set_color(RED).move_to(IN * height / 2)

        # Edge of the coin
        edge = Cylinder(radius=radius, height=height).set_fill(GREY, opacity=1)

        # Combine all parts
        coin = VGroup(edge, top, bottom, front_text)

        self.play(FadeIn(coin))
        self.wait(0.5)

        # Flip multiple times
        for _ in range(20):
            self.play(Rotate(coin, angle=PI, axis=UP), run_time=0.18)

        self.wait(30)
        self.play(FadeOut(coin))
        self.play(FadeOut(title))
        # self.wait(2)


class EntanglementScene(ThreeDScene):
    def construct(self):
       
        title = Text("Entanglement").to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        self.set_camera_orientation(phi=60 * DEGREES, theta=90 * DEGREES)
        # axes = ThreeDAxes()

        # Create 3D cubes
        cube1 = Cube(side_length=1, fill_opacity=0.7, fill_color=BLUE).move_to(LEFT * 1.5)
        cube2 = Cube(side_length=1, fill_opacity=0.7, fill_color=BLUE).move_to(RIGHT * 1.5)
        cubes = VGroup(cube1, cube2)
        self.add(cube1, cube2)

        def get_arrow():
            p1 = self.camera.project_point(cube1.get_center() + RIGHT * 0.5)
            p2 = self.camera.project_point(cube2.get_center() + LEFT * 0.5)
            return DoubleArrow(p1, p2, color=YELLOW, stroke_width=4)

        arrow = always_redraw(get_arrow)
        self.add_fixed_in_frame_mobjects(arrow)

        self.wait(12)
        self.play(
            cube1.animate.shift(LEFT * 2),
            cube2.animate.shift(RIGHT * 2),
            run_time=2
        )

        arrow_label = Text("The ends of the globe", font_size=20).move_to(UP * 0.5)
        self.add_fixed_in_frame_mobjects(arrow_label)
        self.play(FadeIn(arrow_label))
        self.wait(20)

        self.play(FadeOut(cubes), FadeOut(arrow), FadeOut(arrow_label), FadeOut(title))
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait(2)

class SpookyToParallelism(Scene):
    def construct(self):
        # First part: Einstein quote
        einstein_quote = Text("Einstein called this “spooky action at a distance.”", font_size=30)
        self.play(Write(einstein_quote))
        self.wait(2)

        # Fade out the quote
        self.play(FadeOut(einstein_quote))
        self.wait(0.5)

        # Second part: build up to parallelism
        question = Text("So, what happens when we combine superposition and entanglement?", font_size=30)
        self.play(Write(question))
        self.wait(2)

        # Fade out the question
        self.play(FadeOut(question))
        self.wait(0.5)

        # Dramatic reveal: parallelism
        reveal = Text("We get quantum parallelism.", font_size=36, color=BLUE)
        self.play(FadeIn(reveal, scale=1.2))
        self.wait(2)

        self.play(FadeOut(reveal))


class QuantumParallelism(Scene):
    def construct(self):
       
        # --- Title ---
        title = Text("Quantum Parallelism").to_edge(UP)
        self.play(Write(title))

        # --- First Visualization: Clues activating sequentially ---
        line = Line(LEFT * 4, RIGHT * 4)

        # Create 11 dots along the line
        points = [Dot(point=line.point_from_proportion(i / 10)) for i in range(11)]

        # Label only the first and last
        point_A = Text("Clue 1").next_to(points[0], LEFT, buff=0.2)
        point_end = Text("Conclusion").next_to(points[-1], RIGHT, buff=0.2)

        for point in points:
            point.set_color(WHITE)

        self.play(FadeIn(line, *points, point_A, point_end))

        # Sequential highlight animation
        for i, point in enumerate(points):
            self.play(point.animate.set_color(RED), run_time=0.3)
            if i > 0:
                self.play(points[i-1].animate.set_color(WHITE), run_time=0.3)

        self.wait()
        self.play(FadeOut(line, *points, point_A, point_end))

        # --- Second Visualization: Parallel lines converging ---
        start_x = -5
        end_x = 4
        y_positions = [2, 1, -1, -2]

        start_dots = VGroup()
        lines = VGroup()

        # Create end dot
        end_dot = Dot(point=[end_x, 0, 0], color=WHITE)
        end_text = Text("Conclusion").next_to(end_dot, RIGHT, buff=0.4)

        for y in y_positions:
            dot = Dot(point=[start_x, y, 0], color=WHITE)
            line = Line(dot.get_center(), end_dot.get_center(), color=WHITE)
            start_dots.add(dot)
            lines.add(line)

        start_text = Text("Clues").next_to(start_dots, UP, buff=0.5)

        self.play(FadeIn(start_dots, end_dot, start_text, end_text))
        self.wait(0.5)

        self.play(*[
            GrowFromPoint(line, dot.get_center())
            for line, dot in zip(lines, start_dots)
        ], run_time=1)

        self.wait(1)



### --- THE END OF THE VIDEO --- ###




class QuantumChallenge(Scene):
    def construct(self):
        title = Text("Why Aren’t We Using It Everywhere?").to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Split the sentence to place the absolute zero value between
        text_before = Text("Qubits need to stay", font_size=28)
        abs_zero = Text("≈ -273.15°C", color=BLUE, font_size=28)
        text_after = Text("just to stay stable", font_size=28)

        # Arrange them horizontally
        full_sentence = VGroup(text_before, abs_zero, text_after).arrange(RIGHT, buff=0.4).move_to(UP * 0.5)
        self.play(FadeIn(full_sentence))
        self.wait(1.5)

        # Additional space cold fact
        space_text = Text("That’s colder than outer space!", font_size=26).next_to(full_sentence, DOWN, buff=0.6)
        self.play(Write(space_text))
        self.wait(1.5)

        # Sensitive to decoherence
        sensitive_text = Text("Qubits are extremely sensitive...", font_size=26).shift(DOWN * 1)
        decoherence = Text("Decoherence", color=RED, font_size=30).next_to(sensitive_text, DOWN, buff=0.3)
        self.play(FadeIn(sensitive_text), FadeIn(decoherence))
        self.wait(30)

        # Fade everything out to move to the next scene
        self.play(FadeOut(title, full_sentence, space_text, sensitive_text, decoherence))


class QuantumImpact(Scene):
    def construct(self):
        title = Text("What Could Quantum Computers Do?").to_edge(UP)
        self.play(Write(title))

        # Industries as circles + text
        labels = [
            "Cybersecurity",
            "Medicine",
            "Logistics",
            "Climate"
        ]

        circles = VGroup()
        for i, label in enumerate(labels):
            circle = Circle(radius=0.5, color=WHITE)
            text = Text(label, font_size=24)
            group = VGroup(circle, text).arrange(DOWN, buff=0.2).move_to(LEFT * 3 + RIGHT * i * 2)
            circles.add(group)

        self.play(LaggedStart(*[FadeIn(c) for c in circles], lag_ratio=0.3))
        self.wait(21)
        self.play(FadeOut(circles))

class QuantumWrapUp(Scene):
    def construct(self):
       
        lines = [
            "Quantum computing isn’t just a better computer...",
            "It’s a new way of solving problems.",
            "Superposition. Entanglement. Parallelism.",
            "It could transform science, industries, and our future."
        ]

        text_mobjects = VGroup()

        for i, line in enumerate(lines):
            t = Text(line, font_size=28).move_to(DOWN * (i - 1.5))
            text_mobjects.add(t)
            self.play(Write(t))
            self.wait(1)

        self.wait(2)

        self.play(FadeOut(text_mobjects))

        title = Text("Welcome to the Quantum Age", font_size=36).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(2)


class TransitiontoSuper(Scene):
    def construct(self):
        title = Text("The potential to be both...until it's caught", font_size=24)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait()


class CreditsScene(Scene):
    def construct(self):
        
        # Placeholder names and roles
        credits = [
            ("Amrita Konaje", "Animator"),
            ("Sydney Metz", "Scriptwriter and Researcher"),
            ("Maxton Gibbs", "Storyboard Artist and Researcher"),
            ("Siddh Saxena", "Researcher"),
            ("George O'Carroll", "Researcher")
        ]

        entries = []

        for name, role in credits:
            name_text = Text(name, font_size=32, color=WHITE)
            role_text = Text(role, font_size=24, color=WHITE)
            entry = VGroup(name_text, role_text).arrange(DOWN, center=True, buff=0.1)
            entries.append(entry)

       
        # Stack all entries vertically and center them
        credit_group = VGroup(*entries).arrange(DOWN, center=True, buff=0.5)

        # Start below the screen
        start_y = -config.frame_height / 2 - credit_group.height / 2
        end_y = config.frame_height / 2 + credit_group.height / 2

        credit_group.move_to([0, start_y, 0])

        # Animate full scroll off screen
        self.add(credit_group)
        self.play(credit_group.animate.move_to([0, end_y, 0]), run_time=10, rate_func=linear)

