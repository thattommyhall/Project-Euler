(defn square [x] (* x x))

(defn divides? [a b]
  (= (remainder b a) 0))

(defn smallest-divisor
  ([n] smallest-divisor [n 2])
  ([n test-divisor]
     (cond (> (square test-divisor) n) n
	   (divides? test-divisor) test-divisor
	   :else (smallest-divisor n (+ test-divisor 1)))))0
     
     