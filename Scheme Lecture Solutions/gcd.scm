;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname gcd) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ())))
(define GCD 
  (lambda (a b) 
    (cond [(= a b) a]
          [(> a b) (GCD (- a b) b)]
          [else (GCD a (- b a))]
      )
    )
  )