# Valtix-Coding-Excercise
The repository contains all the details/code to solve the Valtix coding execercise

**Problem Statement:**


<img width="801" alt="Screenshot 2022-11-19 at 12 22 24 AM" src="https://user-images.githubusercontent.com/118561751/202780898-1e7126ef-206f-48da-a16f-d83b0ed12434.png">

**Solution:**

<img width="944" alt="Screenshot 2022-11-19 at 12 41 32 AM" src="https://user-images.githubusercontent.com/118561751/202784081-ff3c0fe7-7b36-4bbc-9149-ad7f1b34bce1.png">
<img width="840" alt="Screenshot 2022-11-19 at 12 41 56 AM" src="https://user-images.githubusercontent.com/118561751/202784137-4d228221-1feb-4ade-8cc5-30a349c3c2c1.png">
<img width="798" alt="Screenshot 2022-11-19 at 12 42 07 AM" src="https://user-images.githubusercontent.com/118561751/202784162-3783d48a-e5f2-47d2-8376-cd7357f40b20.png">

**Test cases Executed**

1, Allocate memory 3000 
  - This will split the node 3 and create a new mode m3-1 and inserted into the linked list after split node
  - After allocation done verify the new node m3-1 has become the head with the right splitted value added

Code executed:  Memory needs to be allocated is 3000

Head of the linked list is M1

The initial LL after the initial node and memory allocation done
M1: 1000 -> M2: 1500 -> M3: 1500 -> M4: 1000 -> M5: 1500

To Allocate the needed memory we need to be splitting the node 
and creating a new node with the remaining memory after allocation

The node identified to split is M3

Print the LL with the new added split node
M1: 1000 -> M2: 1500 -> M3: 500 -> M3-1: 1000 -> M4: 1000 -> M5: 1500

The new LL after allocation done successfully
M3-1: 1000 -> M4: 1000 -> M5: 1500

2, Allocate memory 2500
   - This will not split the nodes - since m1 and m2 added will result in 2500 so no split is needed
   - The M3 will become the new head of the linked list after successful memory allocation

Head of the linked list is M1

The initial LL after the initial node and memory allocation done
M1: 1000 -> M2: 1500 -> M3: 1500 -> M4: 1000 -> M5: 1500

Able to allocate the memory for the given mem len without node split

Print the LL with the new added split node
M1: 1000 -> M2: 1500 -> M3: 1500 -> M4: 1000 -> M5: 1500

The new LL after allocation done successfully
M3: 1500 -> M4: 1000 -> M5: 1500

