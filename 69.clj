(defn sqrt [somenumber]
  (Math/sqrt somenumber))

(defn primefactors
  ([n] (primefactors n 2 []))
  ([n trying sofar]
     (cond (= trying
	      n)
	   (conj sofar n)
	   (= (rem n trying)
	      0)
	   (recur (/ n trying) trying (conj sofar trying))
	   :else (recur n (inc trying) sofar))))

(defn totient [n]
  (* n
     (reduce * (map #(- 1
			(/ 1 %))
		    (distinct (primefactors n))))))

(time (println (apply max-key #(/ % (totient %)) (range 2 10001))))

(time (println (apply max-key #(/ % (totient %)) (range 2 10001))))


	


     







