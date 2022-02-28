
/**************************************************
   Simple example program to print some pixel values
   of the input image, and to display it.
   The first argument must contain the file name of
   the input image.
***************************************************/


#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>


using namespace std;
// using namespace cv;

int main( int argc, char *argv[] )
{
    if ( argc < 2 ) {
      cout << "Error: number of arguments: include input image file" << endl;
      return 1;
    }
    cv::Mat gImg1 = cv::imread( argv[ 1 ], cv::IMREAD_GRAYSCALE );


    // Copy of image
    cv::Mat gImg2 = gImg1.clone();


    // Basic method to access pixel (x, y), where x and y denote, respectively
    // the column and row coordinates:
    // Mat::at<type>( y, x )
    //
    // cv::Point() can be used if the order (column, row) is preferred:
    // Mat::at<type>( cv::Point( x, y) )
    //
    //
    // For 8-bit images, use the 'uchar' type:
    // Mat::at<uchar>( y, x )
    // or
    // Mat::at<uchar>( cv::Point( x, y ) )
  



    cout << "gImg2.rows: " << gImg2.rows << endl; 
    cout << "gImg2.cols: " << gImg2.cols << endl; 
    cout << "----------------------------------" << endl;
    cout << "Accessing pixel values by using at<uchar>(row, column):" << endl;
    cout << "(upper-left corner)  at<uchar>(0,0): " << (int) gImg2.at<uchar>( 0, 0 ) << endl;
    cout << "                     at<uchar>(0,1): " << (int) gImg2.at<uchar>( 0, 1 ) << endl;
    cout << "(upper-right corner) at<uchar>(0,255): " << (int) gImg2.at<uchar>( 0, ( gImg2.cols - 1 ) ) << endl;
    cout << "(lower-left corner)  at<uchar>(255,0): " << (int) gImg2.at<uchar>( ( gImg2.rows - 1 ), 0 ) << endl;
    cout << "(lower-right corner) at<uchar>(255,255): " << (int) gImg2.at<uchar>( ( gImg2.rows - 1 ), ( gImg2.cols - 1 ) ) << endl;
    cout << "----------------------------------" << endl;
    gImg2.at<uchar>( 0, 0 ) = 1;
    gImg2.at<uchar>( 0, 1 ) = 2;
    gImg2.at<uchar>( 0, ( gImg2.cols - 1 ) ) = 3;
    gImg2.at<uchar>( ( gImg2.rows - 1 ), 0 ) = 4;
    gImg2.at<uchar>( ( gImg2.rows - 1 ), ( gImg2.cols - 1 ) ) = 5;
    cout << "----------------------------------" << endl;
    cout << "After modifying those pixels values:" << endl;
    cout << "Accessing pixel values by using at<uchar>(row, column):" << endl;
    cout << "(upper-left corner)  at<uchar>(0,0): " << (int) gImg2.at<uchar>( 0, 0 ) << endl;
    cout << "                     at<uchar>(0,1): " << (int) gImg2.at<uchar>( 0, 1 ) << endl;
    cout << "(upper-right corner) at<uchar>(0,255): " << (int) gImg2.at<uchar>( 0, ( gImg2.cols - 1 ) ) << endl;
    cout << "(lower-left corner)  at<uchar>(255,0): " << (int) gImg2.at<uchar>( ( gImg2.rows - 1 ), 0 ) << endl;
    cout << "(lower-right corner) at<uchar>(255,255): " << (int) gImg2.at<uchar>( ( gImg2.rows - 1 ), ( gImg2.cols - 1 ) ) << endl;
    cout << "----------------------------------" << endl;

    cout << "Saving image output1.pgm ..." << endl;
    imwrite("output1.pgm", gImg2);

    cout << "Showing image in window... Press a key to finish." << endl;
    cv::imshow("Window: Img2", gImg2);
    cv::waitKey(0); // cvWaitKey(0) or cv::waitKey(0)

    return 0;
}

/*

# In Linux:
g++ -o example_opencv_1 example_opencv_1.cpp $(pkg-config --cflags --libs opencv4)

# To launch: example:
./example_opencv_1 cam_74.pgm

*/


/*
# In Linux, to install the libraries (Ubuntu):
sudo apt install libopencv-dev
*/

