/*
 * Copyright (c). All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */



/**
 * Note: using and adapting some things from
 * http://boofcv.org/index.php?title=Tutorial_Images
 * boofcv.examples.segmentation.ExampleBinaryOps.java
 * boofcv.examples.segmentation.ExampleThresholding
 */


import boofcv.io.image.ConvertBufferedImage;
import boofcv.io.image.UtilImageIO;
import boofcv.struct.image.GrayU8;

import java.awt.image.BufferedImage;

import java.util.Arrays;


public class SimpleExample01 {

	public static void main( String args[] ) {

		// load and convert the image into a usable format
    String filein1 = "particles01__rows480__cols638.jpg";
    String fileout1 = "out1.png";
    String fileout2 = "out2.png";
    System.out.println("filein1: " + filein1);
		// BufferedImage image = UtilImageIO.loadImage("particles01__rows480__cols638.jpg");
		BufferedImage image = UtilImageIO.loadImage(filein1);


    // Converting from BufferedImage input image to BoofCV imgray8
    GrayU8 imgray8 = ConvertBufferedImage.convertFromSingle(image, null, GrayU8.class);
    System.out.println("imgray8.width: " + imgray8.width);
    System.out.println("imgray8.height: " + imgray8.height);

    // Copying the data array from imgray8 to a new im2gray8.
		GrayU8 im2gray8 = new GrayU8(imgray8.width, imgray8.height); // an image is created
    im2gray8.setData(Arrays.copyOf(imgray8.getData(), imgray8.width * imgray8.height));

    // The imgray8 is going to be modified: its 4 corner pixels will have
    // values 201, 202, 203, 204.
    //
    //
    // Using accessors (.set y .get)
    System.out.println("BEFORE CHANGES:");
    System.out.println("  imgray8.get(0,0): " + imgray8.get(0,0));
    System.out.println("  imgray8.get((imgray8.width - 1), 0): " + imgray8.get((imgray8.width - 1), 0));
    System.out.println("  imgray8.get(0, (imgray8.height - 1)): " + imgray8.get(0, (imgray8.height - 1)));
    System.out.println("  imgray8.get((imgray8.width - 1),(imgray8.height - 1)): " + imgray8.get((imgray8.width - 1),(imgray8.height - 1)));
    imgray8.set(0, 0, 201);                    // setting pixel at [col=0, row=0] to value 201
    imgray8.set((imgray8.width - 1), 0, 202);  // setting pixel at [col=(imgray8.width - 1), row=0] to value 202
    imgray8.set(0, (imgray8.height - 1), 203); // setting pixel at [col=0, row=(imgray8.height - 1)] to value 203
    imgray8.set((imgray8.width - 1), (imgray8.height - 1), 204); // setting pixel at [col=(imgray8.width - 1), row=(imgray8.height - 1) to value 204
    System.out.println("AFTER CHANGES:");
    System.out.println("  imgray8.get(0,0): " + imgray8.get(0,0));
    System.out.println("  imgray8.get((imgray8.width - 1), 0): " + imgray8.get((imgray8.width - 1), 0));
    System.out.println("  imgray8.get(0, (imgray8.height - 1)): " + imgray8.get(0, (imgray8.height - 1)));
    System.out.println("  imgray8.get((imgray8.width - 1),(imgray8.height - 1)): " + imgray8.get((imgray8.width - 1),(imgray8.height - 1)));


    // UtilImageIO.saveImage(imgray8, "/tmp/out1.png");
    // UtilImageIO.saveImage(im2gray8, "/tmp/out2.png");
    UtilImageIO.saveImage(imgray8, fileout1);
    System.out.println("fileout1: " + fileout1);
    UtilImageIO.saveImage(im2gray8, fileout2);
    System.out.println("fileout2: " + fileout2);

	}

}
