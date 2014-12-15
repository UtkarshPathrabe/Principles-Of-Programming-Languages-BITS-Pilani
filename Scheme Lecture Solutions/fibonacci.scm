;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname fibonacci) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
(define fibonacci (lambda (n) (if (= n 0) 0 (if (= n 1) 1 (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))))