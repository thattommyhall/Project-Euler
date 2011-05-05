(def primes-simple
     (concat
      [2 3 5 7]
      (lazy-seq
       (let [primes-from
             (fn primes-from [n]
               (if (some #(zero? (rem n %))
                         (take-while #(<= (* % %) n) primes-simple))
                 (recur (+ n 1))
                 (lazy-seq (cons n (primes-from (+ n 1))))))]
         (primes-from 11)))))

(def primes-to-987654321
     (set (take-while #(<= % 987654321) primes-simple)))



