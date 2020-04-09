"""

    Logs

    bases are 2 or 10 genrally
    In Computer Science -> Binary -> We always prefer base 2
    log(8)

    log2(8) => 2 pow 3 = 8

    8 is being divided by 2 again and again :)
    8 4 2 1

                       *                    LEVEL 0

               *              *             LEVEL 1

           *       *      *        *        LEVEL 2

       *      *                             LEVEL 3

                                            4 LEVELS IN TOTAL

                                            1 + floor(log(9))
                                            1 + floor (3.17)
                                            1 + 3
                                            4

      Nodes = 9

                n = 8
                log(8) = 3
                8 4 2 1

                [1, 3, 11, 8, 5, 7, 9, 2]

            [1, 3, 11, 8]       [5, 7, 9, 2]

        [1, 3]  [11, 8]       [5, 7]    [9, 2]

       [1] [3]  [11] [8]     [5] [7]    [9]  [2]


                        8               -> 1 Node 2 pow 0

                   4        4            -> 2 pow 1

                2    2    2    2        -> 2 pow 2

              1  1  1  1 1  1 1  1       -> 2 pow 3


    We are trying to represent this is the worst case for our algo
    O(log n)


"""

# Solve and Compute Time Complexity Analysis for Prims Algorithm :)