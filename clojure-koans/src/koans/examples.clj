;; odd elements
((fn [lst]
   (loop [l lst
          n 0
          acc []]
     (if (empty? l)
       acc
       (recur (rest l)
              (inc n)
              (if (odd? n)
                (conj acc (first l) acc)
                acc))))) [1 2 3])

;; sum of odd elements
((fn [lst]
   (loop [l lst
          acc 0]
     (if (empty? l)
       acc
       (recur (rest l)
              (if (odd? (first l))
                (+ acc (first l))
                acc))))) [1 2 3])

;; length
((fn [lst]
   (loop [l lst
          acc 0]
     (if (empty? l)
       acc
       (recur (rest l)
              (+ 1 acc))))) [1 2 3])

;; abs
((fn [lst] (map (fn [x] (max x (- x))) lst))[1 -2 (- 3)])

;; e^x
(with-in-str "2
1
2
"
 (let [n_t (read-line)
       n (Integer/parseInt n_t)]

   (loop [a0 n]
     (when (> a0 0)

       (let [x_t (read-line)
             x (Float/parseFloat x_t)]
         (loop [n 1
                acc 1]
           (if (= n 11)
             (println (float acc))
             (recur (inc n) (+ acc (/ (reduce * (repeat n x)) (reduce * (range 1 (+ 1 n))))))))
         )
       (recur (- a0 1) )))))

;; calc for i = 1 .. 11 do x^i/i! + ...
((fn [x]
   (loop [n 1
          acc 1]
     (if (= n 11)
       (float acc)
       (recur (inc n) (+ acc (/ (reduce * (repeat n x)) (reduce * (range 1 (+ 1 n))))))))) 1)


;; area under curve
(defn calc-f [x coefs powers]
  (loop [c coefs
         p powers
         acc 0]
    (if (empty? c)
      acc
      (recur (rest c)
             (rest p)
             (+ acc
                (* (first c)
                   (Math/pow x (first p))))))))

(= (calc-f 5 [4 4] [2 2]) 200.0)

(defn read-numbers []
  (map read-string (clojure.string/split (read-line) #"\s+")))


(with-in-str "1 2 3 4 5 6 7 8
-1 -2 -3 -4 1 2 3 4
1 2"
  (let [c (read-numbers)
        p (read-numbers)
        [s e] (read-numbers)
        d 0.001]
    (loop [v s
           acc 0
           acc2 0]
      (if (> v e)
        (do
          (println (* d acc))
          (println (* d acc2)))
        (let [r (calc-f v c p)]
          (recur (+ v d) (+ acc r) (+ acc2 (* (. Math PI) r r))))))))

;; macroexpanc C-c C-m
(->> [1 2 [3 4] 5]
     flatten  ; no parenthesis
     (map inc))

;; ((λx.(x y))(λz.z))
;; z

;; 1. ((λx.((λy.(x y))x))(λz.w))
;; 2
(def w 10)
((fn [x] ((fn [y] (x y)) x)) (fn [z] w))


;; ((λx.(x x))(λx.(x x))

(def x 11)
;; ((fn [x] (x x)) (fn [x] (x x))) ;; can't parse


;; (λg.((λf.((λx.(f (x x)))(λx.(f (x x))))) g))
;; (λg.((λf.((λx.(f (x x)))(λx.(f (x x))))) g))


;; λx.λy.x(xy)

;; CGD
(with-in-str "10 5"
  (let [f (fn [a b] (if (= a b)
                      a
                      (recur (if (> a b) (- a b) (- b a))
                             (if (> a b) b a))))
       [m n] (map read-string (re-seq #"\d+" (read-line)))]
    (println (f m n))))

;; Fib
(defn fib-seq []
  ((fn rfib [a b]
       (cons a (lazy-seq (rfib b (+ a b)))))
   0 1))

(with-in-str "5"
 (let [n (read)]
   (println (nth (fib-seq) n))))

;; pascals-triangle
;; 1
;; 1 1
;; 1 2 1
;; 1 3 3 1
;; 1 4 6 4 1
;; n! / (r! * (n - r)! ), n - row, r - column

(defn fact [n]
  (loop [n n acc 1]
    (if (= n 0)
      acc
      (recur (dec n) (* acc n)))))

(= (fact 1) 1)
(= (fact 3) 6)

(defn calc-pt-num [n r]
  (/ (fact n) (* (fact r) (fact (- n r)))) )

(= (calc-pt-num 0 0) 1)
(= (calc-pt-num 1 0) 1)
(= (calc-pt-num 2 1) 2)

(let [k 4]
  (loop [i 0]
    (if (= i (- k 1))
      nil
      )
    ))
