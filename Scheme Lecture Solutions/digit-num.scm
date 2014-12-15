;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname digit-num) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
(define (digit-num n)
  (if (<= n 9) 1
      (if (<= n 99) 2
          (if (<= n 999) "less than"
              (if (<= n 9999) 4 
                  "a lot")
          )
      )
   )
 )