action = input("While digging underground, you stumble across a tunnel, deep underground and unknown to mankind. What will you do? [explore/look/avoid]
if action == "explore":
  print("As you venture deeper into the tunnel, a creature springs out of the darkness, and slices you to bits with a knife. Game over.")
elif action == "look":
  action2 = input("Looking around, you pick up a rusty sword strewn on the ground. What will you do next? [explore/look/avoid]
  if action2 == "explore":
    print("You meet a hideous creature in the tunnel, and the two of you engage in a swordfight. Before long, the creature is dead, and you step over its body to find priceless treasure. You win!")
  elif action2 == "look":
    print("As you continue your search, you are oblivious to a dark shadow looming over you, and you are unfortunately sliced to bits by a cave creature. Game over.")
  elif action2 == "avoid":
    print("Hearing some strange noises from the tunnel, you hurriedly go back into the warm embrace of daylight. The only thing that you found is a sword, and you can't help but wonder if you missed anything from the tunnel. Game over.")
  else:
    print("The system has malfunctioned, and the game ends immediately due to an invalid response.")
elif action == "avoid":
  print("The darkness is terrifying, and you climb out into daylight. You have gotten absolutely nothing from your expedition, and you can't help but imagine what lay in the tunnel. Game over.")
else:
  print("Unable to process information. Game over.")
