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

(defn distinct-primefactors [n]
  (count (distinct (primefactors n))))

(def consec
     (iterate #(map inc %)
	      [2 3 4 5]))


(println
 (let [target [4 4 4 4]]
	 (first
		(first
		 (filter #(= target 
								 (map distinct-primefactors %))
						 consec)))))

