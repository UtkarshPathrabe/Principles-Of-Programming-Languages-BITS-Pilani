;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname SchemeLecFull) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ())))
(define square1 (λ(x)(* x x)))
(define (square2 x) (* x x))

(define (curried-add x) (λ(y) (+ x y)))
(define add3 (curried-add 3))

(define (digit-numIf n) (if (<= n 9) 1 (if (<= n 99) 2 (if (<= n 999) "less than" (if (<= n 9999) 4 "a lot")))))
(define (digit-numC n) (cond [(<= n 9) 1] [(<= n 99) 2] [(<= n 999) 3] [(<= n 9999) 4] [else "a lot"]))

(define fac (λ(n) (if (= n 0) 1 (* n (fac(- n 1))))))
(define fib (λ(n) (if (= n 0) 0 (if (= n 1) 1 (+ (fib (- n 1)) (fib (- n 2)))))))

(define mygcd (λ(a b) (cond [(= a b) a] [(> a b) (mygcd (- a b) b)] [else (mygcd a (- b a))])))

(< -1 0)
(> -1 0)
(not #t)
(or #f #t)
(equal? 1 2)
(null? '())
(list? '(abc))
(number? 2)
(member? 2 (list 1 2 3 4))
(memv 2 '(1 2 3 4))
(* 1 2 1 1 1 3)
'(* 1 2 1 1 1 3)
(quote (* 1 2 1 1 1 3))
'("hi" "bits" "cs")
'()
(cons '(abcd) '(1 2 3 4))
(cons '(a b c d) '(1 2 3 4))
(car '(a b c))
(cdr '(a b c))
(cdr '(a))
(car (cdr '(a b c)))
(cdr (cdr '(a b c)))
(car '((a b) (c d)))
(cdr '((a b) (c d)))
(car '('() '(1 2 3 4 5)))
(cdar '('() '(1 2 3 4 5)))
(car (cons 'a '(b c)))
(cdr (cons 'a '(b c)))
(cons (car '(a b c)) (cdr '(d e f)))
(cons (car '(a b c)) (cdr '(a b c)))

(define (sumall list) (cond [(null? list) 0] [else (+ (car list) (sumall (cdr list)))]))

(define (makelist n value) (cond [(= n 0) '()] [else (cons value (makelist (- n 1) value))]))

(define (ismember item list) (cond [(null? list) #f] [(equal? (car list) item) #t] [else (ismember item (cdr list))]))

(define (remove-duplicates list) (cond [(null? list) '()] [(ismember (car list) (cdr list)) (remove-duplicates (cdr list))] [else (cons (car list) (remove-duplicates (cdr list)))]))

(let ((x 5))
(let ((x 6) (f (lambda (y z) (* y (- z x)))))
(f x 8)))

(let ((x 5))
(let* ((x 6) (f (lambda (y z) (* y (- z x)))))
(f x 8)))

(define f
(lambda (a b)
(let ((a b) (b a)) (list a b))
))

(define f1
(lambda (a b)
(let* ((a b) (b a)) (list a b))
))

(define infix
  (lambda (expr)
    (if (list? expr)
        (cond
          ((= 2 (length expr)) (list (car expr) (infix (cdr expr))))
          ((= 3 (length expr)) (list (infix (cadr expr)) (car expr) (infix (caddr expr)))) 
          (else expr)
        )
        expr
    )
  )
) 

(define (pairwise f)
    (λ(mylist)
           (letrec ((func (lambda(list)
                         (cond
                               ((null? list) '())
                               ((= 1 (modulo (length list) 2)) '())
                               (else (cons (f (car list) (cadr list)) (func (cddr list))))
                              )
                         )
                   ))
             (func mylist)
             )
    )
  )