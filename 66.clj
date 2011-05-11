(ns e66
  (:use clojure.contrib.math))

(defn y [x D]
  (sqrt (/ (- (* x x)
                   1)
           D)))

(defn find-minx [D]
  (do ;(println D)
      (first (filter #(do (println %)
                          (integer? (y % D))) (iterate inc 2)))))

;(println (map find-minx [2 3 5 6 7]))

(time (println (apply max (map find-minx (remove #(integer? (sqrt %)) (range 2 8))))))
(time (println (apply max (map find-minx (remove #(integer? (sqrt %)) (range 2 10001))))))