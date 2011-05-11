(ns e55
  (:require [clojure.contrib.math :as math
             clojure.contrib.string :as string
             ]))

(defn next-fib [[pos last value]]
  [(inc pos) value (+ last value)])

(def fibs (iterate next-fib [2 1 1]))

(defn pandigital?
  [numstring]
  (and (= 9 (count numstring))
       (= 9 (count (distinct (remove #(= \0 %) numstring))))))

(defn first-nine [somenum]
  (take 9 (str somenum)))

(defn last-nine [somenum]
  (take 9 (reverse (str somenum))))

(defn test-last [[pos last value]]
  (pandigital? (last-nine value)))

(defn test-first [[pos last value]]
  (pandigital? (first-nine value)))

(time (println (take 1 (filter (fn [[pos last value]]
                                 (pandigital? (last-nine value))) fibs))))