(def triangles
  (map #(/ (* %
	      (inc %))
	   2)
       (iterate inc 1)))

(def pentagonals 
  (map #(/ (* %
	      (- (* 3 %) 1))
	   2)
       (iterate inc 1)))

(def hexagonals
     (map #(* %
	      (- (* 2 %) 1))
	  (iterate inc 1)))

(defn incsmallest [somevec]
     (def smallest (apply min (map first somevec)))
     (map #(if (= (first %)
		  smallest)
	     (next %)
	     (identity %))
	  somevec))

(def results
     (map ffirst
	  (filter #(= (first (nth % 0))
		      (first (nth % 1))
		      (first (nth % 2)))
		  (iterate incsmallest
			   [triangles pentagonals hexagonals]))))
     
(time (println (take 1 (drop-while #(< % 40756) results))))