s,k,u=map(int, input().split())
keyboard=list(map(int, input().split()))
usb=list(map(int, input().split()))
k_max=max(keyboard)
u_max=max(usb)
max_so_far=-1
for i in keyboard:
    for j in usb:
        temp=i+j
        if(temp<= s and temp>max_so_far):
            max_so_far=temp
print(max_so_far)
