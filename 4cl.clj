(defn my-count
  ([someseq] (my-count someseq 0))
  ([someseq tot]
     (if (not (seq someseq))
       tot
       (my-count (rest someseq) (inc tot)))))
  