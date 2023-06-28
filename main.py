
if s == 16:
    l8.color,l9.color, l14.color, l15.color, l20.color, l21.color, l26.color, l27.color = color_for_1gr
    l10.color, l11.color, l16.color, l17.color, l22.color, l23.color, l28.color, l29.color = color_for_2gr
    l1.color, l2.color, l3.color, l4.color, l5.color, l6.color, l7.color, l12.color, l13.color, l18.color, l19.color, l24.color, l25.color, l30.color, l31.color, l32.color, l33.color, l34.color, l35.color, l36.color = zero_color
elif s == 24:
    l7.color, l8.color, l9.color, l13.color, l14.color, l15.color, l19.color, l20.color, l21.color, l25.color, l26.color, l27.color= color_for_1gr
    l10.color, l11.color, l12.color, l16.color, l17.color, l18.color, l22.color, l23.color, l24.color, l28.color, l29.color, l30.color = color_for_2gr
    l1.color, l2.color, l3.color, l4.color, l5.color, l6.color, l31.color, l32.color, l33.color, l34.color, l35.color, l36.color= zero_color
else:
    l1.color, l2.color, l3.color, l7.color, l8.color, l9.color, l13.color, l14.color, l15.color, l19.color, l20.color, l21.color, l25.color, l26.color, l27.color, l31.color, l32.color, l33.color = color_for_1gr
    l4.color, l5.color, l6.color, l10.color, l11.color, l12.color, l16.color, l17.color, l18.color, l22.color, l23.color, l24.color, l28.color, l29.color, l30.color, l34.color, l35.color, l36.color = color_for_2gr


size_line = [40, 500];
line_Width = 1;
l1_answer_2.lineWidth = line_Width;
l1_answer_2.ori = Mo;