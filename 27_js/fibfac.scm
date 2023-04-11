; Team GuacNoSauce :: Vansh Saboo, Samantha Hua
;SoftDev pd7
;K27 -- Basic functions in JavaScript
;2023-04-03t

;Scheme Antecedents for JS work

;factorial:
;<your team's fact(n) implementation>

;(fact 1) ;"...should be  1"
;(fact 2) ;"...should be  2"
;(fact 3) ;"...should be  6"
;(fact 4) ;"...should be  24"
;(fact 5) ;"...should be  120"


;fib:
;<your team's fib(n) implementation>

;(fib 0) ;"...should be  0"
;(fib 1) ;"...should be  1"
;(fib 2) ;"...should be  1"
;(fib 3) ;"...should be  2"
;(fib 4) ;"...should be  3"
;=================================================================

(define fact (lambda (n)
    (if (< n 2)
        1
        (* n (fact (- n 1)))
)))
             
(define fib (lambda (n)
    (if (< n 2)
        n
        (+ (fib (- n 1)) (fib (- n 2)))
)))


(display (fact 10))
(newline)
(display (fact 4))
(newline)
(display (fib 10))
