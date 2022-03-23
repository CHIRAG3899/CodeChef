#There are N cities in Chefland numbered from 1 to N and every city has a railway station. Some cities have a train and each city has at most one train originating from it. The trains are represented by an array A, where Ai=0 means the i-th city doesn't have any train originating from it, Ai=1 means the train originating from the i-th city is moving right (to a higher numbered city), and Ai=2 means the train originating from the i-th city is moving left (to a lower numbered city).
#Each train keeps on going forever in its direction and takes 1 minute to travel from the current station to the next one. There is a special station at city 1 which lets travellers instantaneously teleport to any other station that currently has a train. Teleportation and getting on a train once in the city both take 0 minutes and all trains start at time 0.
#There are M travellers at city 1, and the i-th traveller has destination city Bi. They ask Chef to guide them to teleport to a particular station from which they can catch a train to go to their destination in the least time possible. In case it's not possible for a person to reach his destination, print −1.
#Note: The input and output of this problem are large, so prefer using fast input/output methods.
#Input
#The first line contains an integer T, the number of test cases. Then the test cases follow.
#Each test case contains three lines of input.
#The first line contains two integers N, M.
#The second line contains N integers A1,A2,…,AN.
#The third line contains M integers B1,B2,…,BM.
#Output
#For each test case, output M space-separated integers C1,C2,…,CM, where Ci is the minimum time required by the i-th traveller to reach his destination and if the i-th traveller can't reach his destination, Ci=−1.
#Sample Input
#3
#5 1
#1 0 0 0 0
#5
#5 1
#1 0 0 0 2
#4
#5 2
#2 0 0 0 1
#3 1
#Sample Output
#4
#1
#-1 0
#Explanation
#Test Case 1: The only person takes the train from station 1 and hence takes |5−1|=4 minutes to reach his destination.
#Test Case 2: The only person takes the train from station 5 and hence takes |5−4|=1 minute to reach his destination.
#Test Case 3: Since no train passes station 3, it's impossible for the first person to reach his destination and since the second person is already at station 1, it takes him 0 minutes to reach his destination.

from sys import stdin

def travel_times():
    city_ct, pax_ct = map(int, stdin.readline().split())
    trains = list(map(int, stdin.readline().split()))
    pax_dest = list(map(int, stdin.readline().split()))

    ups = []
    downs = []
    for city, dirn in enumerate(trains, start=1):
        if dirn == 1:
            ups.append(city)
        elif dirn == 2:
            downs.append(city)
    ups.append(city_ct+1)
    downs.reverse()
    downs.append(0)

    time = [-1]*(city_ct + 1)
    u_from = ups[0]
    for u_to in ups[1:]:
        time[u_from:u_to] = range(u_to-u_from)
        u_from = u_to
    d_from = downs[0]
    for d_to in downs[1:]:
        t = 0
        for dest in range(d_from, d_to, -1):
            if t < time[dest] or time[dest] < 0:
                time[dest] = t
            t += 1
        d_from = d_to
    time[1] = 0 # no matter what

    return ' '.join(str(time[d]) for d in pax_dest)


# ===================== #

if __name__ == "__main__":
    T = int(input())
    print(*(travel_times() for _ in range(T)), sep = '\n')
