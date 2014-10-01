import hubo_ach as ha
import ach
import sys
import time
from ctypes import *

# starting up straight
time.sleep(5)
s=0
x=0.01
print "shifting weights to the right foot." 
while x < .16: 
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] = x
	ref.ref[ha.LHR] = x
	ref.ref[ha.RAR]=-x
	x=x+.01
	time.sleep(.5)
	r.put(ref)
	r.close()
	s.close()
time.sleep(5)
print "lift left foot"
y=0
while y<1.3:
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] = .15
	ref.ref[ha.LHR] = .15
	ref.ref[ha.RAR]=-.15	
	ref.ref[ha.LHP]=-y
	ref.ref[ha.LKN]=y
	y=y+0.01
	time.sleep(.5)
	r.put(ref)
	r.close()
	s.close()
z=0
a=0
print "move up and down 2 times .2m"
while z<2:
	while a<1.5:#going down
		s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
		r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
		state = ha.HUBO_STATE()
		ref = ha.HUBO_REF()
		[statuss, framesizes] = s.get(state, wait=False,last=False)	
		ref.ref[ha.RHR] = .15
		ref.ref[ha.LHR] = .15
		ref.ref[ha.RAR]=-.15
		ref.ref[ha.LHP]=-1.3
		ref.ref[ha.LKN]=1.3	
		ref.ref[ha.RAP]= -a/2
		ref.ref[ha.RHP]= -a/2
		ref.ref[ha.RKN]=a
		a=a+0.1
		time.sleep(.5)
		r.put(ref)
		r.close()
		s.close()
	while a>0:#going up
		s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
		r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
		state = ha.HUBO_STATE()
		ref = ha.HUBO_REF()
		[statuss, framesizes] = s.get(state, wait=False,last=False)	
		ref.ref[ha.RHR] = .15
		ref.ref[ha.LHR] = .15
		ref.ref[ha.RAR]=-.15
		ref.ref[ha.LHP]=-1.3
		ref.ref[ha.LKN]=1.3	
		ref.ref[ha.RAP]= -a/2
		ref.ref[ha.RHP]= -a/2
		ref.ref[ha.RKN]=a
		a=a-0.1
		time.sleep(.5)
		r.put(ref)
		r.close()
		s.close()
	z=z+1
	print z
#straighten- unnecessary can just put wait
#b=0
#while b>0:
#		s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
#		r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
#		state = ha.HUBO_STATE()
#		ref = ha.HUBO_REF()
#		[statuss, framesizes] = s.get(state, wait=False,last=False)	
#		ref.ref[ha.RHR] = .15
#		ref.ref[ha.LHR] = .15
#		ref.ref[ha.RAR]=-.15
#		ref.ref[ha.LHP]=-1.3
#		ref.ref[ha.LKN]=1.3	
#		ref.ref[ha.RAP]= -a
#		ref.ref[ha.RHP]= -a
#		ref.ref[ha.RKN]=a
#		b=b-0.1
#		time.sleep(.5)
#		r.put(ref)
#		r.close()
#		s.close()
time.sleep(3)
print "put leg down"
c=1.3
while c>0:
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] = .15
	ref.ref[ha.LHR] = .15
	ref.ref[ha.RAR]=-.15	
	ref.ref[ha.LHP]=-c
	ref.ref[ha.LKN]=c
	c=c-0.01
	time.sleep(.2)
	r.put(ref)
	r.close()
	s.close()

#going back to origin
d=.16
while d > 0: 
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] = d
	ref.ref[ha.LHR] = d
	ref.ref[ha.RAR]=-d
	d=d-.01
	time.sleep(.5)
	r.put(ref)
	r.close()
	s.close()
time.sleep(7)
#SHifting weight to LEFT leg
e=0
while e < .16: 
	print "shifting W to right leg"
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] = -e
	ref.ref[ha.LHR] = -e
	ref.ref[ha.LAR]=e
	e=e+.01
	time.sleep(.5)
	r.put(ref)
	r.close()
	s.close()
time.sleep(5)
f=0
print "raising right leg"
while f<1.3:
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] =-.16
	ref.ref[ha.LHR] =-.16
	ref.ref[ha.LAR]=.16	
	ref.ref[ha.RHP]=-f
	ref.ref[ha.RKN]=f
	f=f+0.01
	time.sleep(.5)
	r.put(ref)
	r.close()
	s.close()
#move up and down 2 times .1m
z=0
a=0
print "flexing leg"
while z<2:
	while a<.75:#going down
		s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
		r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
		state = ha.HUBO_STATE()
		ref = ha.HUBO_REF()
		[statuss, framesizes] = s.get(state, wait=False,last=False)	
		ref.ref[ha.RHR] = -.16
		ref.ref[ha.LHR] = -.16
		ref.ref[ha.LAR]=.16
		ref.ref[ha.RHP]=-1.3
		ref.ref[ha.RKN]=1.3	
		ref.ref[ha.LAP]= -a/2
		ref.ref[ha.LHP]= -a/2
		ref.ref[ha.LKN]=a
		#print "JointRKN = ", state.joint[ha.LHP].pos
	 	a=a+0.1
		#print "a=",a		
		time.sleep(.5)
		r.put(ref)
		r.close()
		s.close()
	while a>0:#going up
		s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
		r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
		state = ha.HUBO_STATE()
		ref = ha.HUBO_REF()
		[statuss, framesizes] = s.get(state, wait=False,last=False)	
		ref.ref[ha.RHR] = -.16
		ref.ref[ha.LHR] = -.16
		ref.ref[ha.LAR]=.16
		ref.ref[ha.RHP]=-1.3
		ref.ref[ha.RKN]=1.3	
		ref.ref[ha.LAP]= -a/2
		ref.ref[ha.LHP]= -a/2
		ref.ref[ha.LKN]=a
		#print "JointRKN = ", state.joint[ha.LHP].pos
	 	a=a-0.1
		time.sleep(.5)
		r.put(ref)
		r.close()
		s.close()
	z=z+1
	print z
#put leg down
g=1.3
print "putting leg down"
while g>0:
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] = -.16
	ref.ref[ha.LHR] = -.16
	ref.ref[ha.LAR]=.16	
	ref.ref[ha.RHP]=-g
	ref.ref[ha.RKN]=g
	g=g-0.01
	time.sleep(.2)
	r.put(ref)
	r.close()
	s.close()
#shift weight back: 
h=.16
while h > 0: 
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] = -h
	ref.ref[ha.LHR] = -h
	ref.ref[ha.LAR]=h
	h=h-.01
	time.sleep(.5)
	r.put(ref)
	r.close()
	s.close()
time.sleep(7)

print "done"
