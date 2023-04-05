// Team GuacNoSauce :: Vansh Saboo, Samantha Hua
// SoftDev pd7
// K27 -- Basic functions in JavaScript
// 2023-04-03t


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

function Factorial(n) {
    if (n < 2) {
        return 1;
    }
    else {
        return n * Factorial( n - 1 );
    }
}

function Fibonacci(n) {
    if (n < 2) {
        return 1;
    }
    else {
        return n * Factorial( n - 1 );
    }
}