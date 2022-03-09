## Exercise 02d 

In this exercise we are going to compare the number of operations in two alternatives for computing a morphological dilation with structuring element.

### Considerations 

We are going to compute the number of elementary $max$ operations that we have to do in order to compute the max of a list of elements. \

* Considering only two elements:
    * $max(x_1, x_2)$ -> operation

* Considering three elements:
    * $max(x1,x2,x3) = max(x1,max(x2,x3))$ -> 2 operations

* Considering four elements:
    * $max(x_1, x_2, x_3) = max(x_1, max(x_2, x_3)) $-> 3operations

* Finally if we consider $n$ elements:
    * $max(x_1, x_2, ..., x_n) = max(x_1, max(x_2, ... ,max(x_{n-1}, x_n)))$ -> n-1 operations

## dilate_B (I))
For computing the operations of the structuring element, whose size is $MxM$, we have $M^2$ elements \

$MxM→M^2 −1 (operations)$ \
 As the image have $NxN$ elements, or $N^2$, we can compute the total number of operations: \

$NumOp_1 = N^2(M^2 −1)$

## dilate_C(dilate_D (I)))
For each structuring element as their size is $M$, we can say that the number of elementary operations is $M-1$, following the preovious reasoning

As the image have $NxN$ elements, or $N^2$, we can compute the total number of operations, with only one structuring element:

$N^2(M−1)$

But, we have two elements, so we have to multiply the number of operations
by two

$NumOp_2 = 2N^2(M−1) $

### Conclusion 
We can confirm that the number of operations in the second alternative is lower than the first one.
