(ns e102
  (:require [clojure.contrib.math :as math]
            [clojure.contrib.string :as string]
            [clojure.contrib.generic.math-functions :as gmath]))

(def input (slurp "triangles.txt"))

(def sq #(* % %))

(def O [0,0])

(defn sq-dist-between [[ax,ay],[bx,by]]
  (+ (sq (- ax bx))
     (sq (- ay by))))

(defn dist-between [B,C]
  (math/sqrt (sq-dist-between B C)))

(defn to-deg [rad]
  (* (/ rad
        (* 2 (Math/PI)))
     360))

(defn angle-with-origin [B C]
  (let [a_sq (sq-dist-between B C)
        b_sq (sq-dist-between C O)
        c_sq (sq-dist-between B O)
        b (dist-between C O)
        c (dist-between B O)]
    (to-deg (gmath/acos (/ (- (+ b_sq c_sq)
                              a_sq)
                           (* 2 b c))))))

(def sum (partial reduce +))

(defn close-enuf? [A B]
     (< (math/abs (- A B))
        0.00000001))

(defn contains-O? [A B C]
  (close-enuf? 360 (+ (angle-with-origin A B)
                      (angle-with-origin A C)
                      (angle-with-origin B C))))

(def t1 [[-340,495],[-153,-910],[835,-947]])
(def t2 [[-175,41],[-421,-714],[574,-645]])

(println "t1 is true? :- " (contains-O? [-340,495] [-153,-910] [835,-947]))

(println "t2 is false? :-" (contains-O? [-175,41] [-421,-714] [574,-645]))

(defn to-int [somestr]
  (Integer/parseInt somestr))

(defn make-triangle [line]
  (let [[ax ay bx by cx cy] (vec (map to-int (string/split #"," line)))]
    [[ax ay] [bx by] [cx cy]]))

(def triangles (map make-triangle (string/split-lines input)))

(time (println (count (filter (partial apply contains-O?) triangles))))