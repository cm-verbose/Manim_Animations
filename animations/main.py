from manim import *

#
# manim.cfg 
#
# frame_rate = 120
# pixel_height = 720
# pixel_width = 1280
# background_color = 0xFAF0E6
# background_opacity = 1
# scene_names = Physics
# 

class Physics(Scene):
    def construct(self):
        center = self.play_time_formula_definition()
        self.play_calculate_time(center) 
        center_2 = self.play_speed_formula_definition()
        self.play_calculate_speeds(center_2)
        self.play_calculate_average_speed()
        self.play_calculate_projectile_reach()
        self.play_graph_display() 
        self.play_caculate_experimental_corelation() 
        self.play_calculate_difference()
        self.wait(1)
    
    # indicating the formula and transitioning 
    def play_time_formula_definition(self): 
        formula = MathTex(r"p = v\Delta t").set_color(0)
        self.play(Write(formula), run_time=0.75) 
        self.wait(0.5)
        color_animations = [
            formula[0][3:].animate.set_color(0xED2939), 
            formula[0][:3].animate.set_color(0xFAF0E6), 
        ]
        self.play(*color_animations, run_time=0.75)
        self.play(ApplyMethod(formula[0][3:].move_to, ORIGIN))
        self.wait(1)
        self.play(FadeOut(formula), run_time=1e-5)
        return formula[0][3:].get_center()
    
    # shows steps to calculate delta t 
    def play_calculate_time(self, center):
        time = MathTex(r"\Delta t = \sqrt{\frac{2h}{g}}")
        delta_t = time[0][:2].set_color(0xED2939)
        root = time[0][2:].set_color(0xFAF0E6)
        delta_t.move_to(center)
        root.next_to(delta_t, RIGHT)
        self.add(delta_t, root)

        self.play(ApplyMethod(time.move_to, ORIGIN), run_time=0.75)
        self.play(root.animate.set_color(0))
        self.wait(1)
        self.play(time[0][6].animate.set_color(0x246BCE))
        self.wait(1)

        p = r"\Delta t = "
        matching_substutions = [
            MathTex(p + r"\sqrt{\frac{2(45\mathrm{cm})}{g}}"),
            MathTex(p + r"\sqrt{\frac{2(45\mathrm{cm})}{9.8\mathrm{m}/\mathrm{s}^2}}"),
            MathTex(p + r"\sqrt{\frac{90\mathrm{cm}}{9.8\mathrm{m}/\mathrm{s}^2}}"),
            MathTex(p + r"\sqrt{\frac{0.90\mathrm{m}}{9.8\mathrm{m}/\mathrm{s}^2}}"),
            MathTex(p + r"\sqrt{0.0918\mathrm{s}^2}"),
            MathTex(p + r"0.3029851481508623\mathrm{s}"),
            MathTex(r"\Delta t \approx 0.30\mathrm{s}"),
        ]

        for i, substitution in enumerate(matching_substutions):
            substitution.set_color(0)
            substitution[0][:2].set_color(0xED2939)
            self.play(
                TransformMatchingTex(time, substitution) if i == 0 
                else TransformMatchingTex(matching_substutions[i - 1], substitution)
            )

        self.play(FadeOut(matching_substutions[len(matching_substutions) - 1]))
        self.wait(1)

    # Indicates the formula to compute v
    def play_speed_formula_definition(self):
        formula = MathTex(r"p = v\Delta t").set_color(0)
        self.play(Write(formula))
        color_animations = [
            formula[0][:2].animate.set_color(0xFAF0E6), 
            formula[0][2].animate.set_color(0x62D095),
            formula[0][3:].animate.set_color(0xFAF0E6), 
        ]
        self.play(*color_animations)
        self.play(ApplyMethod(formula[0][2].move_to, ORIGIN))
        self.wait(1)
        self.play(FadeOut(formula[0][2]), run_time=1e-5)
        return formula[0][2].get_center() 
    
    # Calculate the 5 theoretical speeds from obtained data
    def play_calculate_speeds(self, center): 
        formula = MathTex(r"v = \frac{\Delta x}{\Delta t}").set_color(0) 
        v = formula[0][0].set_color(0x62D095).set_z_index(6)
        rest = formula[0][1:].set_color(0xFAF0E6).set_z_index(5)
        v.move_to(center)
        self.add(v, rest)
        self.wait(1)
        self.play(ApplyMethod(v.move_to, LEFT * rest.width))
        rest.next_to(v, RIGHT)
        rest.shift(UP * (v.get_y() + 0.05))
        self.play(rest.animate.set_color(0))
        
        # collected data 
        dt_v = [0.055, 0.110, 0.165, 0.220, 0.275, 0.330]
        dx_v = [0, 18, 27, 37, 48, 57]
        
        time_label = MathTex("\Delta t")
        distance_label = MathTex("\Delta x")
        
        table = DecimalTable(
            [ dt_v, dx_v ],
            row_labels=[time_label, distance_label],
            line_config={"stroke_width": 0.5, "color": 0xCCCCCC},
            element_to_mobject_config={"num_decimal_places": 3},
            include_outer_lines=True
        ).set_color(0)
        
    
        table.scale(0.5)
        table.move_to(UP * 2.25)
        self.play(FadeIn(table), run_time=0.75)
        
        equations = [
            MathTex(r"v_{1} = \frac{0 \mathrm{cm}}{0.055 \mathrm{s}}"),
            MathTex(r"v_{2} = \frac{18 \mathrm{cm}}{0.110 \mathrm{s}}"),
            MathTex(r"v_{3} = \frac{27 \mathrm{cm}}{0.165 \mathrm{s}}"),
            MathTex(r"v_{4} = \frac{37 \mathrm{cm}}{0.220 \mathrm{s}}"),
            MathTex(r"v_{5} = \frac{48 \mathrm{cm}}{0.275 \mathrm{s}}"),
            MathTex(r"v_{6} = \frac{57 \mathrm{cm}}{0.330 \mathrm{s}}"),
        ]
        
        equations[0].shift(LEFT * time_label.get_y(), UP * 1)
        
        for k, eq in enumerate(equations): 
            eq.set_color(0)
            eq.scale(0.5)
            if k == 0: 
                continue
            else: 
                eq.next_to(equations[k - 1], DOWN)
                
        self.play(TransformMatchingTex(formula, VGroup(*equations)))
        
        ans = [
            MathTex(r" = 0\mathrm{cm}/\mathrm{s}"),
            MathTex(r" = 163.63\mathrm{cm}/\mathrm{s}"),
            MathTex(r" = 163.63\mathrm{cm}/\mathrm{s}"),
            MathTex(r" = 168.18\mathrm{cm}/\mathrm{s}"),
            MathTex(r" = 174.54\mathrm{cm}/\mathrm{s}"),
            MathTex(r" = 172.77\mathrm{cm}/\mathrm{s}"),
        ]
        
        for k, eq in enumerate(equations):
            ans[k].set_color(0)
            ans[k].scale(0.5)
            ans[k].next_to(eq, RIGHT)
            self.play(FadeIn(ans[k]))
        
        self.play(ans[0][0][1:].animate.set_color(0xED2939))
        self.wait(0.5)
        self.play(FadeOut(ans[0]), FadeOut(equations[0]))
        self.wait(0.5)
        fadeGroup = [
            FadeOut(table),
            *[FadeOut(eq) for eq in equations],
            *[FadeOut(a) for a in ans]
        ]
        ans[0].set_color(0xFAF0E6)
        equations[0].set_color(0xFAF0E6)
        self.play(AnimationGroup(*fadeGroup))
        self.wait(1)
        
    def play_calculate_average_speed(self):
        formula = MathTex(r"\bar{v} = \frac{\sum v}{n}").set_color(0)
        self.play(Write(formula))
        f_2 = MathTex(
            r"""
            \tilde{v} =\frac{163.63\mathrm{cm}/\mathrm{s} + 163.63\mathrm{cm}/\mathrm{s} + \
            168.18\mathrm{cm}/\mathrm{s} + 174.54\mathrm{cm}/\mathrm{s} + 
            172.77\mathrm{cm}/\mathrm{s}}{5}
            """
        ).scale(0.75).set_color(0)
        self.play(TransformMatchingTex(formula, f_2))
        f_3 = MathTex(r"\bar{v} = 168.55\mathrm{cm}/\mathrm{s}").set_color(0)
        
        self.play(TransformMatchingTex(f_2, f_3))
        self.play(FadeOut(f_3))
    
    def play_calculate_projectile_reach(self):
        formula = MathTex(r"p = v\Delta t").set_color(0)
        self.play(Write(formula), run_time=0.75) 
        self.wait(0.5)
        color_change_animation = [
            formula[0][2].animate.set_color(0x62D095),
            formula[0][3:].animate.set_color(0xED2939)
        ]
        
        for anim in color_change_animation:
            self.play(anim)
            
        f_1 = MathTex(r"p &= 168.55\mathrm{cm}/\mathrm{s} \times 0.30 \mathrm{s}").set_color(0)
        self.play(TransformMatchingTex(formula, f_1))
        
        f_2 = MathTex(r"p &= 50.57 \mathrm{cm}").set_color(0)
        self.play(TransformMatchingTex(f_1, f_2))
        self.wait(0.5)
        self.play(FadeOut(f_2))
        self.wait(1)
    
    def play_graph_display(self):
        axes = Axes(
            x_range=[0, 0.33, 0.055], 
            y_range=[0, 60, 10],
            axis_config={"include_numbers": True},
            tips=False
        ).set_color(0)
        axes.width = 4
        axes.height = 6
        
        x_values = [0.055, 0.110, 0.165, 0.220, 0.275, 0.330]
        y_values = [0, 18, 27, 37, 48, 57]
        
        plot = axes.plot_line_graph(x_values=x_values, y_values=y_values)
        self.play(Write(axes))
        
        color_set = [0xF94144, 0xF8961E, 0xF9c74F, 0x90BE6D, 0x43AA8B, 0x577590]
        
        s = [] 
        d = []
        
        for k, dot in enumerate(plot["vertex_dots"]):
            dot.set_color(color_set[k]).set_z_index(8)
            label = MathTex(f"({x_values[k]}, {y_values[k]})").set_color(color_set[k]).scale(0.5)
            label.next_to(dot, RIGHT * 0.75 + UP * 0.75,).set_z_index(9)
            group = [
                FadeIn(dot),
                FadeIn(label),
            ]
            s.append(label)
            d.append(dot)
            self.play(AnimationGroup(*group), run_time=0.25)

        graph = axes.plot(lambda x: 200 * x - 7.333).set_z_index(7).set_color(0)
        graph.stroke_width = 1 
        
        self.play(FadeIn(graph))
        
        self.wait(1)
        
        fadeLabelGroup = [
            FadeOut(graph),
            FadeOut(axes),
            *[FadeOut(x) for x in s],
            *[FadeOut(x) for x in d]
        ]
        self.play(AnimationGroup(*fadeLabelGroup))
        self.wait(1)
    
    # Calculate the experimental corelation percentage 
    def play_caculate_experimental_corelation(self):
        formula = MathTex(
            r"r = \frac{n \sum{xy} - \sum{x} \sum{y}}{\sqrt{n \sum{x^2} - (\sum x)^2} \cdot \sqrt{n \sum{y^2} - (\sum{y})^2}}"
        ).set_color(0)
        self.play(Write(formula), run_time=0.75)
        
        f_1 = MathTex(
            r"r = \frac{6 \sum{xy} - \sum{x} \sum{y}}{\sqrt{6 \sum{x^2} - (\sum x)^2} \cdot \sqrt{6 \sum{y^2} - (\sum{y})^2}}"
        ).set_color(0)
        self.play(TransformMatchingTex(formula, f_1), run_time=0.75)
        
        steps = [
            MathTex(r"r = \frac{6 (46.59) - (1.155) \cdot (187)}{\sqrt{6(0.28) - (1.33)} \cdot \sqrt{6 (7975) - (34969)}}"),
            MathTex(r"r = \frac{63.56}{67.14}"),
            MathTex(r"r = 0.9466"),
            MathTex(r"r = 94.66\%"),
        ]
        
        for k, step in enumerate(steps):
            step.set_color(0)
            if(k == 0):
                self.play(TransformMatchingTex(f_1, steps[k]))
            else: 
                self.play(TransformMatchingTex(steps[k - 1], step))
            
        self.play(FadeOut(steps[len(steps) - 1])) 
    
    # Caculate the percentage of difference between reality and theory
    def play_calculate_difference(self):
        equation = MathTex(r"d = 1 - \frac{50.57\mathrm{cm}}{57\mathrm{cm}}").set_color(0)
        self.play(Write(equation), run_time=0.75)
        
        f_1 = MathTex(r"d = 1 - 0.88719298245").set_color(0)
        self.play(TransformMatchingTex(equation, f_1))
        
        f_2 = MathTex(r"d = 0.11280701754").set_color(0)
        self.play(TransformMatchingTex(f_1, f_2))
        
        f_3 = MathTex(r"d \approx 11.28\%").set_color(0)
        self.play(TransformMatchingTex(f_2, f_3))
        
        self.wait(0.5)
        self.play(FadeOut(f_3))
        
        self.wait(9)

