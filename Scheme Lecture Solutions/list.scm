;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname list) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ())))
(define (sumAll list)
  (cond [(null? list) 0]
        [else (+ (car list) (sumAll (cdr list)))]
  )
 )

(define (makeList n value)
  (cond [(= n 0) '()]
        [else (cons value (makeList (- n 1) value))]
   )
 )

(define (isMember item list)
  (cond [(null? list) #f]
        [(equal? (car list) item) #t]
        [else (isMember item (cdr list))]
   )
 )

(define (removeDuplicates list)
  (cond [(null? list) '()]
        [(isMember (car list) (cdr list)) (removeDuplicates (cdr list))]
        [else (cons (car list) (removeDuplicates (cdr list)))]
   )
 )