(defn days []
	(cycle [:mon :tues :weds :thurs :fri :sat :sun]))

(defn leap-year? [year]
		 (cond (= (rem year 400)
				0)
		 true
		 ;
		 (= (rem year 100)
				0)
		 false
		 ;
		 (= (rem year 4)
				0)
		 true
		 ;
		 :else
		 false))


(defn days-in-month [month year] 
	(cond (= month :sept) 30
	      (= month :april) 30
        (= month :june) 30
        (= month :nov) 30
        (= month :feb) (if (leap-year? year)
                         29
                         28)
                         ;
        :else 31))


(def months [:jan :feb :march :april :may :june :july :aug :sept :oct :nov :dec] )


(defn dates []
  (for [year (range 1900 2001)
        month months
        date (range 1 (inc (days-in-month month year)))]
    [date month year]))

(def daydates (map cons (days) (dates)))

;(println (take 365 daydates))

(time
 (println
  (count 
   (for [[day date month year] daydates
         :when (> year 1900)
         :when (and (= day :sun)
                    (= date 1))]
     [day date month year]))))


 


  
    
      



