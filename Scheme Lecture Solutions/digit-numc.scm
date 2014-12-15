;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname digit-numc) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
(define (digit-numc n)
  (cond [(<= n 9) 1]
  [(<= n 99) 2]
  [(<= n 999) 3]
  [(<= n 9999) 4]
  [else "a lot"]
  )
)