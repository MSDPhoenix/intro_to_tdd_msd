import unittest

def reverseList(a): # "a" represents a list
    x = len(a)
    for i in range(x//2):
        a[i],a[x-i-1] = a[x-i-1],a[i]
    return a

class reverseListTests(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(reverseList([1,3,5]),[5,3,1])
    def testCase2(self):
        self.assertEqual(reverseList([2,4,6,8]),[8,6,4,2])
    def testCase3(self):
        self.assertEqual(reverseList([3,6,9,12,15]),[15,12,9,6,3])
    def testCase4(self):
        self.assertEqual(reverseList([4,8,12,16,20,24,28]),[28,24,20,16,12,8,4])
    def testCase5(self):
        self.assertEqual(reverseList([1,2,3,4,5,6,7,8,9]),[9,8,7,6,5,4,3,2,1])
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown")

if __name__ == '__main__' :
    unittest.main()

#################

import unittest

def isPalindrome(a):   # "a" represents a string
    x = len(a)
    b = ""
    for i in range(x):
        b = b + a[x-1-i]
    if a == b:
        return True
    else:
        return False

class isPalindromeTests(unittest.TestCase):
    def testCase1(self): 
        self.assertTrue(isPalindrome("racecar"))
    def testCase2(self):
        self.assertFalse(isPalindrome("rabcr"))
    def testCasde3(self):
        self.assertTrue(isPalindrome("wassamassaw"))
    def testCase4(self):
        self.assertFalse(isPalindrome("wut?"))
    def testCase5(self):
        self.assertTrue(isPalindrome("able was I ere I saw elba"))
    def testCase6(self):
        self.assertFalse(isPalindrome("factorial"))
    def testCase7(self):
        self.assertTrue(isPalindrome("saippuakivikauppias"))
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown")

if __name__ == "__main__":
    unittest.main()

###################################################

import unittest

def coins(x):   # "x" represents the amount of change to give back
    q = x//25
    x = x - 25*q
    d = x//10
    x = x - 10*d
    n = x//5
    x = x - n*5
    ans = str(q) + " quarter(s), "+ str(d) + " dime(s), " + str(n) + " nickel(s), and " + str(x) + " penny/pennies."
    return ans

class coinsTests(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(coins(87),"3 quarter(s), 1 dime(s), 0 nickel(s), and 2 penny/pennies.")
    def testCase2(self):
        self.assertEqual(coins(30),"1 quarter(s), 0 dime(s), 1 nickel(s), and 0 penny/pennies.")
    def testCase3(self):
        self.assertEqual(coins(13),"0 quarter(s), 1 dime(s), 0 nickel(s), and 3 penny/pennies.")
    def testCase4(self):
        self.assertEqual(coins(17),"0 quarter(s), 1 dime(s), 1 nickel(s), and 2 penny/pennies.")
    def testCase5(self):
        self.assertEqual(coins(51),"2 quarter(s), 0 dime(s), 0 nickel(s), and 1 penny/pennies.")
    def testCase6(self):
        self.assertEqual(coins(44),"1 quarter(s), 1 dime(s), 1 nickel(s), and 4 penny/pennies.")
    def testCase7(self):
        self.assertEqual(coins(92),"3 quarter(s), 1 dime(s), 1 nickel(s), and 2 penny/pennies.")
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown")

if __name__ == "__main__":
    unittest.main()

#####################################

import unittest

def recursive_factorial(n):
    if n < 0:
        return None
    elif n ==0:
        return 1
    else:
        return n * recursive_factorial(n-1)

class factorialTests(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(recursive_factorial(2),2)
    def testCase2(self):
        self.assertEqual(recursive_factorial(3),6)
    def testCase3(self):
        self.assertEqual(recursive_factorial(4),24)
    def testCase4(self):
        self.assertEqual(recursive_factorial(5),120)
    def testCase5(self):
        self.assertEqual(recursive_factorial(6),720)
    def testCase6(self):
        self.assertEqual(recursive_factorial(-2),None)
    def testCase7(self):
        self.assertEqual(recursive_factorial(0),1)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown")

if __name__ == "__main__":
    unittest.main()

#############################

import unittest

def recursive_fibonnacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursive_fibonnacci(n-1) + recursive_fibonnacci(n-2)

class recursive_fibonnacci_tests(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(recursive_fibonnacci(1),0)
    def testCase2(self):
        self.assertEqual(recursive_fibonnacci(2),1)
    def testCase3(self):
        self.assertEqual(recursive_fibonnacci(3),1)
    def testCase4(self):
        self.assertEqual(recursive_fibonnacci(4),2)
    def testCase5(self):
        self.assertEqual(recursive_fibonnacci(5),3)
    def testCase6(self):
        self.assertEqual(recursive_fibonnacci(6),5)
    def testCase7(self):
        self.assertEqual(recursive_fibonnacci(7),8)
    def testCase8(self):
        self.assertEqual(recursive_fibonnacci(8),13)
    def testCase9(self):
        self.assertEqual(recursive_fibonnacci(9),21)
    def testCase10(self):
        self.assertEqual(recursive_fibonnacci(10),34)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown")

if __name__ == "__main__":
    unittest.main()