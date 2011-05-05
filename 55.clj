(ns e55
  (:use clojure.string :only [reverse] :rename {revers reverse-string} ))

;(defn reverse-string [somestring]
;  (clojure.string/reverse somestring))

(defn palendrome? [somestring]
  (= somestring
     (reverse-string somestring)))
  
(defn is-lychrel?
  ([n] (is-lychrel? n 0))
  ([n depth]
     (let [numstring (str n)]
       (cond (and (> depth 0)
									(palendrome? numstring))
						 false
						 ;
						 (> depth 50)
						 true 
	           ;
						 :else
						 (recur (+ n
											 (bigint (reverse-string numstring)))
										(inc depth))))))

(println (count (filter #(is-lychrel? %) (range 10001))))
