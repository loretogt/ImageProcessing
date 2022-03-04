(All the following calls are inside the folder of the exercise)
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
    python3 exercise_3a_erosion.py i exercise_03a_input_01.pgm exercise_03a_output_01.pgm
    example: python3 exercise_3a_erosion.py 1 immed_gray_inv.pgm output_erosion_1.pgm
    example: python3 exercise_3a_erosion.py 2 immed_gray_inv.pgm output_erosion_2.pgm
    
Call exercise 3b:
    python3 exercise_3b_dilatation.py i exercise_03a_input_01.pgm exercise_03a_output_01.pgm
    example: python3 exercise_3b_dilatation.py 1 immed_gray_inv.pgm output_dilatation_1.pgm
    example: python3 exercise_3b_dilatation.py 2 immed_gray_inv.pgm output_dilatation_2.pgm

Call exercise 4a:
    python3 exercise_4a_opening.py i exercise_04a_input_01.pgm exercise_04a_output_01.pgm   
    example: python3 exercise_4a_opening.py 1 immed_gray_inv.pgm output_opening_1.pgm   
    example: python3 exercise_4a_opening.py 2 immed_gray_inv.pgm output_opening_2.pgm   

Call exercise 4b:
    python3 exercise_4b_closing.py i exercise_04a_input_01.pgm exercise_04a_output_01.pgm 
    example: python3 exercise_4b_closing.py 1 immed_gray_inv.pgm output_closing_1.pgm   
    example: python3 exercise_4b_closing.py 2 immed_gray_inv.pgm output_closing_2.pgm   

Call exercise 5a example:
    python3 Exercises_04ab/exercise_4a_opening.py 1 Exercises_05ab/cam_74.pgm Exercises_05ab/exercise_05a_output_01.pgm
    python3 Exercises_04ab/exercise_4a_opening.py 1 Exercises_05ab/exercise_05a_output_01.pgm Exercises_05ab/exercise_05a_output_02.pgm
    They are equal 
    
Call exercise 5b example:
    python3 Exercises_04ab/exercise_4a_closing.py 1 Exercises_05ab/cam_74.pgm Exercises_05ab/exercise_05a_output_01_c.pgm
    python3 Exercises_04ab/exercise_4a_closing.py 1 Exercises_05ab/exercise_05a_output_01_c.pgm Exercises_05ab/exercise_05a_output_02_c.pgm
    They are equal 

Call exercise 6a:
    python3 exercise_06a_closing_opening.py i exercise_06a_input_01.pgm exercise_06a_output_01.pgm 
    example: python3 exercise_06a_closing_opening.py 2 immed_gray_inv.pgm clos_op_2.pgm 
    example: python3 exercise_06a_closing_opening.py 4 immed_gray_inv.pgm clos_op_4.pgm 

Call exercise 6b:
    python3 exercise_06b_opening_closing.py i exercise_06a_input_01.pgm exercise_06a_output_01.pgm 
    example: python3 exercise_06b_opening_closing.py 2 immed_gray_inv.pgm op_clos_2.pgm
    example: python3 exercise_06b_opening_closing.py 4 immed_gray_inv.pgm op_clos_4.pgm

Call exercise 7a example:
    python3 Exercises_06ab/exercise_06a_closing_opening.py 1 Exercises_07ab/cam_74.pgm Exercises_07ab/exercise_07a_output_01_c.pgm
    python3 Exercises_06ab/exercise_06a_closing_opening.py 1 Exercises_07ab/exercise_07a_output_01_c.pgm Exercises_07ab/exercise_07a_output_02_c.pgm
    They are equal 
    
Call exercise 7b example:
    python3 Exercises_06ab/exercise_06b_opening_closing.py 1 Exercises_07ab/cam_74.pgm Exercises_07ab/exercise_07b_output_01_c.pgm
    python3 Exercises_06ab/exercise_06b_opening_closing.py 1 Exercises_07ab/exercise_07b_output_01_c.pgm Exercises_07ab/exercise_07b_output_02_c.pgm
    They are equal 
    
Call exercise 8b:
    Filter 1: python3 Exercises_04ab/exercise_4a_opening.py 1 Exercises_08a/isn_256.pgm Exercises_08a/filter1.pgm
    Filter 2: python3 Exercises_04ab/exercise_4a_closing.py 1 Exercises_08a/isn_256.pgm Exercises_08a/filter2.pgm
    Filter 3: python3 Exercises_06ab/exercise_06a_closing_opening.py 1 Exercises_08a/isn_256.pgm Exercises_08a/filter3.pgm
    Filter 4: python3 Exercises_06ab/exercise_06b_opening_closing.py 1 Exercises_08a/isn_256.pgm Exercises_08a/filter4.pgm

python3 compare.py immed_gray_inv_20051123_clo1.pgm output_closing_1.pgm




