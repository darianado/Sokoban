(define (domain sokoban)
  (:requirements :strips :typing)
  (:types location)
  (:predicates
    (agent-at ?loc - location)
    (box-at ?loc - location)
    (adj-n ?loc1 ?loc2 - location)
    (adj-s ?loc1 ?loc2 - location)
    (adj-e ?loc1 ?loc2 - location)
    (adj-v ?loc1 ?loc2 - location)
    (wall-at ?loc - location)
  )

  ;; Move agent
  (:action move-agent-n
    :parameters (?from ?to - location)
    :precondition (and (agent-at ?from) (adj-n ?from ?to) (not (wall-at ?to)) (not (box-at ?to)) )
    :effect (and
              (not (agent-at ?from))
              (agent-at ?to)
            )
  )

  (:action move-agent-s
    :parameters (?from ?to - location)
    :precondition (and (agent-at ?from) (adj-s ?from ?to) (not (wall-at ?to)) (not (box-at ?to)) )
    :effect (and
              (not (agent-at ?from))
              (agent-at ?to)
            )
  )

  (:action move-agent-e
    :parameters (?from ?to - location)
    :precondition (and (agent-at ?from) (adj-e ?from ?to) (not (wall-at ?to)) (not (box-at ?to)) )
    :effect (and
              (not (agent-at ?from))
              (agent-at ?to)
            )
  )

  (:action move-agent-v
    :parameters (?from ?to - location)
    :precondition (and (agent-at ?from) (adj-v ?from ?to) (not (wall-at ?to)) (not (box-at ?to)) )
    :effect (and
              (not (agent-at ?from))
              (agent-at ?to)
            )
  )

  ;; Push box
  (:action push-box-n
    :parameters (?boxloc ?agentloc ?newboxloc - location)
    :precondition (and (agent-at ?agentloc) (box-at ?boxloc) 
                       (adj-n ?agentloc ?boxloc) (adj-n ?boxloc ?newboxloc)
                        (not (wall-at ?newboxloc)) (not (box-at ?newboxloc)))
    :effect (and
              (not (box-at ?boxloc))
              (box-at ?newboxloc)
              (agent-at ?boxloc)
              (not (agent-at ?agentloc))
            )
  )


  (:action push-box-s
    :parameters (?boxloc ?agentloc ?newboxloc - location)
    :precondition (and (agent-at ?agentloc) (box-at ?boxloc) 
                       (adj-s ?agentloc ?boxloc) (adj-s ?boxloc ?newboxloc)
                        (not (wall-at ?newboxloc)) (not (box-at ?newboxloc)))
    :effect (and
              (not (box-at ?boxloc))
              (box-at ?newboxloc)
              (agent-at ?boxloc)
              (not (agent-at ?agentloc))
            )
  )

  (:action push-box-e
    :parameters (?boxloc ?agentloc ?newboxloc - location)
    :precondition (and (agent-at ?agentloc) (box-at ?boxloc) 
                       (adj-e ?agentloc ?boxloc) (adj-e ?boxloc ?newboxloc)
                        (not (wall-at ?newboxloc)) (not (box-at ?newboxloc)))
    :effect (and
              (not (box-at ?boxloc))
              (box-at ?newboxloc)
              (agent-at ?boxloc)
              (not (agent-at ?agentloc))
            )
  )

  (:action push-box-v
    :parameters (?boxloc ?agentloc ?newboxloc - location)
    :precondition (and (agent-at ?agentloc) (box-at ?boxloc) 
                       (adj-v ?agentloc ?boxloc) (adj-v ?boxloc ?newboxloc)
                        (not (wall-at ?newboxloc)) (not (box-at ?newboxloc)))
    :effect (and
              (not (box-at ?boxloc))
              (box-at ?newboxloc)
              (agent-at ?boxloc)
              (not (agent-at ?agentloc))
            )
  )

    

)
