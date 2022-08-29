bpm=[120,160*2]
Clock.bpm = 180 #120


## battery

### kick
k=P[0,0,0,0]

p1 >> MidiOut(k,dur=1,channel=0,oct=3)
Clock.clear()
p1 >> p1.stop()



###hithat
h1 >> MidiOut([3.5,3.5,1.5,[5.5]]*2,dur=1/2,channel=1,oct=3)
h1.stop()
###snar

s1 >> MidiOut(P[1,1,rest(1),1],dur=1/2,channel=1,oct=3)
s1.stop()
### bass
p2 >> MidiOut(P[0,0,0,0],dur=1/4,channel=2,oct=3)
Clock.clear()
p2.stop()
### bass
b2 >> MidiOut(P[3.5,3.5,3.5,3.5,[5.5,5.5]],dur=1/2,channel=3,oct=3)
h1.stop()

b1 >> MidiOut(P[1,1,rest(1),1],dur=1/2,channel=3,oct=3)


# melodie
melk = P[5,rest(4),4,3,2,1,1,1]*2
melki = melk.reverse()
melko = P[5,4,3,2].shuffle()
melk = P[5,4,3,2]

melkmaster=[melk,melki,melko]



## key
e1 >> MidiOut(melki[:],sus=.12,dur=1/,channel=4,oct=2).stop()
e2 >> MidiOut([1,4,4,14].reverse(),sus=.02,dur=1/1.5,channel=4,oct=2) #.stop()
e2 >> MidiOut(P[1,2,[3,4],5].reverse(),sus=.02,dur=1/1.5,channel=4,oct=2) #.stop()


e2 >> scatter(1,3,-3 )
e1 >> MidiOut([9,4,19,14,9,4,19,14].reverse(),sus=.02,dur=1/1.5,channel=4,oct=4)
e1 >> MidiOut(arp(1,4),sus=.02,dur=1/1.5,channel=4,oct=4)


## bass
b1 >> MidiOut(melk,dur=1,oct=P[1,2]*3,channel=3)



## lead
l1 >> MidiOut(melkmaster,dur=8,channel=4,oct=3,sus=16)
l1 >> MidiOut(P[(0,3,5), (1,4,6), (2,5,7), (4,7,9)], dur=4,sus=4,channel=5,oct=4) #.stop()
l1.every(1,"stutter")

## pad
p1.stop()
p8 >> MidiOut(linvar([0, 2],[2, 4]*10).reverse(),sus=1,dur=1/2,channel=6,oct=6)
p7.stop()
p8.every(5,"stutter")

## stab
t1 >> MidiOut(2,dur=1/4,channel=16)

#group
Group(b1,l1).solo

##### notes ####
# object

Clock.clear()
