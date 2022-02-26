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
    
    

python3 /Users/Loreto/Documents/Master/Image Processing, Analysis and Classification/Exercises/Ejercicios1/Exercises_02ab/exercise_02b_compare.py cam_74_threshold100.pgm cam_74_threshold100Exercise.pgm