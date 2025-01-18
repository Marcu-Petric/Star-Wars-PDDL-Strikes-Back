(define (problem starwars-delivery)
   (:domain starwars-transport)
   (:objects
      tatooine hoth dagobah r2d2 c3po )
   (:init
      (planet tatooine)
      (planet hoth)
      (planet dagobah)
      (droid r2d2)
      (droid c3po)
      (ship-at tatooine)
      (droid-at r2d2 tatooine)
      (droid-at c3po hoth)
      (ship-free))
   (:goal
      (and (droid-at r2d2 dagobah)
           (droid-at c3po dagobah))))
