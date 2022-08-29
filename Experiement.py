instru1
instru2
instru3
instru4
instru5


c = var([4,3,6,3,5],2)

a = var([4,3,()],2)
a = var([1,1,1,0], 1)

a = var([3,3,3,3]+[0,0,0,0,0,0,1], .1)   ##working
a = var([3,1,3]+[0,0,0,1], .1)   ##working
a = var([3,3, 3]+[0,0,0], .1)
a = var(([0,0,3,0,0))








a= var([0,0,1],1)
a = var([0,0,0,0],0.2)
b = var([1,0,1,0], 0.2)
b = var([4], 0.2)
b = ([3,3,3,3]+[0,0,0,0,0,0,2], .1)
a = ([0], 0.1)
a =   ([0,1,0,0])
a = var([0,1],[0,1])


#Melody
c =  ([1,2,3,4,5,6,7,8])


Clock.bpm=154
p1 >> pluck(dur=1/4, amp=[1, 1/2, 1/2, 1, 0,0,0 , 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1]
)# Default samples
p1 >> play("x-o-x")
#--Kick1 ----------------------------------
p1 >> MidiOut (a,channel=1,dur=[.251,.251,.251,.251,rest(.51)], oct=3  )
p1 >> MidiOut (a,channel=1,dur=[.251,.251,rest(.51),.251,rest(.51)], oct=3  )
p1 >> MidiOut (a,channel=1,dur=[.451], oct=3  )
p2 >> MidiOut (a,channel=1,dur=[.51], oct=3 )
p2.sus = 4
b1 >> sawbass(var([0,1,-2],[8,8,16]), dur=PDur(5,16), cutoff=P[1000,5000][:5], sus=1/2)

p1 >> MidiOut((2,[4,4,4,4,5],6,[8,8,9]), channel=1,dur=1/4, sus=1/2, vib=0, pan=PWhite(-1,1), vibdepth=0.02, coarse=0, oct=[4,5],)
clear();
p1.stop()
p2.stop()
p1 >> MidiOut(a,channel=1,oct=3) ## Les crochets carrés définissent une séquence

p1 >> MidiOut (a,channel=1,dur=[.1,rest(.51),.3,.4,rest(.51),.1,rest(.51)], oct=3  )
p1 >> MidiOut (a,channel=1,dur=[.3,rest(.51),.3,.1,rest(.51),.3,rest(.51)], oct=3  )
p1 >> MidiOut (a,channel=1,dur=[ .1,rest(.51),.1], oct=3  )



#--Snar ----------------------------------
p2 >> MidiOut (b,channel=3, dur=.5, oct=3  )
p2 >> MidiOut (b,channel=3, dur=.25, oct=2.5  )


p3 >> MidiOut (c,channel=2, dur=.25, oct=3  )
##p2.stutter(4)

#--basss ----------------------------------
p4 >> MidiOut (c,channel=2, dur=8, oct=3 )
p4 >>  MidiOut ([0,7,6,4,2], dur=1/2, sus=1,,channel=2, dur=8, oct=3)

#--lead ----------------------------------

p5 >> MidiOut (b,channel=3, dur=PDur(1,4)*0.25, oct=3 )



#-drum--------------------------------------
p2 >> play("x--X")
p2 >> play("x---X")

p2 >> play("xX--Xx")
p1.stop()
p5.stop()
Clock.clear()
