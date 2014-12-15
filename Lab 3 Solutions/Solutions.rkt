;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname Solutions) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ())))
/* Binary search function */
(define binary-search
  (lambda (ls value low high)
    (let ((mid (floor (/ (+ low high) 2))))
      (cond
        ((> low high) -1)
        ((= (list-ref ls mid) value) mid)
        ((> (list-ref ls mid) value) (binary-search ls value low (- mid 1)))
        ((< (list-ref ls mid) value) (binary-search ls value (+ mid 1) high))
        )
      )
    )
  )

/* Reversing the contents of list */
(((lambda (fun) 
    ((lambda (F) (F F)) 
     (lambda (F) (fun (lambda (x) ((F F) x)))
       )
     )
    )
  (lambda (rev) (lambda (lst)
                  (cond ((null? lst) '())
                        (else (append (rev (cdr lst)) (cons (car lst) '())))
                        )
                  )
    )
  ) '(1 2 3))

/* Tail recursive version of Length of List */
(define (TRlength lst)
  (cond ((null? lst) 0) (#T (+ 1 (TRlength (cdr lst)))))
  )

/* Non-Tail recursive version of Length of List */
(define (NTRlength lst)
  (NTRlength.1 lst 0)
  )
(define (NTRlength.1 lst result)
  (cond ((null? lst) result) (#T (NTRlength.1 (cdr lst) (+ 1 result))))
  )

/* Nameless length function */
(((lambda (fun) ((lambda (F) (F F)) (lambda (F) (fun (lambda (x) ((F F) x))))))
(lambda (len) (lambda (lst) (cond ((null? lst) 0) (#T (+ 1 (len (cdr lst))))))))
 '(1 2 3))