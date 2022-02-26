## Exercise 2 
Call exercise 2a: 
    python3 exercise_02a_thresh.py exercise_02a_input_01.pgm value exercise_02a_output_01.pgm
    example : python3 exercise_02a_thresh.py cam_74.pgm 100 cam_74_threshold100Exercise.pgm

Call exercise 2b:
    python3 exercise_02b_compare.py exercise_02b_input_01.pgm exercise_02b_input_02.pgm
    example1 : python3 exercise_02b_compare.py cam_74.pgm cam_74_threshold100Exercise.pgm (the result is 0)
    example2 : python3 exercise_02b_compare.py cam_74_threshold100.pgm cam_74_threshold100Exercise.pgm (the result is 1)
    
Call exercise 2c:
    python3 exercise_02c_sup.py exercise_02c_input_01.pgm exercise_02c_input_02.pgm exercise_02c_output_01.pgm
    example: python3 exercise_02c_sup.py image1.pgm image2.pgm exercise_02c_sup_output_01.pgm
    python3 exercise_02c_inf.py exercise_02c_input_01.pgm exercise_02c_input_02.pgm exercise_02c_output_01.pgm
    example: python3 exercise_02c_inf.py image1.pgm image2.pgm exercise_02c_inf_output_01.pgm
    
Call exercise 3a:
    python3 exercise_03a_erosion.py i exercise_03a_input_01.pgm exercise_03a_output_01.pgm
    python3 exercise_3a_erosion.py 1 immed_gray_inv.pgm output_erosion_1.pgm
    python3 exercise_3a_erosion.py 2 immed_gray_inv.pgm output_erosion_2.pgm
    
Call exercise 3b:
    python3 exercise_03a_dilatation.py i exercise_03a_input_01.pgm exercise_03a_output_01.pgm
    python3 exercise_3a_dilatation.py 1 immed_gray_inv.pgm output_dilatation_1.pgm
    python3 exercise_3a_dilatation.py 2 immed_gray_inv.pgm output_dilatation_2.pgm

python3 compare.py immed_gray_inv_20051123_dil2.pgm output_dilatation_2.pgm