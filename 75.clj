(ns e75
 (:use clojure.contrib.math))

(defn coprime? [a b]
  (= (gcd a b)
     1))

(defn square [a]
  (* a a))

(defn pqs [max-perimeter]
  (let [upto (sqrt max-perimeter)]
    (for [p (range (inc upto))
	  q (range 1 p)
	  :when (and (or (even? p) (even? q))
		     (coprime? p q))]
      [p q])))

(defn primative [max-perimeter]
  (for  [[p q] (pqs max-perimeter)
	 :let [sqp (square p)
	       sqq (square q)
	       a (* 2 p q)
	       b (- sqp sqq)
	       c (+ sqp sqq)
	       per (+ (* 2 p q)
		      (* 2 sqp))]
	 ]
    [a b c per]))

(defn triples [max-perimeter]
  (for [t (primative max-perimeter)
	mult (iterate inc 1)
	:while (< (* (nth t 3) mult)
		  max-perimeter)]
    (vec (map #(* mult %) t))))


(time (println
       (count
	(filter #(= (val %)
		    1)
		(frequencies
		 (map #(nth % 3)
		      (triples 1500000)))))))
