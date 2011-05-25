(ns e32
  (:require [clojure.contrib.math :as math]
            [clojure.contrib.string :as string])
  (:use clojure.contrib.combinatorics))

(defn pandigital?
  [numstring]
  (and (= 9 (count numstring))
       (= 9 (count (distinct (remove #(= \0 %) numstring))))))

(defn string-permutations
  [somestring]
  (map (partial string/join "") (permutations somestring)))