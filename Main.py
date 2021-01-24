import pygame
from random import randrange
from time import sleep
run=True
win=pygame.display.set_mode((300,350))
img=pygame.image.load("Block.png")
pygame.font.init()
myfont = pygame.font.SysFont('Papyrus', 30,True)
angle=0
c=0
lag=2000
sort=False
score=0
new_score=0
class block:
	def __init__(self,x,y):
		self.x=x
		self.y=y
def dostuf(score):
	old.sort(key=lambda x: x.y, reverse=False)
	score=disappear(score)
	return score
def disappear(score):
	curry=old[0].y
	deleted=[]
	count=0
	new_score=0
	for s in old:
		if curry==s.y:
			count+=1
		elif curry!=s.y:
			count=1
			curry=s.y
		if count==15:
			for v in old:
				if v.y+1>curry and v.y-1<curry:
					deleted.append(v)
				elif v.y<curry:
					v.y+=20
			count=0
	if len(deleted)!=0:
		for i in deleted:
			old.pop(old.index(i))
		new_score=(len(deleted)/15)**2
	return new_score
curr=[]
old=[]
NO=True
runny=False
count=0
score=0
timer=0
while run:
	if timer>0:
		timer-=1
	if len(old)!=0:
		for i in old:
			if i.y<=0:
				run=False
	lag=400
	texty=myfont.render(('score:'+str(score)), False, (255, 0, 0))
	win.blit(texty,(100,310))
	if len(curr)==0:
		x=randrange(7)
		if x==0:
			curr.append(block(240-100,0))
			curr.append(block(240-100,-20))
			curr.append(block(240-100,-40))
			curr.append(block(240-100,-60))
		elif x==1:
			curr.append(block(240-100,0))
			curr.append(block(240-100,-20))
			curr.append(block(260-100,0))
			curr.append(block(260-100,-20))
		elif x==2:
			curr.append(block(220-100,0))
			curr.append(block(240-100,0))
			curr.append(block(260-100,0))
			curr.append(block(240-100,-20))
		elif x==3:
			curr.append(block(220-100,0))
			curr.append(block(240-100,0))
			curr.append(block(220-100,-40))
			curr.append(block(220-100,-20))
		elif x==4:
			curr.append(block(240-100,0))
			curr.append(block(220-100,0))
			curr.append(block(240-100,-40))
			curr.append(block(240-100,-20))
		elif x==5:
			curr.append(block(240-100,0))
			curr.append(block(260-100,0))
			curr.append(block(240-100,-20))
			curr.append(block(220-100,-20))
		elif x==6:
			curr.append(block(220-100,0))
			curr.append(block(240-100,0))
			curr.append(block(260-100,-20))
			curr.append(block(240-100,-20))
	keys=pygame.key.get_pressed()
	if keys[pygame.K_DOWN]:
		lag_mod=5
	else:
		lag_mod=1
	for events in pygame.event.get():
		if events.type==pygame.QUIT:
			run=False
	if c%(lag//2)==0:
		if keys[pygame.K_RIGHT]:
			for i in curr:
				if i.x>=280:
					NO=False
				for j in old:
					if i.y==j.y and i.x+20==j.x:
						NO=False
			if NO:
				for i in curr:
					i.x+=20
		if keys[pygame.K_LEFT]:
			for i in curr:
				if i.x<=0:
					NO=False
				for j in old:
					if i.y==j.y and i.x-20==j.x:
						NO=False
			if NO:
				for i in curr:
					i.x-=20
	if keys[pygame.K_UP] and timer==0:
		timer=400
		if x==0:
			angle+=1
			y1=curr[0].y
			x1=curr[0].x
			curr=[]
			if angle%2==1:
				curr.append(block(x1,y1))
				curr.append(block(x1+20,y1))
				curr.append(block(x1+40,y1))
				curr.append(block(x1+60,y1))
			else:
				curr.append(block(x1,y1))
				curr.append(block(x1,y1+20))
				curr.append(block(x1,y1+40))
				curr.append(block(x1,y1+60))
		elif x==1:
			pass
		elif x==2:
			angle+=1
			y1=curr[-1].y
			x1=curr[-1].x
			curr=[]
			angle%=4
			if angle==1:
				curr.append(block(x1,y1-20))
				curr.append(block(x1,y1+20))
				curr.append(block(x1+20,y1))
				curr.append(block(x1,y1))
			if angle==3:
				curr.append(block(x1,y1-20))
				curr.append(block(x1,y1+20))
				curr.append(block(x1-20,y1))
				curr.append(block(x1,y1))
			if angle==2:
				curr.append(block(x1+20,y1))
				curr.append(block(x1-20,y1))
				curr.append(block(x1,y1+20))
				curr.append(block(x1,y1))
			elif angle==0:
				curr.append(block(x1,y1+20))
				curr.append(block(x1-20,y1+20))
				curr.append(block(x1+20,y1+20))
				curr.append(block(x1,y1))
		elif x==6:
			angle+=1
			y1=curr[0].y
			x1=curr[0].x
			curr=[]
			if angle%2==1:
				curr.append(block(x1-20,y1+20))
				curr.append(block(x1,y1+20))
				curr.append(block(x1,y1+40))
				curr.append(block(x1-20,y1))
			else:
				curr.append(block(x1+20,y1))
				curr.append(block(x1,y1+20))
				curr.append(block(x1-20,y1+20))
				curr.append(block(x1,y1))

		elif x==5:
			angle+=1
			y1=curr[0].y
			x1=curr[0].x
			curr=[]
			if angle%2==0:
				curr.append(block(x1,y1))
				curr.append(block(x1+20,y1))
				curr.append(block(x1,y1-20))
				curr.append(block(x1-20,y1-20))
			else:
				curr.append(block(x1,y1))
				curr.append(block(x1,y1-20))
				curr.append(block(x1+20,y1-20))
				curr.append(block(x1+20,y1-40))
		elif x==4:
			angle+=1
			y1=curr[-1].y
			x1=curr[-1].x
			curr=[]
			angle%=4
			if angle==1:
				curr.append(block(x1+20,y1))
				curr.append(block(x1-20,y1-20))
				curr.append(block(x1-20,y1))				
				curr.append(block(x1,y1))
			if angle==2:
				curr.append(block(x1,y1+20))
				curr.append(block(x1,y1-20))
				curr.append(block(x1+20,y1-20))				
				curr.append(block(x1,y1))
			if angle==3:
				curr.append(block(x1+20,y1))
				curr.append(block(x1+20,y1+20))
				curr.append(block(x1-20,y1))				
				curr.append(block(x1,y1))
			if angle==0:
				curr.append(block(x1,y1+20))
				curr.append(block(x1,y1-20))
				curr.append(block(x1-20,y1+20))				
				curr.append(block(x1,y1))
		elif x==3:
			angle+=1
			y1=curr[-1].y
			x1=curr[-1].x
			curr=[]
			angle%=4
			if angle==1:
				curr.append(block(x1+20,y1))
				curr.append(block(x1-20,y1+20))
				curr.append(block(x1-20,y1))				
				curr.append(block(x1,y1))
			if angle==2:
				curr.append(block(x1,y1+20))
				curr.append(block(x1,y1-20))
				curr.append(block(x1-20,y1-20))				
				curr.append(block(x1,y1))
			if angle==3:
				curr.append(block(x1+20,y1))
				curr.append(block(x1+20,y1-20))
				curr.append(block(x1-20,y1))				
				curr.append(block(x1,y1))
			if angle==0:
				curr.append(block(x1,y1+20))
				curr.append(block(x1,y1-20))
				curr.append(block(x1+20,y1+20))				
				curr.append(block(x1,y1))
	for i in curr:
		win.blit(img,(i.x,i.y))
		if c%((lag/lag_mod)//1)==0:
			if i.y==280:
				for j in curr:
					j.y-=20
					old.append(j)
				curr=[]
				angle=0
				sort=True
			for m in old:
				if i.x==m.x and i.y+20==m.y:
					for j in curr:
						j.y-=20
						old.append(j)
						score+=dostuf(score)
					curr=[]
					angle=0
					break
			i.y+=20
	if sort:
		score+=dostuf(score)
		sort=False
	for i in old:
		win.blit(img,(i.x,i.y))
	pygame.display.update()
	c+=1
	win.fill((0,0,0))
	NO=True