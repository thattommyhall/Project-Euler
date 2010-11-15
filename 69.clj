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

(println (apply max-key (into [#(/ % (totient %))] (range 2 11))))

(println (apply max-key (into [#(/ % (totient %))] (range 2 1000001))))


  

	       
	


     







