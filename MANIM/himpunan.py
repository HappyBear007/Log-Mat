from manim import *

class SetHimpunan(Scene):
    def construct(self):
        
        # 1. enumerasi
        title  = Text('ENUMERASI')
        title.to_edge(UP)
        
        set_A  = Text('A={1,2,3,4}')
        set_B  = Text('B={2,4,6,8,10}')
        set_C  = Text('C={1,2,...,100}')
        
        VGroup(title, set_A, set_B, set_C).arrange(DOWN, center=True)
        
        set_A.next_to(title, DOWN, aligned_edge=LEFT)  
        set_B.next_to(set_A, DOWN, aligned_edge=LEFT)  
        set_C.next_to(set_B, DOWN, aligned_edge=LEFT)

        self.play(Write(title))
        self.play(Write(set_A))
        self.play(Write(set_B))
        self.play(Write(set_C))
        self.wait(5)
        
        self.play(FadeOut(Group(title, set_A, set_B, set_C)))
        
        
        # keanggotaan
        judul  = Text('Keanggotaan')
        judul.to_edge(UP)
        
        set_one   = Text('A={1,2,3}, R={a,b,{a,b,c}}')
        set_two   = Text('maka :')
        set_three = Text('3 ∈ A')
        set_four  = Text('{a, b, c} ∈ R')
        
        VGroup(judul, set_one, set_two, set_three).arrange(DOWN, center=True)
        
        set_one.move_to(ORIGIN)
        set_two.next_to(set_one, DOWN).align_to(set_one, LEFT)
        set_three.next_to(set_two, DOWN).align_to(set_one, LEFT)
        set_four.next_to(set_three, DOWN).align_to(set_one, LEFT)

        self.play(Write(judul))
        self.play(Write(set_one))
        self.play(Write(set_two))
        self.play(Write(set_three))
        self.play(Write(set_four))
        self.wait(5)
        
        self.play(FadeOut(Group(judul, set_one, set_two, set_three, set_four)))
        
        
        # 2. diagram venn
        #A. HIMPUNAN IRISAN
        irisan_A = Circle(radius=1.5, color=BLUE, fill_opacity=0.6)
        irisan_B = Circle(radius=1.5, color=PURPLE, fill_opacity=0.6)

        irisan_A.shift(LEFT)
        irisan_B.shift(RIGHT)

        self.play(Create(irisan_A), Create(irisan_B))
        self.wait(1)

        irisan_label = Tex("Contoh irisan himpunan}", color=WHITE)
        irisan_label.to_edge(LEFT).to_edge(UP)
        irisan_A_label = Tex("A = \\{1, 2, 3, 4, 5\\}", color=WHITE)
        irisan_A_label.next_to(irisan_label, DOWN).align_to(irisan_label, LEFT)
        irisan_B_label = Tex("B = \\{2, 3, 5, 7, 11\\}", color=WHITE)
        irisan_B_label.next_to(irisan_A_label, DOWN).align_to(irisan_A_label, LEFT)
        anb_label = Tex("$A \\cap B = \\{2, 3, 5\\}$", color=WHITE)
        anb_label.next_to(irisan_B_label, DOWN).align_to(irisan_B_label, LEFT)
        
        self.play(Create(irisan_label))
        self.wait(1)
        
        self.play(Create(irisan_A_label), Create(irisan_B_label), Create(anb_label))
        self.wait(1)

        
        # anggota himpunan A di dalam lingkaran A
        iris_label_A1 = Tex("1", color=WHITE).scale(0.7)
        iris_label_A1.move_to(irisan_A.get_center() + UP * 0.5)
        self.play(Create(iris_label_A1))
        self.wait(0.5)

        iris_label_A2 = Tex("4", color=WHITE).scale(0.7)
        iris_label_A2.move_to(irisan_A.get_center())
        self.play(Create(iris_label_A2))
        self.wait(0.5)


        # anggota himpunan B di dalam lingkaran B
        iris_label_B1 = Tex("7", color=WHITE).scale(0.7)
        iris_label_B1.move_to(irisan_B.get_center() + UP * 0.5)
        self.play(Create(iris_label_B1))
        self.wait(0.5)

        iris_label_B2 = Tex("11", color=WHITE).scale(0.7)
        iris_label_B2.move_to(irisan_B.get_center())
        self.play(Create(iris_label_B2))
        self.wait(0.5)


        # anggota himpunan yang ada di antara A dan B
        iris_label_3 = Tex("2", color=WHITE).scale(0.7)
        iris_label_3.move_to((irisan_A.get_center() + irisan_B.get_center()) / 2 + UP * 0.5)
        self.play(Create(iris_label_3))
        self.wait(0.5)

        iris_label_4 = Tex("3", color=WHITE).scale(0.7)
        iris_label_4.move_to((irisan_A.get_center() + irisan_B.get_center()))
        self.play(Create(iris_label_4))
        self.wait(0.5)

        iris_label_5 = Tex("5", color=WHITE).scale(0.7)
        iris_label_5.move_to((irisan_A.get_center() + irisan_B.get_center()) / 2 + DOWN * 0.5)
        self.play(Create(iris_label_5))
        self.wait(0.5)

        self.play(
            FadeOut(Group(irisan_A, irisan_B, irisan_label, irisan_A_label, irisan_B_label, anb_label, iris_label_A1, iris_label_A2, iris_label_B1, iris_label_B2, iris_label_3, iris_label_4, iris_label_5))
        )
        self.wait(1)
        #BATAS HIMPUNAN IRISAN
        
        
        #B. HIMPUNAN GABUNGAN (UNION)
        circle_A = Circle(radius=1.5, color=PINK, fill_opacity=0.6)
        circle_B = Circle(radius=1.5, color=YELLOW, fill_opacity=0.6)

        circle_A.shift(LEFT)
        circle_B.shift(RIGHT)

        self.play(Create(circle_A), Create(circle_B))
        self.wait(1)

        examp_label = Tex("Contoh himpunan gabungan (union)", color=WHITE)
        examp_label.to_edge(LEFT).to_edge(UP)
        universe_label = Tex("U = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}", color=WHITE)
        universe_label.next_to(examp_label, DOWN).align_to(examp_label, LEFT)
        himp_A_label = Tex("A = \\{1, 2, 3, 4, 6\\}", color=WHITE)
        himp_A_label.next_to(universe_label, DOWN).align_to(universe_label, LEFT)
        himp_B_label = Tex("B = \\{3, 4, 7, 8, 10\\}", color=WHITE)
        himp_B_label.next_to(himp_A_label, DOWN).align_to(himp_A_label, LEFT)
        
        self.play(Create(examp_label), Create(universe_label))
        self.wait(1)
        
        self.play(Create(himp_A_label), Create(himp_B_label))
        self.wait(1)

        
        # anggota himpunan A di dalam lingkaran A
        elem_label_A1 = Tex("1", color=WHITE).scale(0.7)
        elem_label_A1.move_to(circle_A.get_center() + UP * 0.5)
        self.play(Create(elem_label_A1))
        self.wait(0.5)

        elem_label_A2 = Tex("2", color=WHITE).scale(0.7)
        elem_label_A2.move_to(circle_A.get_center())
        self.play(Create(elem_label_A2))
        self.wait(0.5)

        elem_label_A3 = Tex("6", color=WHITE).scale(0.7)
        elem_label_A3.move_to(circle_A.get_center() + DOWN * 0.5)
        self.play(Create(elem_label_A3))
        self.wait(0.5)

        # anggota himpunan B di dalam lingkaran B
        elem_label_B1 = Tex("7", color=WHITE).scale(0.7)
        elem_label_B1.move_to(circle_B.get_center() + UP * 0.5)
        self.play(Create(elem_label_B1))
        self.wait(0.5)

        elem_label_B2 = Tex("8", color=WHITE).scale(0.7)
        elem_label_B2.move_to(circle_B.get_center())
        self.play(Create(elem_label_B2))
        self.wait(0.5)

        elem_label_B3 = Tex("10", color=WHITE).scale(0.7)
        elem_label_B3.move_to(circle_B.get_center() + DOWN * 0.5)
        self.play(Create(elem_label_B3))
        self.wait(0.5)

        # anggota himpunan yang ada di antara A dan B
        elem_label_3 = Tex("3", color=WHITE).scale(0.7)
        elem_label_3.move_to((circle_A.get_center() + circle_B.get_center()) / 2 + UP * 0.5)
        self.play(Create(elem_label_3))
        self.wait(0.5)

        elem_label_4 = Tex("4", color=WHITE).scale(0.7)
        elem_label_4.move_to((circle_A.get_center() + circle_B.get_center()) / 2 + DOWN * 0.5)
        self.play(Create(elem_label_4))
        self.wait(0.5)

        # anggota himpunan yang ada di luar A dan B
        elem_label_5 = Tex("5", color=WHITE).scale(0.7)
        elem_label_5.move_to(RIGHT * 2 + UP * 1.5)
        self.play(Create(elem_label_5))
        self.wait(0.5)

        self.play(
            FadeOut(Group(examp_label, universe_label, himp_A_label, himp_B_label, circle_A, circle_B, elem_label_A1, elem_label_A2, elem_label_A3,
                          elem_label_B1, elem_label_B2, elem_label_B3, elem_label_3, elem_label_4, elem_label_5))
        )
        self.wait(1)
        #BATAS HIMPUNAN GABUNGAN (UNION)
        
        
        #C. SELISIH HIMPUNAN
        selisih_A = Circle(radius=1.5, color=GREEN, fill_opacity=0.6)
        selisih_B = Circle(radius=1.5, color=RED, fill_opacity=0.6)

        selisih_A.shift(LEFT)
        selisih_B.shift(RIGHT)

        self.play(Create(selisih_A), Create(selisih_B))
        self.wait(1)

        selisih_label = Tex("Contoh selisih himpunan}", color=WHITE)
        selisih_label.to_edge(LEFT).to_edge(UP)
        selisih_A_label = Tex("A = \\{1, 2, 3, 4, 5\\}", color=WHITE)
        selisih_A_label.next_to(selisih_label, DOWN).align_to(selisih_label, LEFT)
        selisih_B_label = Tex("B = \\{2, 3, 5, 7, 11\\}", color=WHITE)
        selisih_B_label.next_to(selisih_A_label, DOWN).align_to(selisih_A_label, LEFT)
        ab_label = Tex("$A - B = \\{1, 4\\}$", color=WHITE)
        ab_label.next_to(selisih_B_label, DOWN).align_to(selisih_B_label, LEFT)
        
        self.play(Create(selisih_label))
        self.wait(1)
        
        self.play(Create(selisih_A_label), Create(selisih_B_label), Create(ab_label))
        self.wait(1)

        
        # anggota himpunan A di dalam lingkaran A
        selisih_label_A1 = Tex("1", color=WHITE).scale(0.7)
        selisih_label_A1.move_to(selisih_A.get_center() + UP * 0.5)
        self.play(Create(selisih_label_A1))
        self.wait(0.5)

        selisih_label_A2 = Tex("4", color=WHITE).scale(0.7)
        selisih_label_A2.move_to(selisih_A.get_center())
        self.play(Create(selisih_label_A2))
        self.wait(0.5)

        # anggota himpunan B di dalam lingkaran B
        selisih_label_B1 = Tex("7", color=WHITE).scale(0.7)
        selisih_label_B1.move_to(selisih_B.get_center() + UP * 0.5)
        self.play(Create(selisih_label_B1))
        self.wait(0.5)

        selisih_label_B2 = Tex("11", color=WHITE).scale(0.7)
        selisih_label_B2.move_to(selisih_B.get_center())
        self.play(Create(selisih_label_B2))
        self.wait(0.5)


        # anggota himpunan yang ada di antara A dan B
        selisih_label_3 = Tex("2", color=WHITE).scale(0.7)
        selisih_label_3.move_to((selisih_A.get_center() + selisih_B.get_center()) / 2 + UP * 0.5)
        self.play(Create(selisih_label_3))
        self.wait(0.5)

        selisih_label_4 = Tex("3", color=WHITE).scale(0.7)
        selisih_label_4.move_to((selisih_A.get_center() + selisih_B.get_center()))
        self.play(Create(selisih_label_4))
        self.wait(0.5)

        selisih_label_5 = Tex("5", color=WHITE).scale(0.7)
        selisih_label_5.move_to((selisih_A.get_center() + selisih_B.get_center()) / 2 + DOWN * 0.5)
        self.play(Create(selisih_label_5))
        self.wait(0.5)

        self.play(
            FadeOut(Group(selisih_A, selisih_B, selisih_label, selisih_A_label, selisih_B_label, ab_label, selisih_label_A1, selisih_label_A2, selisih_label_B1, selisih_label_B2, selisih_label_3, selisih_label_4, selisih_label_5))
        )
        self.wait(1)
        #BATAS SELISIH HIMPUNAN
        
        
        #C. KOMPLEMEN HIMPUNAN
        komplemen_A = Circle(radius=1.5, color=ORANGE, fill_opacity=0.6)
        # komplemen_A.shift()

        self.play(Create(komplemen_A))
        self.wait(1)

        komp_label = Tex("Contoh komplemen himpunan", color=WHITE)
        komp_label.to_edge(LEFT).to_edge(UP)
        komplemen_label = Tex("S = \\{1, 2, 3, 4, 5, 6, 7\\}", color=WHITE)
        komplemen_label.next_to(komp_label, DOWN).align_to(komp_label, LEFT)
        komp_A_label = Tex("A = \\{1, 3, 5, 7\\}", color=WHITE)
        komp_A_label.next_to(komplemen_label, DOWN).align_to(komplemen_label, LEFT)
        komp_B_label = Tex("$A^{C}$ = \\{3, 4, 7, 8, 10\\}", color=WHITE)
        komp_B_label.next_to(komp_A_label, DOWN).align_to(komp_A_label, LEFT)
        
        self.play(Create(komp_label), Create(komplemen_label))
        self.wait(1)
        
        self.play(Create(komp_A_label), Create(komp_B_label))
        self.wait(1)

        
        # anggota himpunan A di dalam lingkaran A
        komp_label_A1 = Tex("1", color=WHITE).scale(0.7)
        komp_label_A1.move_to(komplemen_A.get_center() + UP * 0.5)
        self.play(Create(komp_label_A1))
        self.wait(0.5)

        komp_label_A2 = Tex("3", color=WHITE).scale(0.7)
        komp_label_A2.move_to(komplemen_A.get_center())
        self.play(Create(komp_label_A2))
        self.wait(0.5)

        komp_label_A3 = Tex("5", color=WHITE).scale(0.7)
        komp_label_A3.move_to(komplemen_A.get_center() + DOWN * 0.5)
        self.play(Create(komp_label_A3))
        self.wait(0.5)
        
        komp_label_A4 = Tex("7", color=WHITE).scale(0.7)
        komp_label_A4.move_to(komplemen_A.get_center() + RIGHT * 0.5)
        self.play(Create(komp_label_A4))
        self.wait(0.5)

        # anggota himpunan yang ada di luar A
        komp_label_5 = Tex("2", color=WHITE).scale(0.7)
        komp_label_5.move_to(RIGHT * 2 + UP * 1.5)
        self.play(Create(komp_label_5))
        self.wait(0.5)
        
        komp_label_6 = Tex("4", color=WHITE).scale(0.7)
        komp_label_6.move_to(RIGHT * 3 + UP * 2)
        self.play(Create(komp_label_6))
        self.wait(0.5)
        
        komp_label_7 = Tex("6", color=WHITE).scale(0.7)
        komp_label_7.move_to(RIGHT * 4 + UP * 2.5)
        self.play(Create(komp_label_7))
        self.wait(0.5)

        self.play(
            FadeOut(Group(komplemen_A, komp_label, komplemen_label, komp_A_label, komp_B_label,
                          komp_label_A1, komp_label_A2, komp_label_A3, komp_label_A4, komp_label_5, komp_label_6, komp_label_7))
        )
        self.wait(1)
        #BATAS KOMPLEMEN HIMPUNAN
        
if __name__ == "__main__":
    scene = SetHimpunan()
    scene.render()