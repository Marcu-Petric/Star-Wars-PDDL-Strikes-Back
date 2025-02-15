(define (domain starwars-transport)
   (:predicates
      (planet ?p)              ; Represents a planet
      (droid ?d)               ; Represents a droid
      (ship-at ?p)             ; Current location of the spaceship
      (droid-at ?d ?p)         ; Location of a droid
      (ship-free)              ; Indicates if the spaceship is free to carry a droid
      (carrying ?d))           ; Indicates if the spaceship is carrying a specific droid

   ; Fly action: The spaceship moves from one planet to another
   (:action fly
       :parameters (?from ?to)
       :precondition (and (planet ?from) (planet ?to) (ship-at ?from))
       :effect (and (ship-at ?to)
                    (not (ship-at ?from))))

   ; Board action: Load a droid onto the spaceship
   (:action board
       :parameters (?d ?p)
       :precondition (and (droid ?d) (planet ?p) (droid-at ?d ?p)
                          (ship-at ?p) (ship-free))
       :effect (and (carrying ?d)
                    (not (droid-at ?d ?p))
                    (not (ship-free))))

   ; Disembark action: Unload a droid from the spaceship at the current planet
   (:action disembark
       :parameters (?d ?p)
       :precondition (and (droid ?d) (planet ?p) (carrying ?d) (ship-at ?p))
       :effect (and (droid-at ?d ?p)
                    (ship-free)
                    (not (carrying ?d)))))
