(ns e32
  (:require [clojure.contrib.math :as math]
            [clojure.contrib.string :as string]
            [clojure.contrib.str-utils2 :as util])
  (:use clojure.contrib.combinatorics))

(defn string-permutations
  [somestring]
  (map (partial string/join "") (permutations somestring)))

(def pandigitals (string-permutations "123456789"))

(def split-pandigitals (for [panstring pandigitals
                             mul-pos (range 1 7)
                             eq-pos (range (+ 2 mul-pos) 7)]
                         (map read-string [(util/take panstring mul-pos)
                                           (util/take (util/drop panstring mul-pos) (- eq-pos mul-pos))
                                           (util/drop panstring eq-pos)])))

(def answers (for [[a b c] split-pandigitals
                   :when (= c
                            (* a b))]
               
               c))


