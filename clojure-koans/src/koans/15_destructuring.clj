(ns koans.15-destructuring
  (:require [koan-engine.core :refer :all]))

(def test-address
  {:street-address "123 Test Lane"
   :city "Testerville"
   :state "TX"})

(meditations
  "Destructuring is an arbiter: it breaks up arguments"
  (= ":bar:foo" ((fn [[a b]] (str b a))
         [:foo :bar]))

  "Whether in function definitions"
  (= (str "An Oxford comma list of apples, "
          "oranges, "
          "and pears.")
     ((fn [[a b c]] (format "An Oxford comma list of %s, %s, and %s."a b c))
      ["apples" "oranges" "pears"]))

  "Or in let expressions"
  (= "Rich Hickey aka The Clojurer aka Go Time aka Lambda Guru"
     (let [[first-name last-name & aliases]
           (list "Rich" "Hickey" "The Clojurer" "Go Time" "Lambda Guru")]
       (format "%s %s aka %s" first-name last-name (clojure.string/join " aka " aliases))))

  "You can regain the full argument if you like arguing"
  (= {:original-parts ["Stephen" "Hawking"] :named-parts {:first "Stephen" :last "Hawking"}}
     (let [[first-name last-name :as full-name] ["Stephen" "Hawking"]]
       {:original-parts full-name :named-parts {:first first-name :last last-name}}))

  "Break up maps by key"
  (= "123 Test Lane, Testerville, TX"
     (let [{street-address :street-address, city :city, state :state} test-address]
       (clojure.string/join ", " [street-address city state])))

  "Or more succinctly"
  (= "123 Test Lane, Testerville, TX"
     (let [{:keys [street-address city state]} test-address]
       (clojure.string/join ", " [street-address city state])))

  "All together now!"
  (= "Test Testerson, 123 Test Lane, Testerville, TX"
     ((fn [[a b] {c :street-address d :city e :state}]
        (format "%s %s, %s, %s, %s" a b c d e)) ["Test" "Testerson"] test-address)))
