(ns e54
  (:require [clojure.contrib.math :as math]
            [clojure.contrib.string :as string]
            [clojure.contrib.combinatorics :as comb]
            [clojure.contrib.generic.math-functions :as gmath]))

(def hands (string/split-lines (slurp "poker.txt")))

(defn score [hand]
  (let [numbers (map first hand)
        suits (map second hand)]
    [numbers suits]))

(defn game-winner [somegame]
  (let [player1 (take 5 (string/split #"\s" somegame))
        player2 (drop 5 (string/split #"\s" somegame))]))

(def player1 (take 5 (string/split #"\s" (first hands))))

  
