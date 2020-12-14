import random

def chaque_iteration(liste):

      for nombre in liste:
            random_nombre = random.randint(0,4)
            if random_nombre == nombre:
                  random_nombre = random.randint(0,4)